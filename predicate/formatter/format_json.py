from types import UnionType
from typing import Any, get_args

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.count_predicate import CountPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.exactly_predicate import ExactlyPredicate
from predicate.fn_predicate import FnPredicate
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.has_path_predicate import HasPathPredicate
from predicate.implies_predicate import ImpliesPredicate
from predicate.in_predicate import InPredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_same_predicate import IsSamePredicate
from predicate.is_subclass_predicate import IsSubclassPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.juxt_predicate import JuxtPredicate
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.match_predicate import MatchPredicate
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.optional_predicate import OptionalPredicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.regex_predicate import RegexPredicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import (
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)
from predicate.tee_predicate import TeePredicate
from predicate.tuple_of_predicate import TupleOfPredicate


def to_json(predicate: Predicate) -> dict[str, Any]:
    """Format predicate as json."""

    def to_value(predicate) -> tuple[str, Any]:
        match predicate:
            case AllPredicate(all_predicate):
                return "all", {"predicate": to_json(all_predicate)}
            case AlwaysFalsePredicate():
                return "false", False
            case AlwaysTruePredicate():
                return "true", True
            case AndPredicate(left, right):
                return "and", {"left": to_json(left), "right": to_json(right)}
            case AnyPredicate(any_predicate):
                return "any", {"predicate": to_json(any_predicate)}
            case CountPredicate(predicate, length_p):
                return "count", {"predicate": to_json(predicate), "length_p": to_json(length_p)}
            case DictOfPredicate(key_value_predicates):
                return "dict_of", {"kv": [[to_json(k), to_json(v)] for k, v in key_value_predicates]}
            case EqPredicate(v):
                return "eq", {"v": v}
            case ExactlyPredicate(n, predicate):
                return "exactly", {"n": n, "predicate": to_json(predicate)}
            case FnPredicate(predicate_fn):
                name = predicate_fn.__code__.co_name
                return "fn", {"name": name}
            case HasKeyPredicate(key):
                return "has_key", {"key": key}
            case HasLengthPredicate(length_p):
                return "has_length", {"length_p": to_json(length_p)}
            case HasPathPredicate(path):
                return "has_path", {"path": [to_json(p) for p in path]}
            case ImpliesPredicate(predicate):
                return "implies", {"predicate": to_json(predicate)}
            case InPredicate(v):
                return "in", {"v": list(v)}
            case IsFalsyPredicate():
                return "is_falsy", None
            case IsInstancePredicate(instance_klass):
                return "is_instance", {"klass": [k.__name__ for k in instance_klass]}
            case IsNonePredicate():
                return "is_none", None
            case IsNotNonePredicate():
                return "is_not_none", None
            case IsRealSubsetPredicate(v):
                return "is_real_subset", {"v": list(v)}
            case IsRealSupersetPredicate(v):
                return "is_real_superset", {"v": list(v)}
            case IsSamePredicate(predicate):
                return "is_same", {"predicate": to_json(predicate)}
            case IsSubclassPredicate(class_or_tuple):
                match class_or_tuple:
                    case tuple() as klasses:
                        names = [k.__name__ for k in klasses]
                    case UnionType() as union_type:
                        names = [k.__name__ for k in get_args(union_type)]
                    case klass:
                        names = [klass.__name__]
                return "is_subclass", {"klass": names}
            case IsSubsetPredicate(v):
                return "is_subset", {"v": list(v)}
            case IsSupersetPredicate(v):
                return "is_superset", {"v": list(v)}
            case IsTruthyPredicate():
                return "is_truthy", None
            case JuxtPredicate(predicates=predicates, evaluate=evaluate):
                return "juxt", {"predicates": [to_json(p) for p in predicates], "evaluate": to_json(evaluate)}
            case GeLePredicate(lower, upper):
                return "ge_le", {"lower": lower, "upper": upper}
            case GeLtPredicate(lower, upper):
                return "ge_lt", {"lower": lower, "upper": upper}
            case GePredicate(v):
                return "ge", {"v": v}
            case GtLePredicate(lower, upper):
                return "gt_le", {"lower": lower, "upper": upper}
            case GtLtPredicate(lower, upper):
                return "gt_lt", {"lower": lower, "upper": upper}
            case GtPredicate(v):
                return "gt", {"v": v}
            case LePredicate(v):
                return "le", {"v": v}
            case ListOfPredicate(predicate):
                return "list_of", {"predicate": to_json(predicate)}
            case LtPredicate(v):
                return "lt", {"v": v}
            case MatchPredicate(predicates, full_match):
                return "match", {"predicates": [to_json(p) for p in predicates], "full_match": full_match}
            case NamedPredicate(name):
                return "variable", name
            case NePredicate(v):
                return "ne", {"v": v}
            case NotInPredicate(v):
                return "not_in", {"v": list(v)}
            case NotPredicate(not_predicate):
                return "not", {"predicate": to_json(not_predicate)}
            case OptionalPredicate(predicate):
                return "optional", {"predicate": to_json(predicate)}
            case OrPredicate(left, right):
                return "or", {"left": to_json(left), "right": to_json(right)}
            case RegexPredicate() as r:
                return "regex", {"pattern": r.pattern}
            case SetOfPredicate(predicate):
                return "set_of", {"predicate": to_json(predicate)}
            case TeePredicate():
                return "tee", None
            case TupleOfPredicate(predicates):
                return "tuple_of", {"predicates": [to_json(p) for p in predicates]}
            case XorPredicate(left, right):
                return "xor", {"left": to_json(left), "right": to_json(right)}
            case _:
                return "unknown", {}

    return dict([to_value(predicate)])
