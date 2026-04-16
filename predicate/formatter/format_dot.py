import inspect
from functools import partial
from itertools import count
from types import UnionType
from typing import Iterable, get_args

import graphviz  # type: ignore
from graphviz import Digraph
from more_itertools import first

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.comp_predicate import CompPredicate
from predicate.compile_predicate import CompiledPredicate
from predicate.count_predicate import CountPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.exactly_predicate import ExactlyPredicate
from predicate.fn_predicate import FnPredicate
from predicate.formatter.helpers import set_to_str
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.has_key_predicate import HasKeyPredicate
from predicate.has_length_predicate import HasLengthPredicate
from predicate.has_path_predicate import HasPathPredicate
from predicate.implies import Implies
from predicate.in_predicate import InPredicate
from predicate.is_close_predicate import IsClosePredicate
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_not_none_predicate import IsNotNonePredicate
from predicate.is_same_predicate import IsSamePredicate
from predicate.is_subclass_predicate import IsSubclassPredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.juxt_predicate import JuxtPredicate
from predicate.lazy_predicate import LazyPredicate, find_predicate_by_ref
from predicate.le_predicate import LePredicate
from predicate.list_of_predicate import ListOfPredicate
from predicate.lt_predicate import LtPredicate
from predicate.match_predicate import MatchPredicate
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import NePredicate
from predicate.not_in_predicate import NotInPredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.optional_predicate import OptionalPredicate
from predicate.plus_predicate import PlusPredicate
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.reduce_predicate import ReducePredicate
from predicate.regex_predicate import RegexPredicate
from predicate.repeat_predicate import RepeatPredicate
from predicate.root_predicate import RootPredicate, find_root_predicate
from predicate.set_of_predicate import SetOfPredicate
from predicate.set_predicates import (
    IntersectsPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
)
from predicate.star_predicate import StarPredicate
from predicate.tee_predicate import TeePredicate
from predicate.this_predicate import ThisPredicate, find_this_predicate
from predicate.tuple_of_predicate import TupleOfPredicate


def to_dot(predicate: Predicate, predicate_string: str | None = None, show_optimized: bool = False):
    """Format predicate as a .dot file."""
    label = predicate_string if predicate_string else repr(predicate)

    graph_attr = {"label": label, "labelloc": "t"}

    node_attr = {"shape": "rectangle", "style": "filled", "fillcolor": "#B7D7A8"}

    edge_attr: dict = {}

    dot = graphviz.Digraph(graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr)

    node_nr = count()

    render_original(dot, predicate, node_nr)

    if show_optimized:
        render_optimized(dot, predicate, node_nr)

    return dot


