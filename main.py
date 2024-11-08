import click

from predicate import FnPredicate
from predicate.formatter.format_dot import to_dot
from predicate.predicate import NamedPredicate
from predicate.standard_predicates import fn_p
from predicate.truth_table import get_named_predicates, truth_table


@click.command()
@click.option("-f", "--filename", help="Output file")
@click.option("-o", "--optimize", is_flag=True, help="Optimize predicate")
@click.option("-p", "--predicate", required=True, help="Predicate to parse")
@click.option("-t", "--truth", is_flag=True, help="Generate truth table")
def cli(predicate: str, filename, optimize: bool, truth: bool) -> None:

    if truth:
        show_truth_table(optimize)
        return

    # predicate_string = "true | false & true ^ ~false"

    # predicate_string = "x in {2, 3, 4} | x not in {4, 5}"

    # parsed = parse_string(predicate)

    p: FnPredicate = fn_p(lambda x: x > 2)
    q: FnPredicate = fn_p(lambda x: x > 3)
    # r: FnPredicate = fn_p(lambda x: x > 4)

    parsed = p ^ (p | q)

    dot = to_dot(parsed, predicate, show_optimized=optimize)

    dot.render("/tmp/predicate.gv", view=True)  # noqa: S108

    # print(json.dumps(to_json(predicate)))


def show_truth_table(optimize: bool) -> None:
    p = NamedPredicate(name="p")
    q = NamedPredicate(name="q")
    r = NamedPredicate(name="r")
    s = NamedPredicate(name="s")

    predicate = (p & q) ^ (r & s)

    def as_bit(value: bool) -> int:
        return 1 if value else 0

    def format_header() -> str:
        named_predicates = get_named_predicates(predicate)
        return " ".join(named_predicates)

    def format_values(values) -> str:
        bits = [str(as_bit(value)) for value in values]
        return " ".join(bits)

    print(format_header())  # noqa: T201
    for row in truth_table(predicate):
        print(f"{format_values(row[0])}:   {as_bit(row[1])}")  # noqa: T201


if __name__ == "__main__":
    cli()
