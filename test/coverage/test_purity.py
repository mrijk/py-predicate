import json
from pathlib import Path

from typer.testing import CliRunner

from predicate.coverage.__main__ import app
from predicate.coverage.purity import analyze, count_flaky, summarize, summarize_exercise

SOURCE = """
import random

def pure(x):
    return x

def impure(x):
    return x + random.random()

def _private(x):
    print(x)
"""


def test_analyze(tmp_path):
    (tmp_path / "mod.py").write_text(SOURCE)
    (tmp_path / "broken.py").write_text("import does_not_exist")

    modules = analyze(tmp_path)

    assert summarize(modules) == {"total": 2, "pure": 1, "impure": 1}
    by_file = {m["file_name"]: m for m in modules}
    assert [(f["name"], f["pure"]) for f in by_file["mod.py"]["functions"]] == [("pure", True), ("impure", False)]
    assert "ModuleNotFoundError" in by_file["broken.py"]["error"]


def test_cli_summary_and_snapshot(tmp_path):
    (tmp_path / "mod.py").write_text(SOURCE)
    snapshot = tmp_path / "snapshot.json"

    result = CliRunner().invoke(app, [str(tmp_path / "mod.py"), "-o", str(snapshot)])

    assert result.exit_code == 0
    assert "1/2 public functions pure (50%)" in result.output
    assert "impure: IMPURE" in result.output
    functions = json.loads(snapshot.read_text())[0]["functions"]
    assert functions[0] == {"name": "pure", "line": 4, "pure": True}
    assert functions[1] == {
        "name": "impure",
        "line": 7,
        "pure": False,
        "category": "randomness",
        "reason": "calls random.random (mod.py:8)",
    }


EXERCISE_SOURCE = """
import os

def add(x: int, y: int) -> int:
    return x + y

def wrong_return(x: int) -> int:
    return str(x)

def unannotated(x):
    return x

def raises(x: int) -> int:
    raise ValueError(x)

def writes_file(x: int) -> int:
    with open("sandbox_test_output.txt", "w") as f:
        f.write("hello")
    return x

def deletes_file(x: int) -> int:
    os.remove("PATH")
    return x

def swallows_violation(x: int) -> int:
    try:
        os.remove("PATH")
    except BaseException:
        pass
    return x

async def async_add(x: int) -> int:
    return x

def hangs(x: int) -> int:
    while True:
        pass

def exits(x: int) -> int:
    os._exit(3)
"""


def test_exercise_sandboxed(tmp_path):
    victim = tmp_path / "victim.txt"
    victim.write_text("precious")
    (tmp_path / "mod.py").write_text(EXERCISE_SOURCE.replace("PATH", str(victim)))

    modules = analyze(tmp_path / "mod.py", exercise=True, calls=3, timeout=5, runs=1)

    status = {f["name"]: f["exercise"]["status"] for f in modules[0]["functions"]}
    assert status == {
        "add": "ok",
        "wrong_return": "failed",
        "unannotated": "not-exercisable",
        "raises": "failed",
        "writes_file": "blocked",
        "deletes_file": "blocked",
        "swallows_violation": "blocked",
        "async_add": "ok",
        "hangs": "timeout",
        "exits": "crashed",
    }
    assert victim.read_text() == "precious"
    assert not list(tmp_path.glob("sandbox_test_output.txt"))
    assert not list(Path.cwd().glob("sandbox_test_output.txt"))
    assert summarize_exercise(modules)["blocked"] == 3


def test_cli_exercise(tmp_path):
    (tmp_path / "mod.py").write_text(EXERCISE_SOURCE.split("def hangs")[0])

    result = CliRunner().invoke(app, [str(tmp_path / "mod.py"), "--exercise", "-n", "2", "--runs", "1"])

    assert result.exit_code == 0
    assert "add: pure, exercise: ok" in result.output
    assert "security boundary" in result.output


