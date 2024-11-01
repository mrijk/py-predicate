from dataclasses import dataclass

from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    Predicate,
    always_false_p,
    always_true_p,
)


@dataclass
class WildcardPredicate[T](Predicate[T]):
    def __call__(self, *args, **kwargs) -> bool:
        return False


p = AlwaysTruePredicate()
q = AlwaysFalsePredicate()

optimization_rules = [
    {"title": "Double not", "from": ~~p, "to": p},
    {
        "title": "Not true is false",
        "from": ~always_true_p,
        "to": always_false_p,
    },
    {"title": "Not false is true", "from": ~always_false_p, "to": always_true_p},
    {
        "title": "False or False is False",
        "from": always_false_p | always_false_p,
        "to": always_false_p,
    },
    {
        "title": "False or True is True",
        "from": always_false_p | always_true_p,
        "to": always_true_p,
    },
    {
        "title": "True or False is True",
        "from": always_true_p | always_false_p,
        "to": always_true_p,
    },
    {
        "title": "True or True is True",
        "from": always_true_p | always_true_p,
        "to": always_true_p,
    },
    {
        "title": "False and True is False",
        "from": always_false_p & always_true_p,
        "to": always_false_p,
    },
    {
        "title": "True and True is True",
        "from": always_true_p | always_true_p,
        "to": always_true_p,
    },
    {
        "title": "p and False is False",
        "from": WildcardPredicate() & always_false_p,
        "to": always_false_p,
    },
    {
        "title": "p & true = true",
        "from": WildcardPredicate() & always_true_p,
        "to": always_true_p,
    },
]
