from typing import Any

from predicate.all_predicate import all_p
from predicate.always_false_predicate import always_false_p
from predicate.always_true_predicate import always_true_p
from predicate.any_predicate import any_p
from predicate.count_predicate import count_p
from predicate.dict_of_predicate import is_dict_of_p
from predicate.eq_predicate import eq_p
from predicate.exactly_predicate import exactly_n
from predicate.ge_predicate import ge_p
from predicate.gt_predicate import gt_p
from predicate.has_key_predicate import has_key_p
from predicate.has_length_predicate import has_length_p
from predicate.has_path_predicate import has_path_p
from predicate.implies_predicate import implies_p
from predicate.in_predicate import in_p
from predicate.is_close_predicate import is_close_p
from predicate.is_falsy_predicate import is_falsy_p
from predicate.is_instance_predicate import is_instance_p
from predicate.is_none_predicate import is_none_p
from predicate.is_not_none_predicate import is_not_none_p
from predicate.is_same_predicate import is_same_p
from predicate.is_subclass_predicate import is_subclass_p
from predicate.is_truthy_predicate import is_truthy_p
from predicate.juxt_predicate import juxt_p
from predicate.le_predicate import le_p
from predicate.list_of_predicate import is_list_of_p
from predicate.lt_predicate import lt_p
from predicate.match_predicate import match_p
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import ne_p
from predicate.not_in_predicate import not_in_p
from predicate.optional_predicate import optional
from predicate.predicate import Predicate
from predicate.range_predicate import ge_le_p, ge_lt_p, gt_le_p, gt_lt_p
from predicate.regex_predicate import regex_p
from predicate.set_of_predicate import is_set_of_p
from predicate.set_predicates import is_real_subset_p, is_real_superset_p, is_subset_p, is_superset_p
from predicate.tuple_of_predicate import is_tuple_of_p


def from_json(data: dict[str, Any]) -> Predicate:
    """Parse a predicate from its JSON representation."""
    ((key, value),) = data.items()

    match key:
        case "all":
            return all_p(from_json(value["predicate"]))
        case "false":
            return always_false_p
        case "true":
            return always_true_p
        case "and":
            return from_json(value["left"]) & from_json(value["right"])
        case "any":
            return any_p(from_json(value["predicate"]))
        case "count":
            return count_p(predicate=from_json(value["predicate"]), length_p=from_json(value["length_p"]))
        case "dict_of":
            pairs = [(from_json(k), from_json(v)) for k, v in value["kv"]]
            return is_dict_of_p(*pairs)
        case "eq":
            return eq_p(value["v"])
        case "exactly":
            return exactly_n(value["n"], from_json(value["predicate"]))
        case "ge_le":
            return ge_le_p(lower=value["lower"], upper=value["upper"])
        case "ge_lt":
            return ge_lt_p(lower=value["lower"], upper=value["upper"])
        case "ge":
            return ge_p(value["v"])
        case "gt_le":
            return gt_le_p(lower=value["lower"], upper=value["upper"])
        case "gt_lt":
            return gt_lt_p(lower=value["lower"], upper=value["upper"])
        case "gt":
            return gt_p(value["v"])
        case "has_key":
            return has_key_p(value["key"])
        case "has_length":
            return has_length_p(from_json(value["length_p"]))
        case "has_path":
            return has_path_p(*[from_json(p) for p in value["path"]])
        case "implies":
            return implies_p(from_json(value["predicate"]))
        case "in":
            return in_p(value["v"])
        case "is_close":
            return is_close_p(value["target"], rel_tol=value["rel_tol"], abs_tol=value["abs_tol"])
        case "is_falsy":
            return is_falsy_p
        case "is_instance":
            klasses = [_resolve_class(name) for name in value["klass"]]
            return is_instance_p(*klasses)
        case "is_none":
            return is_none_p
        case "is_not_none":
            return is_not_none_p
        case "is_real_subset":
            return is_real_subset_p(set(value["v"]))
        case "is_real_superset":
            return is_real_superset_p(set(value["v"]))
        case "is_same":
            return is_same_p(from_json(value["predicate"]))
        case "is_subclass":
            klasses = [_resolve_class(name) for name in value["klass"]]
            return is_subclass_p(tuple(klasses) if len(klasses) > 1 else klasses[0])
        case "is_subset":
            return is_subset_p(set(value["v"]))
        case "is_superset":
            return is_superset_p(set(value["v"]))
        case "is_truthy":
            return is_truthy_p
        case "juxt":
            predicates = [from_json(p) for p in value["predicates"]]
            return juxt_p(*predicates, evaluate=from_json(value["evaluate"]))
        case "le":
            return le_p(value["v"])
        case "list_of":
            return is_list_of_p(from_json(value["predicate"]))
        case "lt":
            return lt_p(value["v"])
        case "match":
            predicates = [from_json(p) for p in value["predicates"]]
            return match_p(*predicates, full_match=value["full_match"])
        case "ne":
            return ne_p(value["v"])
        case "not":
            return ~from_json(value["predicate"])
        case "not_in":
            return not_in_p(value["v"])
        case "optional":
            return optional(from_json(value["predicate"]))
        case "or":
            return from_json(value["left"]) | from_json(value["right"])
        case "reduce":
            raise ValueError("reduce_p cannot be deserialized from JSON: function reference required")
        case "regex":
            return regex_p(value["pattern"])
        case "set_of":
            return is_set_of_p(from_json(value["predicate"]))
        case "tuple_of":
            return is_tuple_of_p(*[from_json(p) for p in value["predicates"]])
        case "variable":
            return NamedPredicate(name=value)
        case "xor":
            return from_json(value["left"]) ^ from_json(value["right"])
        case _:
            raise ValueError(f"Unknown predicate type: {key!r}")


_CLASS_REGISTRY: dict[str, type] = {
    "bool": bool,
    "bytes": bytes,
    "complex": complex,
    "dict": dict,
    "float": float,
    "frozenset": frozenset,
    "int": int,
    "list": list,
    "set": set,
    "str": str,
    "tuple": tuple,
}


def _resolve_class(name: str) -> type:
    if klass := _CLASS_REGISTRY.get(name):
        return klass
    raise ValueError(f"Unknown class: {name!r}")
