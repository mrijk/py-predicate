import json as json_lib
import sys
from typing import Annotated

import typer

from predicate import Predicate, to_json
from predicate import optimize as optimize_predicate
from predicate.formatter.format_dot import to_dot
from predicate.optimizer.parser import parse_string
from predicate.truth_table import get_named_predicates, truth_table

app = typer.Typer()

Expression = Annotated[str, typer.Argument(help="Predicate expression")]
Optimize = Annotated[bool, typer.Option(help="Enable predicate optimization")]


@app.command("dot", help="Output predicate as a dot (Graphviz) file")
def dot(expression: str, optimize: Optimize = False) -> None:
    predicate = predicate_to_expression(expression, optimize)

    graph = to_dot(predicate, repr(predicate), show_optimized=optimize)
    graph.render("/tmp/predicate.gv", view=True)  # noqa: S108


@app.command("json", help="Output predicate as json")
def json(expression: str, optimize: Optimize = False) -> None:
    predicate = predicate_to_expression(expression, optimize)

    sys.stdout.write(json_lib.dumps(to_json(predicate)))


@app.command("table", help="Output predicate as a truth table")
def table(expression: Expression, optimize: Optimize = False) -> None:
    def as_bit(value: bool) -> int:
        return 1 if value else 0

    def format_header(predicate: Predicate) -> str:
        named_predicates = get_named_predicates(predicate)
        return " ".join(named_predicates)

    def format_values(values) -> str:
        bits = [str(as_bit(value)) for value in values]
        return " ".join(bits)

    predicate = predicate_to_expression(expression, optimize)

    sys.stdout.write(f"{format_header(predicate)}\n")
    for row in truth_table(predicate):
        sys.stdout.write(f"{format_values(row[0])}:   {as_bit(row[1])}\n")


def predicate_to_expression(expression: str, optimize: bool) -> Predicate:
    predicate = parse_string(expression)
    return optimize_predicate(predicate) if optimize else predicate


if __name__ == "__main__":
    app()
