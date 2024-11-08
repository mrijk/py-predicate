import click

from predicate.formatter.format_dot import to_dot
from predicate.standard_predicates import fn_p, ge_p


@click.command()
@click.option("-f", "--filename", help="Output file")
@click.option("-o", "--optimize", is_flag=True, help="Optimize predicate")
@click.option("-p", "--predicate", required=True, help="Predicate to parse")
def cli(predicate: str, filename, optimize: bool) -> None:
    # predicate_string = "true | false & true ^ ~false"

    # predicate_string = "x in {2, 3, 4} | x not in {4, 5}"

    # parsed = parse_string(predicate)

    p1 = ge_p(2)
    # p3 = lt_p(2)
    # p2 = le_p(3)
    #
    # parsed = p1 | p2 | p3

    parsed = p1 & fn_p(lambda x: x)

    dot = to_dot(parsed, predicate, show_optimized=optimize)

    dot.render("/tmp/predicate.gv", view=True)  # noqa: S108

    # print(json.dumps(to_json(predicate)))


if __name__ == "__main__":
    cli()
