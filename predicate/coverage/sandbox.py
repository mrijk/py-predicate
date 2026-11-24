"""Exercise a function in a sandboxed subprocess, so that generated inputs can't cause lasting side effects.

The worker (run with `python -I -m predicate.coverage.sandbox FILE NAME CALLS`) installs an audit hook that blocks file
writes and deletes, spawning processes and network access before it loads the module. It runs in an empty temporary
directory with a minimal environment, and the parent kills it after a timeout.

ponytail: an audit hook is a guard against accidents, not a security boundary (ctypes or a C extension can bypass it).
Add OS-level isolation (sandbox-exec, bwrap, a container) if untrusted code must be exercised.
"""

import asyncio
import copy
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  # the worker imports predicate only after installing the audit hook
    from predicate.spec.spec import Spec

_WRITE_FLAGS = os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC
_BLOCKED_EVENTS = {
    "os.chmod", "os.chown", "os.chdir", "os.chroot", "os.kill", "os.killpg", "os.link", "os.mkdir", "os.putenv",
    "os.remove", "os.removexattr", "os.rename", "os.rmdir", "os.setxattr", "os.symlink", "os.system", "os.truncate",
    "os.unsetenv", "os.utime", "os.startfile", "pty.spawn", "sqlite3.connect", "tempfile.mkdtemp", "tempfile.mkstemp",
    "webbrowser.open", "urllib.Request",
}  # fmt: skip
_BLOCKED_PREFIXES = ("os.exec", "os.fork", "os.posix_spawn", "os.spawn", "shutil.", "socket.", "subprocess.", "ctypes.")
_RESULT_LIMIT = 500


class SandboxViolation(
    BaseException
):  # BaseException: the function under test can't swallow it with `except Exception`
    """Raised by the audit hook when the function tries something that isn't allowed."""


def _violation(event: str, args: tuple[Any, ...]) -> str | None:
    if event == "open":
        path, mode, flags = args
        writes = bool(set(mode or "") & set("wax+")) or bool((flags or 0) & _WRITE_FLAGS)
        return f"open {path} for writing" if writes and str(path) != os.devnull else None
    # creating a socket is harmless (asyncio does it for its event loop), using one is not
    blocked = event in _BLOCKED_EVENTS or (event.startswith(_BLOCKED_PREFIXES) and event != "socket.__new__")
    return f"{event} {args[:2]}"[:_RESULT_LIMIT] if blocked else None


def _install_audit_hook(violations: list[str]) -> None:
    def hook(event: str, args: tuple[Any, ...]) -> None:
        if reason := _violation(event, args):
            violations.append(reason)
            raise SandboxViolation(reason)

    sys.addaudithook(hook)


def _same(before: Any, after: Any) -> bool:
    # ponytail: == then repr without addresses, so a deep copy of an object without __eq__ counts as unchanged
    return bool(before == after) or _without_addresses(before) == _without_addresses(after)


def _without_addresses(value: Any) -> str:
    return re.sub(r"0x[0-9a-f]+", "0x", repr(value))


def _with_mutation_check(spec: "Spec", mutated: list[str]) -> "Spec":
    """Add a snapshot of deep-copied arguments (#238) and a `fn` that records the arguments the call changed."""

    def unchanged(old: dict[str, Any] | None = None, **current: Any) -> bool:  # no arguments: no snapshot, no old
        mutated.extend(k for k, v in (old or {}).items() if not _same(v, current[k]))
        return True

    return spec | {"snapshot": dict.fromkeys(spec["args"], copy.deepcopy), "fn": unchanged}


async def _consume_async(results: Any) -> int:
    return len([item async for item in results])


def _exercise(file: str, name: str, calls: int) -> dict[str, Any]:
    from predicate.coverage.purity import _load
    from predicate.spec.exercise import exercise
    from predicate.spec.exercise_function import get_spec_from_function_annotation
    from predicate.spec.spec import InvalidSpecError

    try:
        fn = getattr(_load(Path(file)), name)
        spec = get_spec_from_function_annotation(fn)
    except InvalidSpecError as e:
        return {"status": "not-exercisable", "detail": str(e)}
    mutated: list[str] = []
    results = exercise(fn, _with_mutation_check(spec, mutated), calls)
    count = asyncio.run(_consume_async(results)) if hasattr(results, "__aiter__") else len(list(results))
    if mutated:
        return {"status": "mutates-args", "detail": f"mutates {', '.join(sorted(set(mutated)))}"}
    return {"status": "ok", "calls": count}


def _worker(file: str, name: str, calls: int) -> None:
    sys.dont_write_bytecode = True
    real_stdout = sys.stdout
    violations: list[str] = []
    _install_audit_hook(violations)
    sys.stdout = sys.stderr = io.StringIO()  # whatever the function prints must not corrupt the result
    try:
        result = _exercise(file, name, calls)
    except BaseException as e:  # noqa: BLE001 - anything the function under test raises is a finding
        result = {"status": "failed", "detail": f"{type(e).__name__}: {e}"[:_RESULT_LIMIT]}
    if violations:  # also when the function swallowed the SandboxViolation
        result = {"status": "blocked", "detail": "; ".join(violations[:3])[:_RESULT_LIMIT]}
    print(json.dumps(result), file=real_stdout)


def exercise_sandboxed(file: Path, name: str, calls: int = 10, timeout: float = 10.0) -> dict[str, Any]:
    """Exercise file's function `name` with `calls` generated inputs. Returns a dict with status and detail/calls.

    Status is one of: ok, failed, mutates-args (changed an argument), blocked (tried a forbidden side effect), not-exercisable, timeout or crashed.
    """
    with tempfile.TemporaryDirectory() as cwd:
        env = {"PATH": os.environ.get("PATH", ""), "HOME": cwd, "LANG": "C.UTF-8"}
        command = [sys.executable, "-I", "-m", "predicate.coverage.sandbox", str(file.resolve()), name, str(calls)]
        try:
            process = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)  # noqa: S603
        except subprocess.TimeoutExpired:
            return {"status": "timeout", "detail": f"no result within {timeout}s"}
    try:
        return json.loads(process.stdout.strip().splitlines()[-1])  # type: ignore[no-any-return]
    except (IndexError, json.JSONDecodeError):
        detail = f"exit code {process.returncode}: {process.stderr.strip()[-200:]}"
        return {"status": "crashed", "detail": detail}


if __name__ == "__main__":
    _worker(sys.argv[1], sys.argv[2], int(sys.argv[3]))
