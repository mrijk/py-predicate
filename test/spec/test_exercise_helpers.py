import collections
import collections.abc
import io
import sys
import tempfile
from collections.abc import Callable
from typing import (
    IO,
    AbstractSet,
    Annotated,
    Any,
    BinaryIO,
    LiteralString,
    NamedTuple,
    Never,
    NewType,
    NoReturn,
    NotRequired,
    Required,
    TextIO,
    Tuple,
    TypedDict,
    TypeVar,
    Unpack,
)

import pytest
import typing_extensions
from more_itertools import take

from predicate import (
    always_true_p,
    exercise,
    generate_false,
    generate_true,
    is_instance_p,
    is_int_p,
    is_str_p,
    is_struct_p,
)
from predicate.spec.exercise_helpers import annotation_to_predicate
from predicate.spec.instrument import instrument, instrument_function
from predicate.spec.spec import SpecViolationError
from spec.test_functions.typed_dicts_postponed import Options


def test_annotation_to_predicate_set():
    predicate = annotation_to_predicate(set[int])

    assert predicate({1, 2, 3}) is True
    assert predicate({"a", "b"}) is False
    assert predicate([1, 2, 3]) is False


def test_annotation_to_predicate_dict():
    predicate = annotation_to_predicate(dict[str, int])

    assert predicate({})
    assert predicate({"a": 1})
    assert not predicate({"a": "b"})
    assert not predicate([])


def test_annotation_to_predicate_frozenset():
    predicate = annotation_to_predicate(frozenset[int])

    assert predicate(frozenset({1, 2, 3})) is True
    assert predicate(frozenset({"a", "b"})) is False
    assert predicate({1, 2, 3}) is False


if sys.version_info >= (3, 15):

    def test_annotation_to_predicate_frozendict():
        predicate = annotation_to_predicate(frozendict[str, int])  # noqa: F821

        assert predicate(frozendict({"a": 1})) is True  # noqa: F821
        assert predicate(frozendict({"a": "b"})) is False  # noqa: F821
        assert predicate({"a": 1}) is False


@pytest.mark.parametrize("annotation", [Never, NoReturn])
def test_annotation_to_predicate_never(annotation):
    predicate = annotation_to_predicate(annotation)

    assert predicate(None) is False
    assert predicate(1) is False


def test_get_return_spec_uses_annotation():
    from predicate.spec.exercise_helpers import get_return_spec

    def f() -> list[int]:
        return [1]

    def g() -> NoReturn:
        raise ValueError

    ret = get_return_spec(f, {"args": {}})["ret"]
    assert ret([1, 2]) is True
    assert ret(["a"]) is False

    assert get_return_spec(g, {"args": {}})["ret"](None) is False


def test_annotation_to_predicate_literal_string():
    predicate = annotation_to_predicate(LiteralString)

    assert predicate("abc") is True
    assert predicate(1) is False


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (float, 1, True),
        (float, 1.5, True),
        (float, "1", False),
        (complex, 1, True),
        (complex, 1.5, True),
        (complex, 1j, True),
        (int, 1.5, False),
    ],
)
def test_annotation_to_predicate_numeric_tower(annotation, value, expected):
    assert annotation_to_predicate(annotation)(value) is expected


def test_annotation_to_predicate_union_of_three():
    predicate = annotation_to_predicate(int | str | None)

    assert predicate(1) is True
    assert predicate("a") is True
    assert predicate(None) is True
    assert predicate(1.5) is False


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (tuple[int, ...], (), True),
        (tuple[int, ...], (1, 2, 3), True),
        (tuple[int, ...], (1, "x"), False),
        (tuple[int, ...], [1, 2], False),
        (Tuple[str, ...], ("a",), True),
        (Tuple[str, ...], (1,), False),
        (tuple[()], (), True),
        (tuple[()], (1,), False),
        (tuple[()], [], False),
        (Tuple[()], (), True),
        (Tuple[()], (1,), False),
        (Tuple, (1, "x"), True),
        (tuple[int, str], (1, "x"), True),
        (tuple[int, str], (1, 2), False),
    ],
)
def test_annotation_to_predicate_tuple(annotation, value, expected):
    assert annotation_to_predicate(annotation)(value) is expected


