import pytest
import yaml

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    count_p,
    eq_p,
    exactly_n,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    has_path_p,
    implies_p,
    in_p,
    is_dict_of_p,
    is_falsy_p,
    is_instance_p,
    is_int_p,
    is_list_of_p,
    is_none_p,
    is_not_none_p,
    is_real_subset_p,
    is_real_superset_p,
    is_set_of_p,
    is_str_p,
    is_subclass_p,
    is_subset_p,
    is_superset_p,
    is_truthy_p,
    is_tuple_of_p,
    juxt_p,
    le_p,
    lt_p,
    match_p,
    ne_p,
    not_in_p,
    optional,
    regex_p,
    tee_p,
    to_json,
    to_yaml,
)
from predicate.is_same_predicate import is_same_p
from predicate.named_predicate import NamedPredicate


def parsed(predicate) -> dict:
    """Round-trip helper: parse the YAML output back to a dict."""
    return yaml.safe_load(to_yaml(predicate))


@pytest.mark.skip
def test_format_yaml_false():
    assert parsed(always_false_p) == to_json(always_false_p)


@pytest.mark.skip
def test_format_yaml_true():
    assert parsed(always_true_p) == to_json(always_true_p)


@pytest.mark.skip
def test_format_yaml_and():
    predicate = always_true_p & always_false_p

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_or():
    predicate = always_true_p | always_false_p

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_xor():
    predicate = always_true_p ^ always_false_p

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_not():
    predicate = ~always_true_p

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_all():
    predicate = all_p(predicate=always_true_p)

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_any():
    predicate = any_p(predicate=always_true_p)

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_eq():
    assert parsed(eq_p(5)) == to_json(eq_p(5))


@pytest.mark.skip
def test_format_yaml_ne():
    assert parsed(ne_p(13)) == to_json(ne_p(13))


@pytest.mark.skip
def test_format_yaml_ge():
    assert parsed(ge_p(2)) == to_json(ge_p(2))


@pytest.mark.skip
def test_format_yaml_gt():
    assert parsed(gt_p(2)) == to_json(gt_p(2))


@pytest.mark.skip
def test_format_yaml_le():
    assert parsed(le_p(10)) == to_json(le_p(10))


@pytest.mark.skip
def test_format_yaml_lt():
    assert parsed(lt_p(10)) == to_json(lt_p(10))


@pytest.mark.skip
def test_format_yaml_ge_le():
    assert parsed(ge_le_p(1, 10)) == to_json(ge_le_p(1, 10))


@pytest.mark.skip
def test_format_yaml_ge_lt():
    assert parsed(ge_lt_p(1, 10)) == to_json(ge_lt_p(1, 10))


@pytest.mark.skip
def test_format_yaml_gt_le():
    assert parsed(gt_le_p(1, 10)) == to_json(gt_le_p(1, 10))


@pytest.mark.skip
def test_format_yaml_gt_lt():
    assert parsed(gt_lt_p(1, 10)) == to_json(gt_lt_p(1, 10))


@pytest.mark.skip
def test_format_yaml_is_instance_single():
    assert parsed(is_int_p) == to_json(is_int_p)


@pytest.mark.skip
def test_format_yaml_is_instance_multiple():
    predicate = is_instance_p(int, str)

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_is_falsy():
    assert parsed(is_falsy_p) == to_json(is_falsy_p)


@pytest.mark.skip
def test_format_yaml_is_truthy():
    assert parsed(is_truthy_p) == to_json(is_truthy_p)


@pytest.mark.skip
def test_format_yaml_is_none():
    assert parsed(is_none_p) == to_json(is_none_p)


@pytest.mark.skip
def test_format_yaml_is_not_none():
    assert parsed(is_not_none_p) == to_json(is_not_none_p)


@pytest.mark.skip
def test_format_yaml_named():
    predicate = NamedPredicate(name="foo")

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_tee():
    predicate = tee_p(fn=lambda _: None)

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_fn():
    predicate = fn_p(lambda x: x)

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_juxt():
    predicate = juxt_p(always_true_p, always_false_p, evaluate=all_p(always_true_p))

    assert parsed(predicate) == to_json(predicate)


