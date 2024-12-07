from typing import Any

from predicate.predicate import Predicate


def explain(predicate: Predicate, value: Any) -> dict:
    return predicate.explain(value)