@pytest.mark.parametrize("annotation", [tuple[int, ...], tuple[()]])
def test_annotation_to_predicate_tuple_generators(annotation):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


@pytest.mark.parametrize(
    ("annotation", "value", "expected"),
    [
        (collections.abc.Sequence[int], [1, 2], True),
        (collections.abc.Sequence[int], (1, 2), True),
        (collections.abc.Sequence[int], [], True),
        (collections.abc.Sequence[int], [1, "x"], False),
        (collections.abc.Sequence[int], {1, 2}, False),
        (collections.abc.MutableSequence[int], (1, 2), False),
        (collections.abc.Collection[int], {1, 2}, True),
        (collections.abc.Collection[int], {"x"}, False),
        (collections.abc.Set[int], frozenset({1}), True),
        (collections.abc.Set[int], {"x"}, False),
        (AbstractSet[int], {1}, True),
        (collections.abc.MutableSet[int], frozenset({1}), False),
        (collections.abc.Mapping[str, int], {}, True),
        (collections.abc.Mapping[str, int], {"a": 1}, True),
        (collections.abc.Mapping[str, int], {"a": "b"}, False),
        (collections.abc.Mapping[str, int], [("a", 1)], False),
        (collections.abc.MutableMapping[str, int], {"a": 1}, True),
        (collections.abc.Sequence, ["x"], True),
        (collections.abc.Reversible[int], [1, 2], True),
        (collections.abc.Reversible[int], [1, "x"], False),
        (collections.abc.Reversible[int], {1, 2}, False),
    ],
)
def test_annotation_to_predicate_abc_generics(annotation, value, expected):
    assert annotation_to_predicate(annotation)(value) is expected


@pytest.mark.parametrize(
    "annotation",
    [
        collections.abc.Sequence[int],
        collections.abc.Sequence[str],
        collections.abc.MutableSequence[int],
        collections.abc.Collection[int],
        collections.abc.Set[str],
        collections.abc.MutableSet[int],
        collections.abc.Mapping[int, str],
        collections.abc.MutableMapping[str, int],
        collections.abc.Sequence[collections.abc.Sequence[int]],
        collections.abc.Reversible[int],
    ],
)
def test_annotation_to_predicate_abc_generators(annotation):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


def test_exercise_variadic_tuple():
    def total(values: tuple[int, ...]) -> int:
        return sum(values)

    assert take(5, exercise(total))


def test_exercise_reversible():
    def last(values: collections.abc.Reversible[int]) -> int | None:
        return next(reversed(values), None)  # type: ignore[call-overload]

    assert take(5, exercise(last))


def test_exercise_abc_generics():
    def count(values: collections.abc.Sequence[str], lookup: collections.abc.Mapping[str, int]) -> int:
        return sum(lookup.get(value, 0) for value in values)

    assert take(5, exercise(count))


@pytest.mark.parametrize(
    ("annotation", "item_check"),
    [
        (collections.abc.Iterable[str], lambda item: isinstance(item, str)),
        (collections.abc.Iterable[tuple[str, int]], lambda item: isinstance(item, tuple) and isinstance(item[0], str)),
    ],
)
def test_generate_iterable_items_have_the_item_type(annotation, item_check):
    # #372: Iterable[X] generated items of any type, e.g. ints for Iterable[str]
    values = take(10, generate_true(annotation_to_predicate(annotation)))

    assert all(item_check(item) for value in values for item in value)
    assert any(values)


def test_exercise_iterable_of_str():
    def shout(words: collections.abc.Iterable[str]) -> str:
        return " ".join(word.upper() for word in words)

    assert len(take(5, exercise(shout))) == 5


