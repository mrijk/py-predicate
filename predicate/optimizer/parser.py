from functools import partial

from predicate import AlwaysTruePredicate, NotPredicate
from predicate.predicate import AlwaysFalsePredicate, AndPredicate, OrPredicate, Predicate, XorPredicate

# Tokens
FALSE = "false"
TRUE = "true"
NOT = "~"
AND = "&"
OR = "|"
XOR = "^"


def _parse_string(predicate_string: str, stack: list) -> tuple[str, Predicate]:
    def push(item):
        stack.append(item)

    def pop():
        return stack.pop()

    while predicate_string:
        if lookahead_false(predicate_string):
            predicate_string = skip_token(predicate_string, FALSE)
            push(AlwaysFalsePredicate())

        if lookahead_true(predicate_string):
            predicate_string = skip_token(predicate_string, TRUE)
            push(AlwaysTruePredicate())

        if lookahead_not(predicate_string):
            predicate_string = skip_token(predicate_string, NOT)
            predicate_string, predicate = _parse_string(predicate_string, stack)
            push(NotPredicate(predicate=predicate))

        if lookahead_and(predicate_string):
            predicate_string = skip_token(predicate_string, AND)
            predicate_string, right = _parse_string(predicate_string, stack)
            push(AndPredicate(left=pop(), right=right))

        if lookahead_or(predicate_string):
            predicate_string = skip_token(predicate_string, OR)
            predicate_string, right = _parse_string(predicate_string, stack)
            push(OrPredicate(left=pop(), right=right))

        if lookahead_xor(predicate_string):
            predicate_string = skip_token(predicate_string, XOR)
            predicate_string, right = _parse_string(predicate_string, stack)
            push(XorPredicate(left=pop(), right=right))

    return predicate_string, pop()


def parse_string(predicate_string: str) -> Predicate:
    stack: list = []
    _, predicate = _parse_string(predicate_string, stack)

    return predicate


def skip_token(predicate_str: str, token: str) -> str:
    return predicate_str[len(token) :].lstrip(" ")


def lookahead(predicate_str: str, token: str) -> bool:
    return predicate_str.startswith(token)


lookahead_false = partial(lookahead, token=FALSE)
lookahead_true = partial(lookahead, token=TRUE)
lookahead_not = partial(lookahead, token=NOT)
lookahead_and = partial(lookahead, token=AND)
lookahead_or = partial(lookahead, token=OR)
lookahead_xor = partial(lookahead, token=XOR)
