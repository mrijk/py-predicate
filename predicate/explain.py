from typing import Any

from predicate.predicate import Predicate


def explain(predicate: Predicate[Any], value: Any) -> dict[str, Any]:
    return predicate.explain(value)
