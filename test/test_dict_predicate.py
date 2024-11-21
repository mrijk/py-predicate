from predicate import is_iterable_of_p
from predicate.standard_predicates import (
    comp_p,
    depth_eq_p,
    depth_ge_p,
    depth_gt_p,
    depth_le_p,
    depth_lt_p,
    depth_ne_p,
    has_key_p,
    is_dict_p,
    is_int_p,
    is_single_or_list_of_p,
    root_p,
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


def dict_values(x: dict):
    return x.values()


def test_dict_with_only_int_leaves():
    valid_value_p = is_single_or_list_of_p(is_int_p | root_p)
    valid_values_p = is_iterable_of_p(valid_value_p)
    only_int = is_dict_p & comp_p(dict_values, valid_values_p)

    # TODO 1: should we have a is_dict_of_p ?
    # TODO 3: should we have >> for parameters:
    #         valid_value_p = node_p | is_iterable_of_p >> node_p
    #
    # only_int = is_dict_of_p(is_iterable_of_p(is_single_or_iterable_of_p(is_int_p | root_p)))
    # only_int = is_dict_of_p >> is_iterable_of_p >> is_single_or_iterable_of_p >> is_int_p | root_p

    assert not only_int(1)
    assert not only_int({"x": {"y": 2, "z": "foo"}})

    assert only_int({"x": 1})
    assert only_int({"x": {"y": 2}})
    assert only_int({"x": {"y": [2], "z": 3}})