def test_annotation_to_predicate_iterable_doesnt_consume_iterators():
    # Checking the items would use up an iterator argument before the function gets it
    values = iter([1, 2, 3])

    assert annotation_to_predicate(collections.abc.Iterable[int])(values)
    assert list(values) == [1, 2, 3]


def test_annotation_to_predicate_object():
    predicate = annotation_to_predicate(object)

    assert predicate(None)
    assert predicate(1)
    assert predicate(object())


def test_exercise_object_parameter():
    def describe(x: object) -> str:
        return type(x).__name__

    assert take(5, exercise(describe))


T = TypeVar("T")
BoundT = TypeVar("BoundT", bound=int)
ConstrainedT = TypeVar("ConstrainedT", int, str)
ForwardBoundT = TypeVar("ForwardBoundT", bound="io.BytesIO")


@pytest.mark.parametrize(
    "annotation, accepted, rejected",
    [
        (type[T], [int, str, object], [3, "a"]),
        (type[BoundT], [int, bool], [str, 3]),
        (type[ConstrainedT], [int, bool, str], [float, 3]),
        (type[ForwardBoundT], [io.BytesIO], [io.StringIO, 3]),
        (type[None], [type(None)], [int, None]),
        (type[int | str], [int, bool, str], [float, 3]),
        (type[Any], [int, object], [3]),
        (type[list[int]], [list], [tuple, [1]]),
    ],
)
def test_annotation_to_predicate_type_of_type_var(annotation, accepted, rejected):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in accepted)
    assert not any(predicate(value) for value in rejected)
    assert all(predicate(value) for value in take(20, generate_true(predicate)))


def test_exercise_type_of_type_var():
    def name(cls: type[BoundT]) -> str:
        assert issubclass(cls, int)
        return cls.__name__

    assert len(list(exercise(name, n=5))) == 5


@pytest.mark.parametrize(
    "annotation, accepted, rejected",
    [
        (IO[bytes], [io.BytesIO(), tempfile.SpooledTemporaryFile()], [io.StringIO(), b"x"]),
        (BinaryIO, [io.BytesIO()], [io.StringIO()]),
        (IO[str], [io.StringIO()], [io.BytesIO(), "x"]),
        (TextIO, [io.StringIO()], [io.BytesIO()]),
        (IO, [io.BytesIO(), io.StringIO()], ["x"]),
        (IO[Any], [io.BytesIO(), io.StringIO()], [b"x"]),
    ],
)
def test_annotation_to_predicate_io(annotation, accepted, rejected):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in accepted)
    assert not any(predicate(value) for value in rejected)
    assert all(predicate(value) for value in take(10, generate_true(predicate)))


def test_exercise_io():
    def read_all(stream: IO[bytes]) -> IO[bytes]:
        stream.read()
        return stream

    assert len(list(exercise(read_all, n=5))) == 5


def _item_types(value):
    return {type(item) for item in (value.values() if isinstance(value, dict) else value)}


@pytest.mark.parametrize(
    "annotation",
    [list[T], collections.abc.Iterable[T], set[T], dict[str, T], list[ConstrainedT], list[BoundT]],  # type: ignore[valid-type]
)
def test_generate_type_var_collection_items_share_one_type(annotation):
    # #375: a type variable is one type per call, and a mixed list can't be sorted
    values = take(100, generate_true(annotation_to_predicate(annotation)))

    assert all(len(_item_types(value)) <= 1 for value in values)


def test_generate_constrained_type_var_uses_each_constraint():
    values = take(100, generate_true(annotation_to_predicate(list[ConstrainedT])))

    assert set().union(*(_item_types(value) for value in values)) == {int, str}


def test_type_var_predicates_equal_the_checking_predicates():
    # Only generation differs: checking, repr and equality stay as they were
    assert annotation_to_predicate(T) == always_true_p
    assert repr(annotation_to_predicate(T)) == "always_true_p"
    assert annotation_to_predicate(ConstrainedT) == is_int_p | is_str_p
    assert repr(annotation_to_predicate(ConstrainedT)) == "is_int_p | is_str_p"


