import pytest

from predicate.spec.instrument import instrument, instrument_class

# --- @instrument on instance methods ---


def test_instrument_method_ok():
    class Adder:
        @instrument
        def add(self, x: int, y: int) -> int:
            return x + y

    assert Adder().add(1, 2) == 3


def test_instrument_method_wrong_arg():
    class Adder:
        @instrument
        def add(self, x: int, y: int) -> int:
            return x + y

    with pytest.raises(ValueError, match="Parameter predicate"):
        Adder().add(1, "not an int")  # type: ignore[arg-type]


def test_instrument_method_wrong_return():
    class Adder:
        @instrument
        def add(self, x: int, y: int) -> int:
            return "oops"  # type: ignore[return-value]

    with pytest.raises(ValueError, match="Return predicate"):
        Adder().add(1, 2)


# --- instrument_class ---


def test_instrument_class_instruments_all_methods():
    class Calculator:
        def add(self, x: int, y: int) -> int:
            return x + y

        def negate(self, x: int) -> int:
            return -x

    instrument_class(Calculator)

    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.negate(5) == -5

    with pytest.raises(ValueError, match="Parameter predicate"):
        calc.add(1, "bad")  # type: ignore[arg-type]


def test_instrument_class_with_pattern():
    class Service:
        def get_value(self, x: int) -> int:
            return x

        def set_value(self, x: int) -> int:
            return x

    instrument_class(Service, pattern="get_*")

    svc = Service()
    assert svc.get_value(1) == 1
    assert hasattr(svc.get_value, "__spec__")
    assert not hasattr(svc.set_value, "__spec__")


def test_instrument_class_on_error():
    errors: list[str] = []

    class Foo:
        def bar(self, x: int) -> int:
            return x

    instrument_class(Foo, on_error=errors.append)

    Foo().bar("oops")  # type: ignore[arg-type]
    assert errors


# --- @instrument on a class ---


def test_instrument_decorator_on_class():
    @instrument
    class Calculator:
        def add(self, x: int, y: int) -> int:
            return x + y

    calc = Calculator()
    assert calc.add(1, 2) == 3

    with pytest.raises(ValueError, match="Parameter predicate"):
        calc.add(1, "bad")  # type: ignore[arg-type]


def test_instrument_decorator_on_class_with_on_error():
    errors: list[str] = []

    @instrument(on_error=errors.append)
    class Foo:
        def bar(self, x: int) -> int:
            return x

    Foo().bar("oops")  # type: ignore[arg-type]
    assert errors
