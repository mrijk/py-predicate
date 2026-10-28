# Names that only exist for the type checker, used where py-predicate evaluates strings itself
from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple, TypedDict, TypeVar

if TYPE_CHECKING:

    class Hidden: ...


HiddenT = TypeVar("HiddenT", bound="Hidden")


class Config(TypedDict):
    name: str
    hidden: Hidden


class Pair(NamedTuple):
    first: int
    hidden: Hidden


def bound(x: HiddenT) -> int:
    return 0


def bound_type(cls: type[HiddenT]) -> int:
    return 0


def config_name(config: Config) -> str:
    return config["name"]


def pair_first(pair: Pair) -> int:
    return pair.first