def test_exercise_sort_of_type_var():
    def smallest(values: collections.abc.Iterable[T]) -> list[T]:
        return sorted(values)[:1]  # type: ignore[type-var]  # a free T, as in natsort's natsorted

    assert len(take(10, exercise(smallest, n=10))) == 10


CallableT = TypeVar("CallableT", bound=Callable[..., Any])
StringBoundT = TypeVar("StringBoundT", bound="int")
NamedTupleT = TypeVar("NamedTupleT", bound=NamedTuple)


@pytest.mark.parametrize(
    "annotation, accepted, rejected",
    [
        (T, [1, "a", None], []),
        (BoundT, [1, -5], ["a", 1.5]),
        (ConstrainedT, [1, "a"], [1.5, None]),
        (StringBoundT, [1], ["a"]),
        (CallableT, [len, lambda: 0], [1, "a"]),
    ],
)
def test_annotation_to_predicate_type_var(annotation, accepted, rejected):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in accepted)
    assert not any(predicate(value) for value in rejected)
    assert all(predicate(value) for value in take(20, generate_true(predicate)))


def test_exercise_type_var_bound():
    def decorate(f: CallableT) -> CallableT:
        assert callable(f)
        return f

    assert len(list(exercise(decorate, n=5))) == 5


class Point(NamedTuple):
    x: int
    y: int


class Movie(TypedDict):
    title: str


class ExtensionsMovie(typing_extensions.TypedDict):
    title: str


@pytest.mark.parametrize(
    "annotation, accepted, rejected",
    [
        (type[NamedTuple], [Point, collections.namedtuple("P", "a b")], [tuple, Point(1, 2), dict]),
        (type[NamedTupleT], [Point], [tuple]),
        (type[TypedDict], [Movie, ExtensionsMovie], [dict, {"title": "x"}]),
        (type[typing_extensions.TypedDict], [Movie, ExtensionsMovie], [dict]),
    ],
)
def test_annotation_to_predicate_type_of_named_tuple_and_typed_dict(annotation, accepted, rejected):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in accepted)
    assert not any(predicate(value) for value in rejected)
    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert all(predicate(value) for value in take(10, generate_true(is_instance_p(annotation))))


def test_exercise_type_of_named_tuple():
    def fields(cls: type[NamedTuple]) -> tuple[str, ...]:
        return cls._fields

    assert len(list(exercise(fields, n=5))) == 5


class Config(TypedDict):
    name: str
    debug: bool


class PartialConfig(TypedDict, total=False):
    level: int
    tag: Required[str]


class Tree(TypedDict):
    value: int
    children: list["Tree"]


@pytest.mark.parametrize(
    "annotation, accepted, rejected",
    [
        (
            Config,
            [{"name": "x", "debug": False}],
            [{"name": "x"}, {"name": 1, "debug": False}, {"name": "x", "debug": True, "extra": 1}, None],
        ),
        (PartialConfig, [{"tag": "a"}, {"tag": "a", "level": 1}], [{}, {"level": 1}, {"tag": "a", "level": "x"}]),
        (
            Tree,
            [{"value": 1, "children": []}, {"value": 1, "children": [{"value": 2, "children": []}]}],
            [{"value": 1}],
        ),
        (Options, [{"name": "x"}, {"name": "x", "verbose": True}], [{"verbose": True}, {"name": "x", "verbose": 1}]),
        (Config | None, [None, {"name": "x", "debug": True}], [{}]),
    ],
)
def test_annotation_to_predicate_typed_dict(annotation, accepted, rejected):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in accepted)
    assert not any(predicate(value) for value in rejected)
    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


def test_exercise_typed_dict_argument_and_return():
    def rename(config: Config, name: str) -> Config:
        return config | {"name": name}

    assert len(list(exercise(rename, n=5))) == 5


