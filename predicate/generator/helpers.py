import math
import random
import string
import sys
import types
from collections.abc import Callable, Iterable
from datetime import datetime, timedelta
from itertools import cycle
from random import choices
from typing import Any, Final, Iterator
from uuid import UUID, uuid4

from more_itertools import first, interleave, random_permutation, repeatfunc, take

from predicate.generator.generate_predicate import generate_predicate
from predicate.predicate import Predicate
from predicate.standard_predicates import eq_p, ge_le_p, is_hashable_p, is_int_p, is_str_p, regex_p


def random_first_from_iterables(*iterables: Iterable) -> Iterator:
    non_empty_iterables = [it for it in iterables if it]

    while True:
        chosen_iterable = random.choice(non_empty_iterables)
        try:
            yield next(iter(chosen_iterable))
        except StopIteration:
            pass


def set_from_list(value: list, order: bool = False) -> Iterator:
    length = len(value)
    if length and is_hashable_p(first(value)):
        if len(result := set(value)) == length:
            yield result if order else set(random_permutation(result))


def random_complex_numbers(radius: float = 1e6) -> Iterator:
    valid_amplitudes = random_floats(lower=0.0, upper=radius)
    valid_angles = random_floats(lower=0.0, upper=2 * math.pi)

    def to_complex(amplitude: float, angle: float) -> complex:
        return complex(real=amplitude * math.cos(angle), imag=amplitude * math.sin(angle))

    yield from (to_complex(amplitude, angle) for amplitude, angle in zip(valid_amplitudes, valid_angles, strict=False))


def random_callables() -> Iterator:
    yield from random_lambdas()


def generate_lambda(arg_names: list[str]):
    arg_count = len(arg_names)
    arg_str = tuple(arg_names)

    # Bytecode for "return 0"
    bytecode = b"d\x00S\x00"  # LOAD_CONST 0; RETURN_VALUE

    # Constants used in the function (0 is at index 0)
    consts = (0,)

    # Names used in the function (none here)
    names = ()

    # No local variables other than args
    varnames = arg_str

    # Flags
    flags = 0x43  # OPTIMIZED | NEWLOCALS | NOFREE

    # Line numbers etc.
    filename = "<generated>"
    name = "<lambda>"
    firstlineno = 1
    lnotab = b""

    # Get correct CodeType constructor based on Python version
    if sys.version_info >= (3, 11):
        code = types.CodeType(
            arg_count,  # co_argcount
            0,  # co_posonlyargcount
            0,  # co_kwonlyargcount
            arg_count,  # co_nlocals
            2,  # co_stacksize
            flags,  # co_flags
            bytecode,  # co_code
            consts,  # co_consts
            names,  # co_names
            varnames,  # co_varnames
            filename,  # co_filename
            name,  # co_name
            name,  # co_qualname
            firstlineno,  # co_firstlineno
            lnotab,  # co_linetable (Py3.11+)
            b"",  # co_exceptiontable
            (),  # co_freevars
            (),  # co_cellvars
        )
    elif sys.version_info >= (3, 8):
        code = types.CodeType(
            arg_count,  # co_argcount
            0,  # co_posonlyargcount
            0,  # co_kwonlyargcount
            arg_count,  # co_nlocals
            2,  # co_stacksize
            flags,  # co_flags
            bytecode,  # co_code
            consts,  # co_consts
            names,  # co_names
            varnames,  # co_varnames
            filename,  # co_filename
            name,  # co_name
            firstlineno,  # co_firstlineno
            lnotab,  # co_lnotab
            (),  # co_freevars
            (),  # co_cellvars
        )
    else:
        code = types.CodeType(
            arg_count,  # co_argcount
            arg_count,  # co_nlocals
            2,  # co_stacksize
            flags,  # co_flags
            bytecode,  # co_code
            consts,  # co_consts
            names,  # co_names
            varnames,  # co_varnames
            filename,  # co_filename
            name,  # co_name
            firstlineno,  # co_firstlineno
            lnotab,  # co_lnotab
            (),  # co_freevars
            (),  # co_cellvars
        )

    return types.FunctionType(code, {})


default_nr_of_parameters_p: Final = eq_p(1)


def random_lambdas(nr_of_parameters_p: Predicate = default_nr_of_parameters_p) -> Iterator:
    value_p = regex_p("[a-z]{2,3}")
    valid_parameter_lists = random_lists(length_p=nr_of_parameters_p, value_p=value_p)
    yield from (generate_lambda(list(arg_names)) for arg_names in valid_parameter_lists)


default_size_p: Final = ge_le_p(lower=0, upper=5)


