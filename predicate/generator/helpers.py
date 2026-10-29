import ast
import asyncio
import atexit
import io
import ipaddress
import logging
import math
import random
import re
import string
import sys
import types
from collections import namedtuple
from collections.abc import Callable, Iterable
from datetime import date, datetime, time, timedelta, timezone, tzinfo
from decimal import Decimal
from enum import Enum, Flag
from fractions import Fraction
from functools import cache, reduce, wraps
from inspect import Parameter, Signature, signature
from itertools import chain, count, cycle
from operator import or_
from pathlib import PurePath
from random import choices
from time import gmtime, struct_time
from typing import Any, Final, ForwardRef, Iterator
from uuid import UUID, uuid4

from more_itertools import interleave, random_permutation, repeatfunc, take, unique_everseen

from predicate.eq_predicate import eq_p
from predicate.generator.generate_predicate import generate_predicate, typed_predicate_type_registry
from predicate.predicate import Predicate
from predicate.range_predicate import ge_le_p
from predicate.regex_predicate import regex_p
from predicate.standard_predicates import is_int_p, is_str_p


def random_first_from_iterables(*iterables: Iterable) -> Iterator[Any]:
    remaining = [it for it in iterables if it]

    # An iterable that runs out is dropped, instead of being picked (and failing) forever
    while remaining:
        chosen_iterable = random.choice(remaining)
        try:
            yield next(iter(chosen_iterable))
        except StopIteration:
            remaining.remove(chosen_iterable)


def set_from_list(value: list[Any], order: bool = False) -> Iterator[set[Any]]:
    length = len(value)
    try:
        if len(result := set(value)) == length:
            yield result if order else set(random_permutation(result))
    except TypeError:
        pass


def random_complex_numbers(radius: float = 1e6) -> Iterator[complex]:
    valid_amplitudes = random_floats(lower=0.0, upper=radius)
    valid_angles = random_floats(lower=0.0, upper=2 * math.pi)

    def to_complex(amplitude: float, angle: float) -> complex:
        return complex(real=amplitude * math.cos(angle), imag=amplitude * math.sin(angle))

    yield from (to_complex(amplitude, angle) for amplitude, angle in zip(valid_amplitudes, valid_angles, strict=False))


def random_callables() -> Iterator[Callable]:
    yield from random_first_from_iterables(random_lambdas(), random_functions(), random_callable_objects())


def generate_lambda(arg_names: list[str]) -> types.FunctionType:
    # Start from a compiled "return 0" so the bytecode is always valid for the running Python version
    code = (lambda: 0).__code__.replace(
        co_argcount=len(arg_names),
        co_nlocals=len(arg_names),
        co_varnames=tuple(arg_names),
        co_filename="<generated>",
    )
    return types.FunctionType(code, {})


default_nr_of_parameters_p: Final = eq_p(1)


def random_lambdas(nr_of_parameters_p: Predicate = default_nr_of_parameters_p) -> Iterator[types.FunctionType]:
    value_p = regex_p("[a-z]{2,3}")
    valid_parameter_lists = random_lists(length_p=nr_of_parameters_p, value_p=value_p)
    yield from (generate_lambda(list(arg_names)) for arg_names in valid_parameter_lists)


default_size_p: Final = ge_le_p(lower=0, upper=5)


def random_signatures(nr_of_parameters_p: Predicate = default_size_p) -> Iterator[Signature]:
    value_p = regex_p("[a-z]{2,3}")
    valid_parameter_lists = random_lists(length_p=nr_of_parameters_p, value_p=value_p)

    def to_signature(names: list[str]) -> Signature:
        return Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in unique_everseen(names)])

    yield from (to_signature(names) for names in valid_parameter_lists)


def random_parameters() -> Iterator[Parameter]:
    kinds = [
        Parameter.POSITIONAL_ONLY,
        Parameter.POSITIONAL_OR_KEYWORD,
        Parameter.VAR_POSITIONAL,
        Parameter.KEYWORD_ONLY,
        Parameter.VAR_KEYWORD,
    ]
    annotations = [Parameter.empty, int, str, Any]
    while True:
        yield Parameter(
            random.choice(["a", "b", "x", "value", "items"]),
            random.choice(kinds),
            annotation=random.choice(annotations),
        )


def random_functions(nr_of_parameters_p: Predicate = default_size_p) -> Iterator[Callable]:
    yield from (function_with_signature(sig) for sig in random_signatures(nr_of_parameters_p))


