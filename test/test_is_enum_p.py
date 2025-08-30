from enum import Enum, IntEnum, StrEnum, auto

from predicate import is_enum_p, is_int_enum_p, is_str_enum_p


def test_is_enum_p_ok():
    class MyEnum(Enum):
        RED = 1
        BLUE = 2
        GREEN = 3

    assert is_enum_p(MyEnum)
    assert not is_int_enum_p(MyEnum)


def test_is_enum_p_fail():
    assert not is_enum_p(int)


def test_is_int_enum():
    class MyEnum(IntEnum):
        RED = 1
        BLUE = 2
        GREEN = 3

    assert is_enum_p(MyEnum)
    assert is_int_enum_p(MyEnum)


def test_is_str_enum():
    class MyEnum(StrEnum):
        RED = auto()
        BLUE = auto()
        GREEN = auto()

    assert is_enum_p(MyEnum)
    assert is_str_enum_p(MyEnum)
