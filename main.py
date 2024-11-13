import click

from predicate import all_p, is_float_p, is_int_p, is_list_p, is_none_p, is_str_p, lazy_p
from predicate.formatter.format_dot import to_dot
from predicate.predicate import NamedPredicate
from predicate.standard_predicates import comp_p, is_dict_p
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

    # str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str")))
    #
    # dot = to_dot(str_or_list_of_str, predicate, show_optimized=optimize)

    _valid_json_p = lazy_p("is_json_p")
    json_list_p = is_list_p & lazy_p("json_values")

    json_keys_p = all_p(is_str_p)

    json_values = all_p(is_str_p | is_int_p | is_float_p | json_list_p | _valid_json_p | is_none_p)
    json_values_p = comp_p(lambda x: x.values(), json_values)

    is_json_p = (is_dict_p & json_keys_p & json_values_p) | json_list_p

    dot = to_dot(is_json_p, repr(is_json_p), show_optimized=optimize)

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