def random_callable_objects(nr_of_parameters_p: Predicate = default_size_p) -> Iterator[Callable]:
    yield from (callable_object_with_signature(sig) for sig in random_signatures(nr_of_parameters_p))


def random_lengths(length_p: Predicate) -> Iterator[int]:
    """Return collection lengths: 0 (the empty collection) at most once and first, then only positive lengths (#356).

    The empty collection is a valuable edge case, but exercise with a small n only sees the start of the stream.
    """
    from predicate import generate_true

    if length_p(0):
        yield 0
    lengths = generate_true(length_p)
    # ponytail: a length_p without a positive length in 100 draws (e.g. eq_p(0)) is taken to allow only 0
    head = take(100, lengths)
    positive = any(n > 0 for n in head)
    yield from (n for n in chain(head, lengths) if (n > 0 if positive else n >= 0))


def random_dicts(
    key_p: Predicate = is_str_p, value_p: Predicate = is_int_p, size_p: Predicate = default_size_p
) -> Iterator[dict[Any, Any]]:
    from predicate import generate_true

    valid_keys = generate_true(key_p)
    valid_values = generate_true(value_p)
    valid_sizes = random_lengths(size_p)

    yield from (dict(zip(take(s, unique_everseen(valid_keys)), valid_values, strict=False)) for s in valid_sizes)


if sys.version_info >= (3, 15):

    def random_frozendicts(
        key_p: Predicate = is_str_p, value_p: Predicate = is_int_p, size_p: Predicate = default_size_p
    ) -> Iterator[frozendict[Any, Any]]:  # noqa: F821
        yield from (
            frozendict(random_dict)  # noqa: F821
            for random_dict in random_dicts(key_p=key_p, value_p=value_p, size_p=size_p)
        )

    def random_sentinels() -> Iterator[sentinel]:  # noqa: F821
        yield from (sentinel(name) for name in random_strings(min_size=1))  # noqa: F821


if sys.version_info >= (3, 14):
    from string.templatelib import Template

    def random_templates() -> Iterator[Template]:
        yield from (Template(s) for s in random_strings())


def random_datetimes(lower: datetime | None = None, upper: datetime | None = None) -> Iterator[datetime]:
    start = lower if lower else datetime(year=1980, month=1, day=1)
    end = upper if upper else datetime(year=2050, month=1, day=1)

    now = datetime.now()

    if start <= now <= end:
        yield now

    while True:
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        yield start + timedelta(seconds=random_second)


def random_predicates(*, max_depth: int = 10, klass: type = int) -> Iterator[Predicate]:
    subclasses = [subclass for subclass in Predicate.__subclasses__() if subclass in typed_predicate_type_registry()]

    iterables = [generate_predicate(subclass, max_depth=max_depth, klass=klass) for subclass in subclasses]  # type: ignore

    yield from random_first_from_iterables(*iterables)


default_length_p: Final = ge_le_p(lower=0, upper=10)


