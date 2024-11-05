import click

from predicate.formatter.format_dot import to_dot
from predicate.standard_predicates import ge_p, lt_p, le_p


@click.command()
@click.option("-f", "--filename", help="Output file")
@click.option("-o", "--optimize", is_flag=True, help="Optimize predicate")
@click.option("-p", "--predicate", required=True, help="Predicate to parse")
def cli(predicate: str, filename, optimize: bool) -> None:
    # predicate_string = "true | false & true ^ ~false"

    # predicate_string = "x in {2, 3, 4} | x not in {4, 5}"

    # parsed = parse_string(predicate)

    ge_2 = ge_p(2)
    lt_2 = ~ge_2

    # parsed = ge_2 & lt_2

    p1 = ge_p(2)
    p3 = lt_p(2)
    p2 = le_p(3)

    parsed = p1 | p2 | p3

    dot = to_dot(parsed, predicate, show_optimized=optimize)

    dot.render("/tmp/predicate.gv", view=True)  # noqa [S108]

    # print(json.dumps(to_json(predicate)))


if __name__ == "__main__":
    cli()
