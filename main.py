import click

from predicate import FnPredicate
from predicate.formatter.format_dot import to_dot
from predicate.standard_predicates import fn_p


@click.command()
@click.option("-f", "--filename", help="Output file")
@click.option("-o", "--optimize", is_flag=True, help="Optimize predicate")
@click.option("-p", "--predicate", required=True, help="Predicate to parse")
def cli(predicate: str, filename, optimize: bool) -> None:
    # predicate_string = "true | false & true ^ ~false"

    # predicate_string = "x in {2, 3, 4} | x not in {4, 5}"

    # parsed = parse_string(predicate)

    p: FnPredicate = fn_p(lambda x: x > 2)
    q: FnPredicate = fn_p(lambda x: x > 3)
    r: FnPredicate = fn_p(lambda x: x > 4)

    parsed = p | (q | r | ~p)

    dot = to_dot(parsed, predicate, show_optimized=optimize)

    dot.render("/tmp/predicate.gv", view=True)  # noqa: S108

    # print(json.dumps(to_json(predicate)))


if __name__ == "__main__":
    cli()