def random_sets(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[set[Any]]:
    from predicate import generate_true

    for length in random_lengths(length_p):
        values = take(length, generate_true(value_p))
        if len(result := set(values)) == length:
            yield result


def random_frozensets(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[frozenset]:
    yield from (frozenset(random_set) for random_set in random_sets(length_p=length_p, value_p=value_p))


def random_bools() -> Iterator[bool]:
    yield from (False, True)
    yield from repeatfunc(random.choice, None, (False, True))


def random_containers() -> Iterator[list[Any] | dict[Any, Any]]:
    yield from cycle(([], {}))


def random_hashables() -> Iterator[Any]:
    yield from interleave(
        random_bools(), random_ints(), random_strings(), random_floats(), random_datetimes(), random_uuids()
    )


def random_non_hashables() -> Iterator[Any]:
    yield from interleave(random_lists(), random_dicts())


def random_strings(min_size: int = 0, max_size: int = 10) -> Iterator[str]:
    population = string.ascii_letters + string.digits
    while True:
        length = random.randint(min_size, max_size)
        yield "".join(choices(population, k=length))


def random_floats(lower: float = -1e-6, upper: float = 1e6) -> Iterator[float]:
    def between(limit: float) -> Iterator[float]:
        low = max(-limit, lower)
        high = min(limit, upper)
        if high >= low:
            yield from (random.uniform(low, high) for _ in range(0, int(limit)))

    while True:
        yield from between(1.0)
        yield from between(10.0)
        yield from between(100.0)


def random_ints(lower: int = -sys.maxsize, upper: int = sys.maxsize, **_kwargs: Any) -> Iterator[int]:
    def between(limit: int) -> Iterator[int]:
        low = max(-limit, lower)
        high = min(limit, upper)
        if high >= low:
            yield from (random.randint(low, high) for _ in range(0, limit))

    if lower <= 0 <= upper:
        yield 0

    while True:
        yield from between(1)
        yield from between(10)
        yield from between(100)


def random_iterables(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[Iterable]:
    # A list or a tuple of each length, so the empty one comes once instead of once per kind
    yield from (random.choice((list, tuple))(values) for values in random_lists(length_p=length_p, value_p=value_p))


def random_lists(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[list[Any]]:
    from predicate import generate_true

    yield from (take(n, generate_true(value_p)) for n in random_lengths(length_p))


def random_tuples(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[tuple[Any, ...]]:
    yield from (tuple(random_list) for random_list in random_lists(length_p=length_p, value_p=value_p))


def random_modules() -> Iterator[types.ModuleType]:
    # ponytail: only modules that are already imported, so generating never triggers an import
    modules = [module for module in sys.modules.values() if isinstance(module, types.ModuleType)]
    while True:
        yield random.choice(modules)


def random_uuids() -> Iterator[UUID]:
    yield from repeatfunc(uuid4)


def random_anys() -> Iterator[Any]:
    yield from interleave(random_bools(), random_ints(), random_strings(), random_floats(), random_datetimes())


def random_named_tuples() -> Iterator[tuple]:
    # ponytail: every value gets a fresh namedtuple class; cache classes if that turns out to be slow
    field_names = random_lists(length_p=ge_le_p(lower=0, upper=4), value_p=regex_p("[a-z]{2,4}"))
    for names in field_names:
        klass = namedtuple("RandomNamedTuple", unique_everseen(names))  # type: ignore[misc]  # noqa: PYI024
        yield klass(*take(len(klass._fields), random_anys()))


def random_named_tuple_instances(klass: type) -> Iterator[tuple]:
    from predicate import generate_true
    from predicate.spec.exercise_helpers import annotation_to_predicate, class_hints

    # Fields without an annotation (collections.namedtuple) accept any value
    hints = class_hints(klass)
    generators = [generate_true(annotation_to_predicate(hints.get(field, Any))) for field in klass._fields]  # type: ignore[attr-defined]
    while True:
        yield klass(*(next(generator) for generator in generators))


def random_values_of_type(klass: type) -> Iterator[Any]:
    type_registry: dict[type, Callable[[], Iterator]] = {
        bool: random_bools,
        datetime: random_datetimes,
        int: random_ints,
        float: random_floats,
        str: random_strings,
    }

    if generator := type_registry.get(klass):
        yield from generator()
    elif klass == Any:
        yield from random_anys()
    else:
        raise ValueError(f"No generator found for {klass}")


def random_constrained_values_of_type(klass: type) -> Iterator[Any]:
    type_registry: dict[type, Callable[[], Iterator]] = {
        int: random_ints,
        float: random_floats,
        str: random_strings,
    }

    if generator := type_registry.get(klass):
        yield from generator()
    else:
        yield from []
        # raise ValueError(f"No generator found for {klass}")


def random_constrained_pairs_of_type(klass: type) -> Iterator[tuple[Any, Any]]:
    def ordered_tuple(x: Any, y: Any) -> tuple[Any, Any]:
        return (x, y) if x <= y else (y, x)

    values_1 = random_constrained_values_of_type(klass)
    values_2 = random_constrained_values_of_type(klass)
    values = zip(values_1, values_2, strict=False)

    yield from (ordered_tuple(x, y) for x, y in values)


def sample_optional_fields(optional: dict[str, Any], generators: dict[str, Iterator[Any]]) -> dict[str, Any]:
    optional_keys = random.sample(list(optional), k=random.randint(0, len(optional)))
    return {key: next(generators[key]) for key in optional_keys}


def generate_datetimes(predicate: Predicate[datetime]) -> Iterator[datetime]:
    yield from (item for item in random_datetimes() if predicate(item))


def generate_floats(predicate: Predicate[float]) -> Iterator[float]:
    yield from (item for item in random_floats() if predicate(item))


def generate_strings(predicate: Predicate[str]) -> Iterator[str]:
    yield from (item for item in random_strings() if predicate(item))


def generate_ints(predicate: Predicate[int]) -> Iterator[int]:
    yield from (item for item in random_ints() if predicate(item))


def generate_uuids(predicate: Predicate[UUID]) -> Iterator[UUID]:
    yield from (item for item in random_uuids() if predicate(item))


def generate_anys(predicate: Predicate) -> Iterator[Any]:
    yield from (item for item in random_anys() if predicate(item))


def generate_even_numbers() -> Iterator[int]:
    yield 0
    yield from (value for value in random_ints() if value % 2 == 0)


def generate_odd_numbers() -> Iterator[int]:
    yield from (value for value in random_ints() if value % 2 != 0)


def function_with_signature(sig: Signature) -> Callable:
    # inspect.signature reads __signature__, so the function only needs to carry it
    def function(*args, **kwargs):
        return None

    function.__signature__ = sig  # type: ignore[attr-defined]
    return function


class CallableObject:
    """Instance whose class implements __call__, so it is a Callable without being a function."""

    # Callables usually have a name; code that reports on them (e.g. instrument) reads it
    __name__ = "callable_object"

    def __call__(self, *args, **kwargs):
        return None


def callable_object_with_signature(sig: Signature) -> Callable:
    # inspect.signature reads __signature__ from the instance before it looks at type(obj).__call__
    obj = CallableObject()
    obj.__signature__ = sig  # type: ignore[attr-defined]
    return obj


def with_parameters(sig: Signature, *parameters: Parameter) -> Signature:
    # A stable sort on kind keeps the order of the original parameters, so the result is a valid signature
    return sig.replace(parameters=sorted([*sig.parameters.values(), *parameters], key=lambda p: p.kind))


def unused_name(sig: Signature) -> str:
    return next(name for name in (f"extra{i}" for i in count()) if name not in sig.parameters)


@cache
def _accepted_names(f: Callable) -> frozenset[str] | None:
    params = signature(f).parameters.values()
    if any(p.kind == Parameter.VAR_KEYWORD for p in params):
        return None  # accepts everything
    return frozenset(p.name for p in params)


def accepted_kwargs(f: Callable, kwargs: dict) -> dict:
    """Keep only the keyword arguments f accepts, e.g. drop length_p for a generator that has no length."""
    if not kwargs or (names := _accepted_names(f)) is None:
        return kwargs
    return {key: value for key, value in kwargs.items() if key in names}


def ignore_unknown_kwargs[F: Callable](dispatcher: F) -> F:
    """Drop keyword arguments the dispatched generator doesn't accept."""

    @wraps(dispatcher)
    def wrapper(predicate, /, **kwargs):
        f = dispatcher.dispatch(type(predicate))  # type: ignore[attr-defined]
        return f(predicate, **accepted_kwargs(f, kwargs))

    wrapper.register = dispatcher.register  # type: ignore[attr-defined]
    wrapper.dispatch = dispatcher.dispatch  # type: ignore[attr-defined]
    wrapper.registry = dispatcher.registry  # type: ignore[attr-defined]
    return wrapper  # type: ignore[return-value]


def random_enum_members(klass: type[Enum]) -> Iterator[Enum]:
    members = list(klass)
    if not members:
        raise ValueError(f"Can't generate values for {klass.__name__}: it has no members")
    if issubclass(klass, Flag):
        # Flags are meant to be combined, so also yield random combinations, including the empty flag
        yield from repeatfunc(lambda: reduce(or_, random.sample(members, random.randint(0, len(members))), klass(0)))
    else:
        yield from repeatfunc(random.choice, None, members)


def random_bytes(min_size: int = 0, max_size: int = 10) -> Iterator[bytes]:
    yield from repeatfunc(lambda: random.randbytes(random.randint(min_size, max_size)))


def random_bytearrays() -> Iterator[bytearray]:
    yield from map(bytearray, random_bytes())


def random_dates() -> Iterator[date]:
    yield from (value.date() for value in random_datetimes())


def random_times() -> Iterator[time]:
    yield from (value.time() for value in random_datetimes())


def random_timedeltas() -> Iterator[timedelta]:
    yield timedelta(0)
    # ponytail: seconds range of about ±100 years, add day/microsecond extremes if functions need them
    yield from repeatfunc(lambda: timedelta(seconds=random.uniform(-3e9, 3e9)))


def random_paths(klass: type[PurePath] = PurePath) -> Iterator[PurePath]:
    segments = random_strings(min_size=1, max_size=8)
    while True:
        yield klass(*take(random.randint(0, 4), segments))


def random_decimals() -> Iterator[Decimal]:
    yield from (Decimal(0), Decimal("-1.5"), Decimal("0.000001"))
    # NaN and Infinity are left out: they break most arithmetic code
    yield from interleave(map(Decimal, random_ints()), map(Decimal, map(str, random_floats())))


def random_supports(protocol: type) -> Iterator[Any]:
    """Generate values for a typing.Supports* protocol, keeping the candidates that implement it."""
    candidates = interleave(random_ints(), random_floats(), random_complex_numbers(), random_decimals(), random_bytes())
    yield from (value for value in candidates if isinstance(value, protocol))


def random_sized() -> Iterator[Any]:
    yield from interleave(random_strings(), random_lists(), random_dicts(), random_sets(), random_tuples())


_simple_patterns: Final = (r"", r"a", r"\d+", r"[a-z]*", r"^\w+$", r"(ab|cd)?", r".", r"x{2,3}")


def random_patterns(kind: type = str) -> Iterator[re.Pattern]:
    patterns = [pattern if kind is str else pattern.encode() for pattern in _simple_patterns]
    yield from repeatfunc(lambda: re.compile(random.choice(patterns)))


def random_slices() -> Iterator[slice]:
    small = list(range(-5, 6))
    steps = [None, *(n for n in small if n)]  # step 0 raises ValueError on use
    while True:
        yield slice(random.choice([None, *small]), random.choice([None, *small]), random.choice(steps))


def random_ranges() -> Iterator[range]:
    while True:
        yield range(random.randint(-10, 10), random.randint(-10, 10), random.choice([1, 2, 3, -1, -2]))


def random_struct_times() -> Iterator[struct_time]:
    # 1970..2100, so time.mktime and strftime accept them on every platform
    while True:
        yield gmtime(random.randint(0, 4_102_444_800))


def random_tzinfos() -> Iterator[tzinfo]:
    yield timezone.utc
    while True:
        yield timezone(timedelta(minutes=random.randint(-23 * 60, 23 * 60)))


def random_exceptions() -> Iterator[Exception]:
    kinds = [ValueError, TypeError, KeyError, RuntimeError, OSError, Exception]
    yield from (random.choice(kinds)(message) for message in random_strings())


def random_forward_refs() -> Iterator[ForwardRef]:
    names = ["int", "str", "float", "bool", "bytes", "list[int]", "dict[str, int]", "int | None"]
    while True:
        yield ForwardRef(random.choice(names))


def random_code_objects() -> Iterator[types.CodeType]:
    sources = ["0", "x", "x + 1", "[i for i in range(3)]", "'a' * 2", "None"]
    while True:
        yield compile(random.choice(sources), "<generated>", "eval")


def random_text_ios() -> Iterator[io.StringIO]:
    yield from map(io.StringIO, random_strings())


def random_ios() -> Iterator[io.IOBase]:
    yield from interleave(map(io.BytesIO, random_bytes()), random_text_ios())


def random_named_tuple_classes() -> Iterator[type]:
    field_names = random_lists(length_p=ge_le_p(lower=0, upper=4), value_p=regex_p("[a-z]{2,4}"))
    yield from (namedtuple("RandomNamedTuple", unique_everseen(names)) for names in field_names)  # type: ignore[misc]  # noqa: PYI024


def random_typed_dict_classes() -> Iterator[type]:
    from typing import TypedDict

    field_names = random_lists(length_p=ge_le_p(lower=0, upper=4), value_p=regex_p("[a-z]{2,4}"))
    field_types = [int, str, float, bool, list[int]]
    for names in field_names:
        yield TypedDict("RandomTypedDict", {name: random.choice(field_types) for name in names})  # type: ignore[operator]


# Valid on every supported Python (3.12+); together they contain nearly every concrete ast node class
_AST_SNIPPETS: Final = (
    "import os\nfrom a import b as c\nglobal g\nassert x, 'msg'\ntype T[U, *Ts, **P] = int",
    "def f(a, b=1, /, *args, c: int = 2, **kw) -> int:\n    'doc'\n    x = y = a + b\n    x += 1\n"
    "    z = [i * 2 for i in a if i] + [*a] + list(i for i in a) + list({i for i in a})\n"
    "    return {k: v for k, v in kw.items()}",
    "for i in range(3):\n    if i and not x or i < 2 or i in y or i is None:\n        continue\nwhile False:\n    break",
    "with open(p) as fh:\n    pass\ntry:\n    raise ValueError(x)\nexcept ValueError as e:\n    del e\nfinally:\n    pass",
    "try:\n    pass\nexcept* OSError:\n    pass",
    "async def g():\n    async with x as y:\n        await y\n    async for z in y:\n        yield z\n"
    "def h():\n    def i():\n        nonlocal x\n    yield from x",
    "class C(B, metaclass=M):\n    attr: int = 1\n    @property\n    def p(self):\n        return lambda q: q[1:2]",
    "match x:\n    case [1, *rest]:\n        pass\n    case {'k': v}:\n        pass\n    case P(a=1) | None:\n        pass",
    "f'{x!r:>10}'\n(a := 1)\nb if c else d\n-a + ~b - +c\n{1, 2}\n[1, 2]\n{1: 2}\n"
    "a / b // c % d ** e @ f << g >> h & i | j ^ k\na == b != c < d <= e > f >= g not in h is not i",
)


def random_ast_nodes(klass: type[ast.AST] = ast.AST) -> Iterator[ast.AST]:
    """Yield nodes from parsed snippets that are instances of klass, e.g. ast.FunctionDef or ast.expr."""
    # Template strings (t"...") only parse on 3.14+
    snippets = (*_AST_SNIPPETS, "t'{x}'") if sys.version_info >= (3, 14) else _AST_SNIPPETS
    nodes = [node for snippet in snippets for node in ast.walk(ast.parse(snippet)) if isinstance(node, klass)]
    nodes += [
        node
        for node in (
            ast.parse("x", mode="eval"),
            ast.parse("()->int", mode="func_type"),
            ast.parse("x", mode="single"),
            *ast.parse("x = 1  # type: ignore", type_comments=True).type_ignores,
        )
        if isinstance(node, klass)
    ]
    if not nodes:
        return  # deprecated classes such as ast.Index or ast.Param never appear in a parsed tree
    while True:
        yield random.choice(nodes)


def random_log_records() -> Iterator[logging.LogRecord]:
    levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    names = random_strings(min_size=1)
    # msg is used as a %-format string by getMessage(), so it must not contain a % without matching args
    messages = (message.replace("%", "%%") for message in random_strings())
    while True:
        level = random.choice(levels)
        yield logging.LogRecord(next(names), level, "<generated>", random.randint(1, 1000), next(messages), (), None)


def random_loggers() -> Iterator[logging.Logger]:
    # ponytail: real loggers registered under a "predicate.generated" prefix; logging keeps them for the process
    yield from (logging.getLogger(f"predicate.generated.{name}") for name in random_strings(min_size=1))


_event_loops: list[asyncio.AbstractEventLoop] = []


def random_event_loops() -> Iterator[asyncio.AbstractEventLoop]:
    # ponytail: a small pool, reused for every value and closed at exit, so generating doesn't leak sockets
    if not _event_loops:
        _event_loops.extend(asyncio.new_event_loop() for _ in range(3))
        atexit.register(lambda: [loop.close() for loop in _event_loops])
    while True:
        yield random.choice(_event_loops)


def random_ipv4_addresses() -> Iterator[ipaddress.IPv4Address]:
    yield from (ipaddress.IPv4Address(0), ipaddress.IPv4Address("127.0.0.1"))
    while True:
        yield ipaddress.IPv4Address(random.getrandbits(32))


def random_ipv6_addresses() -> Iterator[ipaddress.IPv6Address]:
    yield from (ipaddress.IPv6Address(0), ipaddress.IPv6Address("::1"))
    while True:
        yield ipaddress.IPv6Address(random.getrandbits(128))


def random_ipv4_networks() -> Iterator[ipaddress.IPv4Network]:
    while True:
        yield ipaddress.IPv4Network((random.getrandbits(32), random.randint(0, 32)), strict=False)


def random_ipv6_networks() -> Iterator[ipaddress.IPv6Network]:
    while True:
        yield ipaddress.IPv6Network((random.getrandbits(128), random.randint(0, 128)), strict=False)


def random_fractions() -> Iterator[Fraction]:
    yield from (Fraction(0), Fraction(1, 3), Fraction(-7, 2))
    while True:
        yield Fraction(random.randint(-1000, 1000), random.randint(1, 1000))
