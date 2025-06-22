from enum import Enum, IntEnum

from predicate import is_enum_p


def test_is_enum_p_ok():
    class MyEnum(Enum):
        RED = 1
        BLUE = 2
        GREEN = 3

    assert is_enum_p(MyEnum)


def test_is_enum_p_with_int_enum():
    class MyEnum(IntEnum):
        RED = 1
        BLUE = 2
        GREEN = 3

    assert is_enum_p(MyEnum)


def test_is_enum_p_fail():
    assert not is_enum_p(int)
