from typing import Any

from predicate.predicate import Explanation, Predicate


def explain(predicate: Predicate[Any], value: Any) -> Explanation:
    return predicate.explain(value)
