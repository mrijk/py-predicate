from predicate import same_signature_p


def test_same_signature_p_ok():
    def f() -> int | str:
        pass

    def ok_1() -> int:
        pass

    def ok_2() -> str:
        pass

    predicate = same_signature_p(f)

    assert predicate(ok_1)
    assert predicate(ok_2)


def test_same_signature_p_return_type_nok():
    def f() -> None:
        pass

    def fail_1() -> int:
        pass

    predicate = same_signature_p(f)

    assert not predicate(fail_1)


def test_same_signature_p_args_len_nok():
    def f() -> None:
        pass

    def fail_1(x: int) -> None:
        pass

    predicate = same_signature_p(f)

    assert not predicate(fail_1)


def test_same_signature_p_args_name_nok():
    def f(x: int) -> None:
        pass

    def fail_1(y: int) -> None:
        pass

    predicate = same_signature_p(f)

    assert not predicate(fail_1)


def test_same_signature_p_args_type_ok():
    def f(x: int) -> int | float:
        pass

    def ok_1(x: int | float) -> int:
        pass

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_with_additional_default_args():
    def f(x: int) -> int | float:
        pass

    def ok_1(x: int | float, z: int | None = None) -> int:
        pass

    predicate = same_signature_p(f)

    assert predicate(ok_1)


def test_same_signature_p_args_type_nok():
    def f(x: float) -> None:
        pass

    def fail_1(x: str) -> None:
        pass

    predicate = same_signature_p(f)

    assert not predicate(fail_1)