def random_dicts(
    key_p: Predicate = is_str_p, value_p: Predicate = is_int_p, size_p: Predicate = default_size_p
) -> Iterator:
    from predicate import generate_true

    if size_p(0):
        yield {}

    valid_keys = generate_true(key_p)
    valid_values = generate_true(value_p)
    valid_sizes = generate_true(size_p)

    while True:
        if (valid_size := next(valid_sizes)) >= 0:
            keys = take(valid_size, valid_keys)
            values = take(valid_size, valid_values)
            yield dict(zip(keys, values, strict=False))


def random_datetimes(lower: datetime | None = None, upper: datetime | None = None) -> Iterator:
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


def random_predicates(*, max_depth: int = 10, klass: type = int) -> Iterator:
    subclasses = Predicate.__subclasses__()

    iterables = [generate_predicate(subclass, max_depth=max_depth, klass=klass) for subclass in subclasses]  # type: ignore

    yield from random_first_from_iterables(*iterables)


default_length_p: Final = ge_le_p(lower=0, upper=10)


def random_sets(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator:
    from predicate import generate_true

    if length_p(0):
        yield set()
    valid_lengths = generate_true(length_p)

    while True:
        if (length := next(valid_lengths)) > 0:
            values = take(length, generate_true(value_p))
            if len(result := set(values)) == length:
                yield result


def random_bools() -> Iterator:
    yield from (False, True)
    yield from repeatfunc(random.choice, None, (False, True))


def random_containers() -> Iterator:
    yield from cycle(([], {}))


def random_strings(min_size: int = 0, max_size: int = 10) -> Iterator:
    population = string.ascii_letters + string.digits
    while True:
        length = random.randint(min_size, max_size)
        yield "".join(choices(population, k=length))


def random_floats(lower: float = -1e-6, upper: float = 1e6) -> Iterator:
    def between(limit: float) -> Iterator[float]:
        low = max(-limit, lower)
        high = min(limit, upper)
        if high >= low:
            yield from (random.uniform(low, high) for _ in range(0, int(limit)))

    while True:
        yield from between(1.0)
        yield from between(10.0)
        yield from between(100.0)


def random_ints(lower: int = -sys.maxsize, upper: int = sys.maxsize, **_kwargs) -> Iterator[int]:
    def between(limit: int) -> Iterator[int]:
        low = max(-limit, lower)
        high = min(limit, upper)
        if high >= low:
            yield from (random.randint(low, high) for _ in range(0, limit))

    while True:
        yield from between(1)
        yield from between(10)
        yield from between(100)


def random_iterables(length_p: Predicate = default_length_p, value_p=is_int_p) -> Iterator[Iterable]:
    if length_p(0):
        yield from ([], {}, (), "")
    else:
        iterable_1 = random_sets(length_p=length_p, value_p=value_p)
        iterable_2 = random_lists(length_p=length_p, value_p=value_p)
        iterable_3 = random_tuples(length_p=length_p, value_p=value_p)
        yield from random_first_from_iterables(iterable_1, iterable_2, iterable_3)


def random_lists(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[Iterable]:
    from predicate import generate_true

    if length_p(0):
        yield []

    valid_lengths = generate_true(length_p)
    while True:
        if (length := next(valid_lengths)) >= 0:
            yield take(length, generate_true(value_p))


def random_tuples(length_p: Predicate = default_length_p, value_p: Predicate = is_int_p) -> Iterator[Iterable]:
    yield from (tuple(random_list) for random_list in random_lists(length_p=length_p, value_p=value_p))


def random_uuids() -> Iterator[UUID]:
    yield from repeatfunc(uuid4)


def random_anys() -> Iterator:
    yield from interleave(random_bools(), random_ints(), random_strings(), random_floats(), random_datetimes())


def random_values_of_type(klass: type) -> Iterator:
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


def random_constrained_values_of_type(klass: type) -> Iterator:
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


def random_constrained_pairs_of_type(klass: type) -> Iterator[tuple]:
    def ordered_tuple(x: Any, y: Any) -> tuple:
        return (x, y) if x <= y else (y, x)

    values_1 = random_constrained_values_of_type(klass)
    values_2 = random_constrained_values_of_type(klass)
    values = zip(values_1, values_2, strict=False)

    yield from (ordered_tuple(x, y) for x, y in values)


def generate_strings(predicate: Predicate[str]) -> Iterator[str]:
    yield from (item for item in random_strings() if predicate(item))


def generate_ints(predicate: Predicate[int]) -> Iterator[int]:
    yield from (item for item in random_ints() if predicate(item))


def generate_uuids(predicate: Predicate[UUID]) -> Iterator[UUID]:
    yield from (item for item in random_uuids() if predicate(item))


def generate_anys(predicate: Predicate) -> Iterator:
    yield from (item for item in random_anys() if predicate(item))
