import inspect
from functools import partial
from itertools import count

import graphviz  # type: ignore
from more_itertools import first

from predicate.comp_predicate import CompPredicate
from predicate.lazy_predicate import LazyPredicate, find_predicate_by_ref
from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    IsFalsyPredicate,
    IsTruthyPredicate,
    NamedPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.root_predicate import RootPredicate, find_root_predicate
from predicate.standard_predicates import (
    AllPredicate,
    AnyPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    IsInstancePredicate,
    IsNonePredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    PredicateFactory,
)
from predicate.this_predicate import ThisPredicate, find_this_predicate


def to_dot(predicate: Predicate, predicate_string: str = "", show_optimized: bool = False):
    """Format predicate as a .dot file."""
    graph_attr = {"label": predicate_string, "labelloc": "t"}

    node_attr = {"shape": "rectangle", "style": "filled", "fillcolor": "#B7D7A8"}

    edge_attr: dict = {}

    dot = graphviz.Digraph(graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr)

    node_nr = count()

    render_original(dot, predicate, node_nr)

    if show_optimized:
        render_optimized(dot, predicate, node_nr)

    return dot


def render(dot, predicate: Predicate, node_nr):
    node_predicate_mapping: dict[str, Predicate] = {}

    def _add_node(name: str, *, label: str, predicate: Predicate):
        node = next(node_nr)
        unique_name = f"{name}_{node}"
        dot.node(unique_name, label=label)
        node_predicate_mapping[unique_name] = predicate
        return unique_name

    def to_value(predicate: Predicate):
        add_node = partial(_add_node, predicate=predicate)

        match predicate:
            case AllPredicate(all_predicate):
                node = add_node("all", label="∀")
                child = to_value(all_predicate)
                dot.edge(node, child)
                return node
            case AlwaysFalsePredicate():
                return add_node("F", label="false")
            case AlwaysTruePredicate():
                return add_node("T", label="true")
            case AndPredicate(left, right):
                node = add_node("and", label="∧")
                left_node = to_value(left)
                right_node = to_value(right)
                dot.edge(node, left_node)
                dot.edge(node, right_node)
                return node
            case AnyPredicate(any_predicate):
                node = add_node("any", label="∃")
                child = to_value(any_predicate)
                dot.edge(node, child)
                return node
            case CompPredicate(_fn, comp_predicate):
                node = add_node("comp", label="f")
                child = to_value(comp_predicate)
                dot.edge(node, child)
                return node
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
            case GtPredicate(v):
                return add_node("gt", label=f"x > {v}")
            case InPredicate(v):
                items = ", ".join(str(item) for item in v)
                return add_node("in", label=f"x ∈ {{{items}}}")
            case IsInstancePredicate(klass):
                name = klass[0].__name__  # type: ignore
                return add_node("instance", label=f"is_{name}_p")
            case IsNonePredicate():
                return add_node("none", label="x = None")
            case LazyPredicate(ref):
                return add_node("lazy", label=ref)
            case LePredicate(v):
                return add_node("le", label=f"x ≤ {v}")
            case LtPredicate(v):
                return add_node("lt", label=f"x < {v}")
            case NamedPredicate(name):
                return add_node("named", label=name)
            case NotInPredicate(v):
                items = ", ".join(str(item) for item in v)
                return add_node("in", label=f"x ∉ {{{items}}}")
            case NePredicate(v):
                return add_node("ne", label=f"x ≠ {v}")
            case NotPredicate(not_predicate):
                child = to_value(not_predicate)
                node = add_node("not", label="¬")
                dot.edge(node, child)
                return node
            case OrPredicate(left, right):
                node = add_node("or", label="∨")
                left_node = to_value(left)
                right_node = to_value(right)
                dot.edge(node, left_node)
                dot.edge(node, right_node)
                return node
            case PredicateFactory() as factory:
                return to_value(factory.predicate)
            case RootPredicate():
                return add_node("root", label="root")
            case ThisPredicate():
                return add_node("this", label="this")
            case XorPredicate(left, right):
                node = add_node("xor", label="⊻")
                left_node = to_value(left)
                right_node = to_value(right)
                dot.edge(node, left_node)
                dot.edge(node, right_node)
                return node
            case _:
                raise ValueError(f"Unknown predicate type {predicate}")

    to_value(predicate)

    render_lazy_references(dot, node_predicate_mapping)


def render_lazy_references(dot, node_predicate_mapping):
    def find_in_mapping(lookup: Predicate) -> str:
        return first(node for node, predicate in node_predicate_mapping.items() if predicate == lookup)

    def add_dashed_line(node: str, lookup: Predicate) -> None:
        found = find_in_mapping(lookup)
        dot.edge(node, found, style="dashed")

    frame = inspect.currentframe()

    for node, predicate in node_predicate_mapping.items():
        match predicate:
            case LazyPredicate():
                if reference := find_predicate_by_ref(frame, predicate.ref):
                    add_dashed_line(node, reference)
            case RootPredicate():
                if root := find_root_predicate(frame, predicate):
                    add_dashed_line(node, root)
            case ThisPredicate():
                if this := find_this_predicate(frame, predicate):
                    add_dashed_line(node, this)


def render_original(dot, predicate: Predicate, node_nr):
    with dot.subgraph(name="cluster_original") as original:
        original.attr(style="filled", color="lightgrey")
        original.attr(label="Original predicate")
        render(original, predicate, node_nr)


def render_optimized(dot, predicate: Predicate, node_nr):
    optimized_predicate = optimize(predicate)

    with dot.subgraph(name="cluster_optimized") as optimized:
        optimized.attr(style="filled", color="lightgrey")
        optimized.attr(label="Optimized predicate")
        render(optimized, optimized_predicate, node_nr)
