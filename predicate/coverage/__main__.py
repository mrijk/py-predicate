import json
from pathlib import Path
from typing import Annotated

import typer

from predicate.coverage.purity import analyze, summarize

app = typer.Typer(add_completion=False)


@app.command()
def purity(
    path: Annotated[Path, typer.Argument(exists=True, help="Python file or directory to analyze")],
    snapshot: Annotated[
        Path | None, typer.Option("--snapshot", "-o", help="Write a JSON snapshot of every function scanned")
    ] = None,
) -> None:
    """Report pure and impure public functions. Note: this imports (executes) the analyzed modules."""
    modules = analyze(path)
    if snapshot is not None:
        snapshot.write_text(json.dumps(modules, indent=2) + "\n")
    summary = summarize(modules)
    total = summary["total"]
    percentage = 100 * summary["pure"] / total if total else 0
    typer.echo(f"{summary['pure']}/{total} public functions pure ({percentage:.0f}%), {summary['impure']} impure")
    for module in modules:
        if "error" in module:
            typer.echo(f"{module['path']}: ERROR {module['error']}")
        for fn in module["functions"]:
            typer.echo(f"{module['path']}:{fn['line']} {fn['name']}: {'pure' if fn['pure'] else 'IMPURE'}")


if __name__ == "__main__":
    app()
