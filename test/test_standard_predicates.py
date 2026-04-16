from predicate.standard_predicates import dict_depth


def test_dict_depth_empty_list():
    assert dict_depth([]) == 0


def test_dict_depth_int_list():
    # 1 (list) + max(dict_depth(1)) = 1 + 1 = 2
    assert dict_depth([1, 2]) == 2


def test_dict_depth_nested_list():
    # 1 (list) + max(dict_depth({"a": 1})) = 1 + (1 + dict_depth(1)) = 1 + 2 = 3
    assert dict_depth([{"a": 1}]) == 3
