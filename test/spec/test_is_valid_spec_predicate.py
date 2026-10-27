from predicate import explain, is_int_p, is_str_p, is_valid_spec_p


def f(x: int, y) -> int:
    return x


def test_is_valid_spec_p():
    predicate = is_valid_spec_p(f)

    assert predicate({"args": {"y": is_str_p}})
    assert predicate({"args": {"x": is_int_p, "y": is_str_p}})
    assert not predicate({"args": {}})
    assert not predicate({"args": {"y": is_str_p, "z": is_int_p}})
    assert not predicate({"args": {"x": is_str_p, "y": is_str_p}})


def test_is_valid_spec_p_no_ret():
    def g(x: int):
        return x

    predicate = is_valid_spec_p(g)

    assert not predicate({"args": {}})
    assert predicate({"args": {}, "ret": is_int_p})


def test_is_valid_spec_p_does_not_change_spec():
    spec = {"args": {"y": is_str_p}}

    is_valid_spec_p(f)(spec)

    assert spec == {"args": {"y": is_str_p}}


def test_is_valid_spec_p_repr():
    assert repr(is_valid_spec_p(f)) == "is_valid_spec_p(f)"


def test_is_valid_spec_p_explain():
    expected = {"reason": "Unannotated parameter 'y' not in spec", "result": False}

    assert explain(is_valid_spec_p(f), {"args": {}}) == expected
