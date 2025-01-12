from lark import Lark, Transformer, UnexpectedEOF  # type: ignore

from predicate import always_false_p, always_true_p, ge_p, le_p
from predicate.implies import Implies
from predicate.named_predicate import NamedPredicate
from predicate.predicate import Predicate

grammar = Lark(
    """
    predicate: expression | variable | ge_p | le_p

    ge_p: "ge_p" "(" value ")"
    le_p: "le_p" "(" value ")"

    value: NUMBER
    variable: WORD

    ?expression: grouped_expression | or_expression | and_expression | xor_expression | not_expression
                | implies_expression | false | true

    false: "false"
    true: "true"
    grouped_expression: "(" predicate ")"
    or_expression: predicate "|" predicate
    and_expression: predicate "&" predicate
    xor_expression: predicate "^" predicate
    not_expression: "~" predicate
    implies_expression: predicate "=>" predicate

    %import common.WORD
    %import common.NUMBER
    %ignore " "           // Disregard spaces in text
""",
    start="predicate",
)


class _PredicateTransformer(Transformer):
    def predicate(self, item) -> Predicate:
        return item[0]

    def value(self, item) -> int:
        return int(item[0].value)

    def and_expression(self, items: tuple[Predicate, Predicate]):
        left, right = items
        return left & right

    def false(self, _item) -> Predicate:
        return always_false_p

    def ge_p(self, item) -> Predicate:
        return ge_p(v=item[0])

    def le_p(self, item) -> Predicate:
        return le_p(v=item[0])

    def grouped_expression(self, item):
        return item[0]

    def implies_expression(self, items: tuple[Predicate, Predicate]):
        left, right = items
        return Implies(left=left, right=right)

    def not_expression(self, item: tuple[Predicate]) -> Predicate:
        predicate = item[0]
        return ~predicate

    def or_expression(self, items: tuple[Predicate, Predicate]) -> Predicate:
        left, right = items
        return left | right

    def true(self, _item) -> Predicate:
        return always_true_p

    def variable(self, item) -> Predicate:
        (name,) = item[0]
        return NamedPredicate(name=name)

    def xor_expression(self, items: tuple[Predicate, Predicate]) -> Predicate:
        left, right = items
        return left ^ right

    pass


def parse_expression(expression: str) -> Predicate | None:
    try:
        predicate_tree = grammar.parse(expression)
    except UnexpectedEOF:
        return None

    return _PredicateTransformer().transform(predicate_tree)
