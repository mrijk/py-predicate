from typing import Any, Iterable

from predicate.helpers import join_as_str


def set_to_str(v: Iterable[Any]) -> str:
    return f"{{{join_as_str(v)}}}"