def test_instrument_typed_dict_return():
    @instrument
    def make() -> Config:
        return {"name": "x", "debug": False}

    assert make() == {"name": "x", "debug": False}


def test_exercise_spec_annotated_function():
    def double(x: int) -> int:
        return x * 2

    instrumented = instrument_function(exercise, {"args": {}})

    assert len(list(instrumented(double, {"args": {}}))) > 0


UserId = NewType("UserId", int)
AdminId = NewType("AdminId", UserId)
type IntList = list[int]
type StrDict[V] = dict[str, V]


@pytest.mark.parametrize(
    "annotation, accepted, rejected",
    [
        (UserId, [1, -5], ["1", 1.5]),
        (AdminId, [1], ["1"]),
        (list[UserId], [[1, 2], []], [["a"]]),
        (UserId | None, [1, None], ["1"]),
        (Annotated[int, "metadata"], [1], ["1"]),
        (Annotated[IntList, "metadata"], [[1]], [["a"]]),
        (IntList, [[1, 2], []], [["a"], (1,)]),
        (StrDict[float], [{"a": 1.5}, {}], [{"a": "x"}, {1: 1.5}]),
    ],
)
def test_annotation_to_predicate_aliases(annotation, accepted, rejected):
    predicate = annotation_to_predicate(annotation)

    assert all(predicate(value) for value in accepted)
    assert not any(predicate(value) for value in rejected)
    assert all(predicate(value) for value in take(10, generate_true(predicate)))
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


def test_exercise_new_type_return():
    def normalize(name: str) -> UserId:
        return UserId(len(name))

    assert len(list(exercise(normalize, n=5))) == 5


@pytest.mark.parametrize(
    "annotation, item_p",
    [
        (collections.abc.Iterator[int], lambda item: isinstance(item, int)),
        (collections.abc.Generator[str, None, None], lambda item: isinstance(item, str)),
        (collections.abc.Iterator, lambda item: True),
    ],
)
def test_generate_iterators(annotation, item_p):
    predicate = annotation_to_predicate(annotation)
    values = take(10, generate_true(predicate))

    assert all(predicate(value) for value in values)
    assert all(item_p(item) for value in values for item in value)
    assert not any(predicate(value) for value in take(10, generate_false(predicate)))


def test_exercise_iterator_argument():
    def total(numbers: collections.abc.Iterator[int]) -> int:
        return sum(numbers)

    assert len(list(exercise(total, n=5))) == 5


class ParserOptions(TypedDict, total=False):
    max_errors: int
    level: str


class NamedOptions(TypedDict):
    name: str
    debug: NotRequired[bool]


def test_exercise_unpack_typed_dict_kwargs():
    calls = []

    def parse(sql: str, **opts: Unpack[ParserOptions]) -> str:
        calls.append(opts)
        return sql

    assert len(list(exercise(parse, n=10))) == 10
    assert all(set(opts) <= {"max_errors", "level"} for opts in calls)
    assert all(isinstance(opts.get("max_errors", 0), int) for opts in calls)
    assert all(isinstance(opts.get("level", ""), str) for opts in calls)


def test_exercise_unpack_typed_dict_required_key():
    def describe(**opts: Unpack[NamedOptions]) -> str:
        return opts["name"]

    assert len(list(exercise(describe, n=5))) == 5


def test_instrument_unpack_typed_dict_kwargs():
    @instrument
    def parse(**opts: Unpack[ParserOptions]) -> int:
        return len(opts)

    assert parse(max_errors=3) == 1
    with pytest.raises(SpecViolationError, match="parameter 'opts'"):
        parse(max_errors="three")
    with pytest.raises(SpecViolationError, match="parameter 'opts'"):
        parse(unknown=1)


def test_generate_struct_without_required_keys():
    predicate = is_struct_p(optional={"n": is_int_p})

    values = take(20, generate_true(predicate))

    assert len(values) == 20
    assert all(predicate(value) for value in values)
