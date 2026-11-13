import pytest
from hypothesis import given, settings

from predicate import ge_p, is_int_p, is_str_p, lt_p
from predicate.integrations.hypothesis import from_spec, given_spec
from predicate.spec.spec import InvalidSpecError, SpecViolationError


def adder(x, y):
    return x + y


add_spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}


def test_from_spec_generates_all_arguments():
    spec = {"args": {"x": ge_p(0), "y": is_str_p}, "ret": is_int_p}

    @settings(max_examples=50)
    @given(from_spec(adder, spec))
    def check(value):
        assert set(value) == {"x", "y"}
        assert value["x"] >= 0 and isinstance(value["y"], str)

    check()


def test_from_spec_honours_pre():
    spec = add_spec | {"pre": lambda x, y: x < y}

    @settings(max_examples=50)
    @given(from_spec(adder, spec))
    def check(value):
        assert value["x"] < value["y"]

    check()


def test_from_spec_from_annotations():
    def f(x: int, s: str) -> int:
        return x

    @settings(max_examples=50)
    @given(from_spec(f))
    def check(value):
        assert isinstance(value["x"], int) and isinstance(value["s"], str)

    check()


def test_from_spec_no_arguments():
    def f() -> int:
        return 1

    @given(from_spec(f))
    def check(value):
        assert value == {}

    check()


def test_from_spec_invalid_spec():
    with pytest.raises(InvalidSpecError):
        from_spec(adder, {"args": {"z": is_int_p}, "ret": is_int_p})


def test_given_spec_happy():
    given_spec(adder, add_spec)()


def test_given_spec_from_annotations():
    def f(x: int, y: int) -> int:
        return x + y

    given_spec(f)()


def test_given_spec_var_args():
    def f(*numbers: int) -> int:
        return sum(numbers)

    given_spec(f)()


def test_given_spec_wrong_return_type():
    def f(x, y):
        return str(x + y)

    with pytest.raises(SpecViolationError):
        given_spec(f, add_spec)()


def test_given_spec_fn_constraint():
    def f(x):
        return x - 1

    spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret > x}
    with pytest.raises(SpecViolationError):
        given_spec(f, spec)()


def test_given_spec_fn_constraint_happy():
    def f(x):
        return x + 1

    given_spec(f, {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret > x})()


def test_given_spec_expected_exception():
    def f(x):
        if x < 0:
            raise ValueError("negative")
        return x

    spec = {"args": {"x": is_int_p}, "ret": is_int_p, "raises": ValueError}
    given_spec(f, spec)()


def test_given_spec_unexpected_exception():
    def f(x):
        raise KeyError(x)

    spec = {"args": {"x": is_int_p}, "ret": is_int_p, "raises": ValueError}
    with pytest.raises(SpecViolationError):
        given_spec(f, spec)()


def test_given_spec_exception_not_in_spec_propagates():
    def f(x):
        raise KeyError(x)

    with pytest.raises(KeyError):
        given_spec(f, {"args": {"x": is_int_p}, "ret": is_int_p})()


def test_given_spec_honours_pre():
    def f(x):
        assert x < 10  # only valid because pre restricts the inputs
        return x

    given_spec(f, {"args": {"x": is_int_p}, "ret": is_int_p, "pre": lambda x: x < 10})()


def test_given_spec_shrinks_to_minimal_example():
    def f(x):
        return x if x < 100 else "oops"

    spec = {"args": {"x": ge_p(0) & lt_p(1000)}, "ret": is_int_p}
    with pytest.raises(SpecViolationError) as error:
        given_spec(f, spec)()
    assert "'x': 100" in "".join(error.value.__notes__)


def test_given_spec_async_not_supported():
    async def f(x: int) -> int:
        return x

    with pytest.raises(NotImplementedError):
        given_spec(f)


def test_given_spec_generator_not_supported():
    def f(x: int):
        yield x

    with pytest.raises(NotImplementedError):
        given_spec(f, {"args": {"x": is_int_p}, "ret": is_int_p})


def test_given_spec_class_not_supported():
    class Adder:
        def __call__(self, x):
            return x

    with pytest.raises(NotImplementedError):
        given_spec(Adder(), {"args": {"x": is_int_p}, "ret": is_int_p})
