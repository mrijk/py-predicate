import json
from pathlib import Path
from typing import Annotated

import typer

from predicate.coverage.purity import (
    FunctionInfo,
    ModuleInfo,
    analyze,
    count_flaky,
    failed_only,
    summarize,
    summarize_exercise,
)

app = typer.Typer(add_completion=False)

WARNING = (
    "Exercising functions in sandboxed subprocesses: file writes and deletes, spawning processes and network "
    "access are blocked. This is a best-effort guard against accidents, not a security boundary."
)


@app.command()
def purity(
    path: Annotated[Path, typer.Argument(exists=True, help="Python file or directory to analyze")],
    snapshot: Annotated[
        Path | None, typer.Option("--snapshot", "-o", help="Write a JSON snapshot of every function scanned")
    ] = None,
    exercise: Annotated[bool, typer.Option("--exercise", help="Also exercise each function in a sandbox")] = False,
    calls: Annotated[int, typer.Option("--calls", "-n", help="Generated calls per function")] = 10,
    timeout: Annotated[float, typer.Option(help="Seconds before an exercised function is killed")] = 10.0,
    jobs: Annotated[int, typer.Option("--jobs", "-j", help="Functions exercised in parallel")] = 4,
    failed: Annotated[
        bool, typer.Option("--failed", help="With --exercise: only list/snapshot failed exercises")
    ] = False,
    runs: Annotated[int, typer.Option(help="Times each function is exercised; differing results are flaky")] = 5,
) -> None:
    """Report pure and impure public functions. Note: this imports (executes) the analyzed modules."""
    if failed and not exercise:
        raise typer.BadParameter("--failed needs --exercise")
    if exercise:
        typer.echo(WARNING, err=True)
    modules = analyze(path, exercise=exercise, calls=calls, timeout=timeout, jobs=jobs, runs=runs)
    shown = failed_only(modules) if failed else modules
    if snapshot is not None:
        snapshot.write_text(json.dumps(shown, indent=2) + "\n")
    _report(modules, shown, exercise)


def _report(modules: list[ModuleInfo], shown: list[ModuleInfo], exercise: bool) -> None:
    summary = summarize(modules)
    total = summary["total"]
    percentage = 100 * summary["pure"] / total if total else 0
    typer.echo(f"{summary['pure']}/{total} public functions pure ({percentage:.0f}%), {summary['impure']} impure")
    if exercise:
        typer.echo(f"exercise: {summarize_exercise(modules)}, {count_flaky(modules)} flaky")
    for module in shown:
        if "error" in module:
            typer.echo(f"{module['path']}: ERROR {module['error']}")
        for fn in module["functions"]:
            typer.echo(f"{module['path']}:{fn['line']} {fn['name']}: {_verdict(fn)}")


def _verdict(fn: FunctionInfo) -> str:
    result = "pure" if fn["pure"] else "IMPURE"
    outcome = fn.get("exercise")
    if outcome is None:
        return result
    return f"{result}, exercise: {outcome['status']}{' (FLAKY)' if outcome['flaky'] else ''}"


if __name__ == "__main__":
    app()