def render(dot: Digraph, predicate: Predicate, node_nr: count):
    node_predicate_mapping: dict[str, Predicate] = {}

    def _add_node(name: str, *, label: str, predicate: Predicate | None) -> str:
        node = next(node_nr)
        unique_name = f"{name}_{node}"
        dot.node(unique_name, label=label)
        if predicate:
            node_predicate_mapping[unique_name] = predicate
        return unique_name

    def _add_node_left_right(name: str, *, label: str, predicate: Predicate, left: Predicate, right: Predicate) -> str:
        node = _add_node(name, label=label, predicate=predicate)
        dot.edge(node, to_value(left))
        dot.edge(node, to_value(right))

        return node

    def _add_node_with_child(name: str, *, label: str, predicate: Predicate, child: Predicate) -> str:
        node = _add_node(name, label=label, predicate=predicate)
        dot.edge(node, to_value(child))
        return node

    def to_value(predicate: Predicate):
        add_node = partial(_add_node, predicate=predicate)
        add_node_left_right = partial(_add_node_left_right, predicate=predicate)
        add_node_with_child = partial(_add_node_with_child, predicate=predicate)

        match predicate:
            case CompiledPredicate(predicate=inner):
                return to_value(inner)
            case AllPredicate(all_predicate):
                return add_node_with_child("all", label="∀", child=all_predicate)
            case AlwaysFalsePredicate():
                return add_node("F", label="false")
            case AlwaysTruePredicate():
                return add_node("T", label="true")
            case AndPredicate(left, right):
                return add_node_left_right("and", label="∧", left=left, right=right)
            case AnyPredicate(any_predicate):
                return add_node_with_child("any", label="∃", child=any_predicate)
            case CompPredicate(_fn, comp_predicate):
                return add_node_with_child("comp", label="f", child=comp_predicate)
            case CountPredicate(predicate, length_p):
                node = add_node("count", label="count")
                dot.edge(node, to_value(predicate), label="predicate")
                dot.edge(node, to_value(length_p), label="length")
                return node
            case EqPredicate(v):
                return add_node("eq", label=f"x = {v}")
            case ExactlyPredicate(n, predicate):
                return add_node_with_child("exactly", label=f"exactly {n}", child=predicate)
            case IsFalsyPredicate():
                return add_node("falsy", label="falsy")
            case IsTruthyPredicate():
                return add_node("truthy", label="truthy")
            case FnPredicate(predicate_fn):
                name = predicate_fn.__code__.co_name
                return add_node("fn", label=f"fn: {name}")
            case HasKeyPredicate(key):
                return add_node("has_key", label=f"has_key: {key!r}")
            case HasLengthPredicate(length_p):
                return add_node_with_child("has_length", label="has_length", child=length_p)
            case HasPathPredicate(path):
                node = add_node("has_path", label="has_path")
                for step in path:
                    dot.edge(node, to_value(step))
                return node
            case GePredicate(v):
                return add_node("ge", label=f"x ≥ {v}")
            case GeLePredicate(upper, lower):
                return add_node("gele", label=f"{lower} ≤ x ≤ {upper}")
            case GeLtPredicate(upper, lower):
                return add_node("gelt", label=f"{lower} ≤ x < {upper}")
            case GtPredicate(v):
                return add_node("gt", label=f"x > {v}")
            case GtLePredicate(upper, lower):
                return add_node("gtle", label=f"{lower} ≤ x ≤ {upper}")
            case GtLtPredicate(upper, lower):
                return add_node("gtlt", label=f"{lower} ≤ x < {upper}")
            case InPredicate(v) if isinstance(v, Iterable):
                return add_node("in", label=f"x ∈ {set_to_str(v)}")
            case IntersectsPredicate(v):
                return add_node("intersects", label=f"x ∩ {set_to_str(v)} ≠ ∅")
            case IsClosePredicate(target, rel_tol, abs_tol):
                return add_node("is_close", label=f"x ≈ {target!r}\nrel={rel_tol}, abs={abs_tol}")
            case DictOfPredicate(key_value_predicates):
                node = add_node("dict_of", label="is_dict_of")
                for key, value in key_value_predicates:
                    kv = _add_node("kv", label="kv", predicate=None)
                    dot.edge(node, kv)
                    dot.edge(kv, to_value(key), label="key")
                    dot.edge(kv, to_value(value), label="value")
                return node
            case Implies(left, right):
                return add_node_left_right("implies", label="=>", left=left, right=right)
            case IsInstancePredicate(klass):
                name = klass[0].__name__  # type: ignore
                return add_node("instance", label=f"is_{name}_p")
            case IsNonePredicate():
                return add_node("none", label="x = None")
            case IsNotNonePredicate():
                return add_node("not_none", label="x ≠ None")
            case IsSamePredicate(predicate):
                return add_node_with_child("is_same", label="is_same", child=predicate)
            case IsSubclassPredicate(class_or_tuple):
                if isinstance(class_or_tuple, tuple):
                    names = ", ".join(k.__name__ for k in class_or_tuple)
                elif isinstance(class_or_tuple, UnionType):
                    names = ", ".join(k.__name__ for k in get_args(class_or_tuple))
                else:
                    names = class_or_tuple.__name__
                return add_node("is_subclass", label=f"subclass of {names}")
            case IsRealSubsetPredicate(v):
                return add_node("real_subset", label=f"x ⊂ {set_to_str(v)}")
            case IsSubsetPredicate(v):
                return add_node("subset", label=f"x ⊆ {set_to_str(v)}")
            case IsRealSupersetPredicate(v):
                return add_node("real_superset", label=f"x ⊃ {set_to_str(v)}")
            case IsSupersetPredicate(v):
                return add_node("superset", label=f"x ⊇ {set_to_str(v)}")
            case JuxtPredicate(predicates=predicates, evaluate=evaluate):
                graph_attr = {"label": "juxt", "color": "blue", "style": "filled", "fillcolor": "lightblue"}
                with dot.subgraph(name="cluster_0", graph_attr=graph_attr) as graph:
                    for predicate in predicates:
                        node = next(node_nr)
                        name = "repr_p"
                        unique_name = f"{name}_{node}"
                        graph.node(unique_name, label=repr(predicate))
                        graph.edge(unique_name, "evaluate")
                    graph.node("evaluate", label=repr(evaluate))
                    return None
            case LazyPredicate(ref):
                return add_node("lazy", label=ref)
            case LePredicate(v):
                return add_node("le", label=f"x ≤ {v}")
            case ListOfPredicate(predicate):
                return add_node_with_child("list_of", label="is_list_of", child=predicate)
            case LtPredicate(v):
                return add_node("lt", label=f"x < {v}")
            case MatchPredicate(predicates):
                node = add_node("match", label="match")
                for match_predicate in predicates:
                    dot.edge(node, to_value(match_predicate))
                return node
            case NamedPredicate(name):
                return add_node("named", label=name)
            case NotInPredicate(v) if isinstance(v, Iterable):
                return add_node("in", label=f"x ∉ {set_to_str(v)}")
            case NePredicate(v):
                return add_node("ne", label=f"x ≠ {v}")
            case OptionalPredicate(predicate):
                return add_node_with_child("optional", label="?", child=predicate)
            case PlusPredicate(predicate):
                return add_node_with_child("plus", label="+", child=predicate)
            case NotPredicate(not_predicate):
                return add_node_with_child("not", label="¬", child=not_predicate)
            case OrPredicate(left, right):
                return add_node_left_right("or", label="∨", left=left, right=right)
            case ReducePredicate(fn, initial):
                name = getattr(fn, "__name__", str(fn))
                return add_node("reduce", label=f"reduce({name}, {initial!r})")
            case RegexPredicate() as r:
                return add_node("regex", label=f"~/{r.pattern}/")
            case RepeatPredicate(m, n, predicate):
                return add_node_with_child("repeat", label=f"{{{m},{n}}}", child=predicate)
            case RootPredicate():
                return add_node("root", label="root")
            case SetOfPredicate(predicate):
                return add_node_with_child("set_of", label="is_set_of", child=predicate)
            case StarPredicate(predicate):
                return add_node_with_child("star", label="*", child=predicate)
            case TeePredicate():
                return add_node("tee", label="tee")
            case ThisPredicate():
                return add_node("this", label="this")
            case TupleOfPredicate(predicates):
                node = add_node("tuple_of", label="is_tuple_of")
                for tuple_predicate in predicates:
                    dot.edge(node, to_value(tuple_predicate))
                return node
            case XorPredicate(left, right):
                return add_node_left_right("xor", label="⊻", left=left, right=right)
            case _:
                raise ValueError(f"Unknown predicate type {predicate}")

    to_value(predicate)

    render_lazy_references(dot, node_predicate_mapping)


