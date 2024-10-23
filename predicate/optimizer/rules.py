from predicate.helpers import const
from predicate.predicate import Predicate, always_true_p, always_false_p

p = Predicate(predicate_fn=const(True))
q = Predicate(predicate_fn=const(True))

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
]
