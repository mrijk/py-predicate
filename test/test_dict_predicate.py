from predicate.standard_predicates import (
    depth_eq_p,
    depth_ge_p,
    depth_gt_p,
    depth_le_p,
    depth_lt_p,
    depth_ne_p,
    has_key_p,
)


def test_has_key_p():
    has_key_x = has_key_p("x")

    assert not has_key_x({})
    assert not has_key_x({"y": 13})
    assert has_key_x({"x": 13})


def test_depth_eq_p():
    depth_eq_3 = depth_eq_p(3)

    assert not depth_eq_3({})
    assert not depth_eq_3({"x": {}})

    assert depth_eq_3({"x": {"y": 5}})


def test_depth_ne_p():
    depth_ne_3 = depth_ne_p(3)

    assert depth_ne_3({})
    assert depth_ne_3({"x": {}})

    assert not depth_ne_3({"x": {"y": 5}})


def test_depth_le_p():
    depth_le_3 = depth_le_p(3)

    assert depth_le_3({})
    assert depth_le_3({"x": {}})
    assert depth_le_3({"x": {"y": 5}})
    assert not depth_le_3({"x": {"y": {"z": 5}}})


def test_depth_lt_p():
    depth_lt_3 = depth_lt_p(3)

    assert depth_lt_3({})
    assert depth_lt_3({"x": {}})
    assert not depth_lt_3({"x": {"y": 5}})
    assert not depth_lt_3({"x": {"y": {"z": 5}}})


def test_depth_ge_p():
    depth_ge_3 = depth_ge_p(3)

    assert not depth_ge_3({})
    assert not depth_ge_3({"x": {}})
    assert depth_ge_3({"x": {"y": 5}})
    assert depth_ge_3({"x": {"y": {"z": 5}}})


def test_depth_gt_p():
    depth_gt_3 = depth_gt_p(3)

    assert not depth_gt_3({})
    assert not depth_gt_3({"x": {}})
    assert not depth_gt_3({"x": {"y": 5}})
    assert depth_gt_3({"x": {"y": {"z": 5}}})