@pytest.mark.skip
def test_format_yaml_has_key():
    assert parsed(has_key_p("name")) == to_json(has_key_p("name"))


@pytest.mark.skip
def test_format_yaml_regex():
    assert parsed(regex_p(r"\d+")) == to_json(regex_p(r"\d+"))


@pytest.mark.skip
def test_format_yaml_implies():
    assert parsed(implies_p(always_true_p)) == to_json(implies_p(always_true_p))


@pytest.mark.skip
def test_format_yaml_has_length():
    assert parsed(has_length_p(eq_p(3))) == to_json(has_length_p(eq_p(3)))


@pytest.mark.skip
def test_format_yaml_count():
    assert parsed(count_p(is_int_p, eq_p(2))) == to_json(count_p(is_int_p, eq_p(2)))


@pytest.mark.skip
def test_format_yaml_list_of():
    assert parsed(is_list_of_p(is_int_p)) == to_json(is_list_of_p(is_int_p))


@pytest.mark.skip
def test_format_yaml_set_of():
    assert parsed(is_set_of_p(is_int_p)) == to_json(is_set_of_p(is_int_p))


@pytest.mark.skip
def test_format_yaml_optional():
    assert parsed(optional(is_int_p)) == to_json(optional(is_int_p))


@pytest.mark.skip
def test_format_yaml_exactly():
    assert parsed(exactly_n(3, is_int_p)) == to_json(exactly_n(3, is_int_p))


@pytest.mark.skip
def test_format_yaml_tuple_of():
    assert parsed(is_tuple_of_p(is_int_p, is_str_p)) == to_json(is_tuple_of_p(is_int_p, is_str_p))


@pytest.mark.skip
def test_format_yaml_has_path():
    assert parsed(has_path_p(eq_p("a"), eq_p("b"))) == to_json(has_path_p(eq_p("a"), eq_p("b")))


@pytest.mark.skip
def test_format_yaml_match():
    assert parsed(match_p(is_int_p, is_str_p)) == to_json(match_p(is_int_p, is_str_p))


@pytest.mark.skip
def test_format_yaml_is_subclass_single():
    assert parsed(is_subclass_p(int)) == to_json(is_subclass_p(int))


@pytest.mark.skip
def test_format_yaml_is_subclass_union():
    assert parsed(is_subclass_p(int | str)) == to_json(is_subclass_p(int | str))


@pytest.mark.skip
def test_format_yaml_is_subset():
    assert parsed(is_subset_p({1, 2, 3})) == to_json(is_subset_p({1, 2, 3}))


@pytest.mark.skip
def test_format_yaml_is_real_subset():
    assert parsed(is_real_subset_p({1, 2, 3})) == to_json(is_real_subset_p({1, 2, 3}))


@pytest.mark.skip
def test_format_yaml_is_superset():
    assert parsed(is_superset_p({1, 2, 3})) == to_json(is_superset_p({1, 2, 3}))


@pytest.mark.skip
def test_format_yaml_is_real_superset():
    assert parsed(is_real_superset_p({1, 2, 3})) == to_json(is_real_superset_p({1, 2, 3}))


@pytest.mark.skip
def test_format_yaml_in():
    assert parsed(in_p([1, 2, 3])) == to_json(in_p([1, 2, 3]))


@pytest.mark.skip
def test_format_yaml_not_in():
    assert parsed(not_in_p([1, 2, 3])) == to_json(not_in_p([1, 2, 3]))


@pytest.mark.skip
def test_format_yaml_dict_of():
    assert parsed(is_dict_of_p(("name", is_str_p))) == to_json(is_dict_of_p(("name", is_str_p)))


@pytest.mark.skip
def test_format_yaml_is_same():
    assert parsed(is_same_p(always_true_p)) == to_json(is_same_p(always_true_p))


@pytest.mark.skip
def test_format_yaml_unknown(unknown_p):
    assert parsed(unknown_p) == to_json(unknown_p)
