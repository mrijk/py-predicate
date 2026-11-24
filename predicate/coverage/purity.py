import importlib.util
import inspect
import sys
from collections import Counter
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import ModuleType
from typing import Any

from predicate.coverage.sandbox import exercise_sandboxed
from predicate.is_pure_predicate import find_impurity


def _package_name(file: Path) -> tuple[Path, str] | None:
    """Return (root directory, dotted module name) if file lives in a package, otherwise None."""
    packages: list[str] = []
    directory = file.resolve().parent
    while (directory / "__init__.py").exists():
        packages.insert(0, directory.name)
        directory = directory.parent
    if not packages:
        return None
    return directory, ".".join(packages if file.stem == "__init__" else [*packages, file.stem])


def _load(file: Path) -> ModuleType:
    if (package := _package_name(file)) is not None:  # imported by name, so relative imports work
        root, name = package
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
        return importlib.import_module(name)
    name = f"_purity_{abs(hash(file.resolve()))}"
    spec = importlib.util.spec_from_file_location(name, file)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {file}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        del sys.modules[name]
        raise
    return module


def _public_functions(module: ModuleType) -> Iterator[tuple[str, Any]]:
    names = getattr(module, "__all__", None)
    return (
        (name, fn)
        for name, fn in inspect.getmembers(module, inspect.isfunction)
        if (name in names if names is not None else not name.startswith("_")) and fn.__module__ == module.__name__
    )


def _function_entry(name: str, fn: Any) -> dict[str, Any]:
    impurity = find_impurity(fn)
    entry = {"name": name, "line": fn.__code__.co_firstlineno, "pure": impurity is None}
    return entry if impurity is None else entry | {"category": impurity.category, "reason": impurity.reason}


def _analyze_file(file: Path) -> dict[str, Any]:
    try:
        module = _load(file)
    except BaseException as e:  # noqa: BLE001 - importing user code can fail in any way
        return {"path": str(file), "file_name": file.name, "error": f"{type(e).__name__}: {e}", "functions": []}
    functions = [_function_entry(name, fn) for name, fn in _public_functions(module)]
    return {"path": str(file), "file_name": file.name, "functions": sorted(functions, key=lambda f: f["line"])}


def _exercise_repeated(file: Path, name: str, calls: int, timeout: float, runs: int) -> dict[str, Any]:
    """Exercise a function `runs` times with fresh random inputs; differing statuses make the result flaky."""
    results = []
    for _ in range(runs):
        results.append(exercise_sandboxed(file, name, calls, timeout))
        if results[-1]["status"] == "not-exercisable":  # decided by the signature, repeating can't change it
            break
    statuses = Counter(r["status"] for r in results)
    first_problem = next((r for r in results if r["status"] != "ok"), results[0])
    return first_problem | {"runs": len(results), "flaky": len(statuses) > 1, "statuses": dict(statuses)}


def analyze(
    path: Path, *, exercise: bool = False, calls: int = 10, timeout: float = 10.0, jobs: int = 4, runs: int = 3
) -> list[dict[str, Any]]:
    """Report the purity of all public module-level functions found under path. Imports (executes) the modules.

    With exercise=True each function is also exercised `runs` times in a sandboxed subprocess, see
    predicate.coverage.sandbox.
    """
    files = [path] if path.is_file() else sorted(path.rglob("*.py"))
    modules = [_analyze_file(file) for file in files]
    if exercise:
        targets = [(Path(m["path"]), f) for m in modules for f in m["functions"]]
        with ThreadPoolExecutor(max_workers=jobs) as executor:
            results = executor.map(lambda t: _exercise_repeated(t[0], t[1]["name"], calls, timeout, runs), targets)
            for (_, function), result in zip(targets, results, strict=True):
                function["exercise"] = result
    return modules


def summarize(modules: list[dict[str, Any]]) -> dict[str, int]:
    functions = [f for m in modules for f in m["functions"]]
    pure = sum(f["pure"] for f in functions)
    return {"total": len(functions), "pure": pure, "impure": len(functions) - pure}


def summarize_exercise(modules: list[dict[str, Any]]) -> dict[str, int]:
    return dict(Counter(f["exercise"]["status"] for m in modules for f in m["functions"] if "exercise" in f))


def count_flaky(modules: list[dict[str, Any]]) -> int:
    return sum(f.get("exercise", {}).get("flaky", False) for m in modules for f in m["functions"])


def failed_only(modules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep only the functions whose exercise went wrong, and only the modules that still have any."""
    bad = {
        "failed",
        "mutates-args",
        "blocked",
        "timeout",
        "crashed",
    }  # not-exercisable is a property of the signature, not a failure
    kept = [m | {"functions": [f for f in m["functions"] if f["exercise"]["status"] in bad]} for m in modules]
    return [m for m in kept if m["functions"]]