def test_flaky(monkeypatch, tmp_path):
    outcomes = iter(["ok", "failed", "ok", "ok", "ok", "ok"])
    monkeypatch.setattr(
        "predicate.coverage.purity.exercise_sandboxed",
        lambda *args: {"status": next(outcomes), "detail": "boom"},
    )
    (tmp_path / "mod.py").write_text("def f(x: int) -> int:\n    return x\n\ndef g(x: int) -> int:\n    return x\n")

    modules = analyze(tmp_path / "mod.py", exercise=True, jobs=1)

    f, g = (fn["exercise"] for fn in modules[0]["functions"])
    assert f == {"status": "failed", "detail": "boom", "runs": 3, "flaky": True, "statuses": {"ok": 2, "failed": 1}}
    assert g["flaky"] is False
    assert g["statuses"] == {"ok": 3}
    assert count_flaky(modules) == 1


def test_cli_failed_only(tmp_path):
    (tmp_path / "mod.py").write_text(EXERCISE_SOURCE.replace("PATH", str(tmp_path / "x")).split("def hangs")[0])
    snapshot = tmp_path / "snapshot.json"

    result = CliRunner().invoke(
        app, [str(tmp_path / "mod.py"), "--exercise", "--failed", "--runs", "1", "-o", str(snapshot)]
    )

    assert result.exit_code == 0
    names = [f["name"] for f in json.loads(snapshot.read_text())[0]["functions"]]
    assert names == ["wrong_return", "raises", "writes_file", "deletes_file", "swallows_violation"]
    assert "add:" not in result.output
    assert "exercise: {" in result.output  # the totals still cover every function


def test_cli_failed_needs_exercise(tmp_path):
    (tmp_path / "mod.py").write_text("def f(x: int) -> int:\n    return x\n")

    assert CliRunner().invoke(app, [str(tmp_path / "mod.py"), "--failed"]).exit_code != 0


def test_exercise_detects_mutated_arguments(tmp_path):
    (tmp_path / "mod.py").write_text(
        "def append(lst: list[int], x: int) -> None:\n    lst.append(x)\n\n\n"
        "def concat(lst: list[int], x: int) -> list[int]:\n    return [*lst, x]\n"
    )

    modules = analyze(tmp_path / "mod.py", exercise=True, calls=5, timeout=5, runs=1)

    exercise = {f["name"]: f["exercise"] for f in modules[0]["functions"]}
    assert exercise["append"] == exercise["append"] | {"status": "mutates-args", "detail": "mutates lst"}
    assert exercise["concat"]["status"] == "ok"


def test_exercise_arguments_that_cannot_be_copied(tmp_path):
    (tmp_path / "mod.py").write_text(
        "from collections.abc import AsyncIterable\n\n\n"
        "async def first(values: AsyncIterable[int]) -> int | None:\n"
        "    async for value in values:\n        return value\n    return None\n"
    )

    modules = analyze(tmp_path / "mod.py", exercise=True, calls=5, timeout=5, runs=1)

    assert modules[0]["functions"][0]["exercise"]["status"] == "ok"


def test_exercise_function_with_a_parameter_named_old(tmp_path):
    (tmp_path / "mod.py").write_text(
        "def replace(s: str, old: str, new: str) -> str:\n    return s.replace(old, new)\n"
    )

    modules = analyze(tmp_path / "mod.py", exercise=True, calls=5, timeout=5, runs=1)

    assert modules[0]["functions"][0]["exercise"]["status"] == "ok"


def test_exercise_importing_ctypes_is_not_blocked_but_loading_a_library_is(tmp_path):
    (tmp_path / "mod.py").write_text(
        "def imports_ctypes(x: int) -> int:\n    import ctypes\n\n    return x + ctypes.sizeof(ctypes.c_int)\n\n\n"
        "def loads_library(x: int) -> int:\n    import ctypes\n\n    ctypes.CDLL('libc.so.6')\n    return x\n"
    )

    modules = analyze(tmp_path / "mod.py", exercise=True, calls=3, timeout=5, runs=1)

    exercise = {f["name"]: f["exercise"]["status"] for f in modules[0]["functions"]}
    assert exercise == {"imports_ctypes": "ok", "loads_library": "blocked"}
