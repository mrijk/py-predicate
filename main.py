import json as json_lib
import sys
from typing import Annotated

import typer
from more_itertools import take

from predicate import generate_true
from predicate import optimize as optimize_predicate
from predicate.formatter import to_dot, to_json, to_latex
from predicate.parser import parse_expression
from predicate.predicate import Predicate
from predicate.truth_table import get_named_predicates, truth_table

app = typer.Typer()

Number = Annotated[int, typer.Option("--number", "-n", help="Number of values to generate")]
Expression = Annotated[str, typer.Argument(help="Predicate expression")]
Optimize = Annotated[bool, typer.Option("--optimize", "-o", help="Enable predicate optimization")]


@app.command("dot", help="Output predicate as a dot (Graphviz) file")
def dot(expression: str, optimize: Optimize = False) -> None:
    if predicate := expression_to_predicate(expression):
        graph = to_dot(predicate, repr(predicate), show_optimized=optimize)
        graph.render("/tmp/predicate.gv", view=True)  # noqa: S108
    else:
        failed_to_pass(expression)


@app.command("json", help="Output predicate as json")
def json(expression: Expression, optimize: Optimize = False) -> None:
    if predicate := expression_to_predicate(expression, optimize):
        sys.stdout.write(json_lib.dumps(to_json(predicate)))
    else:
        failed_to_pass(expression)


@app.command("latex", help="Output predicate as LaTeX")
def latex(expression: Expression, optimize: Optimize = False) -> None:
    if predicate := expression_to_predicate(expression, optimize):
        sys.stdout.write(to_latex(predicate))
    else:
        failed_to_pass(expression)


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

    if predicate := expression_to_predicate(expression, optimize):
        sys.stdout.write(f"{format_header(predicate)}\n")
        for row in truth_table(predicate):
            sys.stdout.write(f"{format_values(row[0])}:   {as_bit(row[1])}\n")
    else:
        failed_to_pass(expression)


@app.command("generate", help="Generate values based on the predicate expression")
def generate(expression: Expression, number: Number = 10) -> None:
    if predicate := expression_to_predicate(expression):
        if values := take(number, generate_true(predicate)):
            for value in values:
                sys.stdout.write(f"{value}\n")
        else:
            sys.stderr.write(f"Could not generate True values for predicate `{predicate}`\n")
    else:
        failed_to_pass(expression)


def failed_to_pass(expression: str) -> None:
    sys.stderr.write(f'Could not parse expression: "{expression}"\n')


def expression_to_predicate(expression: str, optimize: bool = False) -> Predicate | None:
    if predicate := parse_expression(expression):
        return optimize_predicate(predicate) if optimize else predicate
    return None


if __name__ == "__main__":
    app()
