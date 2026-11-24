import json

from typer.testing import CliRunner

from predicate.coverage.__main__ import app
from predicate.coverage.purity import analyze, summarize

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
