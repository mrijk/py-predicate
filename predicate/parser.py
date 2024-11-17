from lark import Lark, Transformer, UnexpectedEOF

from predicate import NotPredicate, Predicate, XorPredicate, always_false_p
from predicate.predicate import AndPredicate, NamedPredicate, OrPredicate, always_true_p

grammar = Lark(
    """
    predicate: expression | variable

    variable: WORD
    ?expression: grouped_expression | or_expression | and_expression | xor_expression | not_expression | false | true

    false: "false"
    true: "true"
    grouped_expression: "(" predicate ")"
    or_expression: predicate "|" predicate
    and_expression: predicate "&" predicate
    xor_expression: predicate "^" predicate
    not_expression: "~" predicate

    %import common.WORD   // imports from terminal library
    %ignore " "           // Disregard spaces in text
""",
    start="predicate",
)


class _PredicateTransformer(Transformer):
    def predicate(self, item) -> Predicate:
        return item[0]

    def and_expression(self, items):
        left, right = items
        return AndPredicate(left=left, right=right)

    def false(self, _item) -> Predicate:
        return always_false_p

    def grouped_expression(self, item):
        return item[0]

    def not_expression(self, item) -> Predicate:
        return NotPredicate(predicate=item[0])

    def or_expression(self, items) -> Predicate:
        left, right = items
        return OrPredicate(left=left, right=right)

    def true(self, _item) -> Predicate:
        return always_true_p

    def variable(self, item) -> Predicate:
        (name,) = item[0]
        return NamedPredicate(name=name)

    def xor_expression(self, items) -> Predicate:
        left, right = items
        return XorPredicate(left=left, right=right)

    pass


def parse_expression(expression: str) -> Predicate | None:
    try:
        predicate_tree = grammar.parse(expression)
    except UnexpectedEOF:
        return None

    return _PredicateTransformer().transform(predicate_tree)
