import inspect
from functools import partial
from itertools import count

import graphviz  # type: ignore
from more_itertools import first

from predicate.all_predicate import AllPredicate
from predicate.always_false_predicate import AlwaysFalsePredicate
from predicate.always_true_predicate import AlwaysTruePredicate
from predicate.any_predicate import AnyPredicate
from predicate.comp_predicate import CompPredicate
from predicate.dict_of_predicate import DictOfPredicate
from predicate.eq_predicate import EqPredicate
from predicate.fn_predicate import FnPredicate
from predicate.formatter.helpers import set_to_str
from predicate.ge_predicate import GePredicate
from predicate.gt_predicate import GtPredicate
from predicate.implies import Implies
from predicate.is_falsy_predicate import IsFalsyPredicate
from predicate.is_instance_predicate import IsInstancePredicate
from predicate.is_none_predicate import IsNonePredicate
from predicate.is_truthy_predicate import IsTruthyPredicate
from predicate.lazy_predicate import LazyPredicate, find_predicate_by_ref
from predicate.le_predicate import LePredicate
from predicate.lt_predicate import LtPredicate
from predicate.named_predicate import NamedPredicate
from predicate.ne_predicate import NePredicate
from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AndPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.range_predicate import GeLePredicate, GeLtPredicate, GtLePredicate, GtLtPredicate
from predicate.root_predicate import RootPredicate, find_root_predicate
from predicate.set_predicates import (
    InPredicate,
    IsRealSubsetPredicate,
    IsRealSupersetPredicate,
    IsSubsetPredicate,
    IsSupersetPredicate,
    NotInPredicate,
)
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


def render(dot, predicate: Predicate, node_nr: count):
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
            case EqPredicate(v):
                return add_node("eq", label=f"x = {v}")
            case IsFalsyPredicate():
                return add_node("falsy", label="falsy")
            case IsTruthyPredicate():
                return add_node("truthy", label="truthy")
            case FnPredicate(predicate_fn):
                name = predicate_fn.__code__.co_name
                return add_node("fn", label=f"fn: {name}")
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
            case InPredicate(v):
                return add_node("in", label=f"x ∈ {set_to_str(v)}")
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
            case IsRealSubsetPredicate(v):
                return add_node("real_subset", label=f"x ⊂ {set_to_str(v)}")
            case IsSubsetPredicate(v):
                return add_node("subset", label=f"x ⊆ {set_to_str(v)}")
            case IsRealSupersetPredicate(v):
                return add_node("real_superset", label=f"x ⊃ {set_to_str(v)}")
            case IsSupersetPredicate(v):
                return add_node("superset", label=f"x ⊇ {set_to_str(v)}")
            case LazyPredicate(ref):
                return add_node("lazy", label=ref)
            case LePredicate(v):
                return add_node("le", label=f"x ≤ {v}")
            case LtPredicate(v):
                return add_node("lt", label=f"x < {v}")
            case NamedPredicate(name):
                return add_node("named", label=name)
            case NotInPredicate(v):
                return add_node("in", label=f"x ∉ {set_to_str(v)}")
            case NePredicate(v):
                return add_node("ne", label=f"x ≠ {v}")
            case NotPredicate(not_predicate):
                return add_node_with_child("not", label="¬", child=not_predicate)
            case OrPredicate(left, right):
                return add_node_left_right("or", label="∨", left=left, right=right)
            case RootPredicate():
                return add_node("root", label="root")
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