def render_lazy_references(dot, node_predicate_mapping) -> None:
    def find_in_mapping(lookup: Predicate) -> str:
        return first(node for node, predicate in node_predicate_mapping.items() if predicate == lookup)

    def add_dashed_line(node: str, lookup: Predicate) -> None:
        found = find_in_mapping(lookup)
        dot.edge(node, found, style="dashed")

    frame = inspect.currentframe()

    for node, predicate in node_predicate_mapping.items():
        match predicate:
            case LazyPredicate() if reference := find_predicate_by_ref(frame, predicate.ref):
                add_dashed_line(node, reference)
            case RootPredicate() if root := find_root_predicate(frame, predicate):
                add_dashed_line(node, root)
            case ThisPredicate() if this := find_this_predicate(frame, predicate):
                add_dashed_line(node, this)


def render_original(dot, predicate: Predicate, node_nr) -> None:
    with dot.subgraph(name="cluster_original") as original:
        original.attr(style="filled", color="lightgrey")
        original.attr(label="Original predicate")
        render(original, predicate, node_nr)


def render_optimized(dot, predicate: Predicate, node_nr) -> None:
    optimized_predicate = optimize(predicate)

    with dot.subgraph(name="cluster_optimized") as optimized:
        optimized.attr(style="filled", color="lightgrey")
        optimized.attr(label="Optimized predicate")
        render(optimized, optimized_predicate, node_nr)
