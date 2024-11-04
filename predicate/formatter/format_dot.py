from itertools import count

import graphviz  # type: ignore

from predicate import (
    AllPredicate,
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    AnyPredicate,
    EqPredicate,
    FnPredicate,
    GePredicate,
    GtPredicate,
    InPredicate,
    LePredicate,
    LtPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)
from predicate.optimizer.predicate_optimizer import optimize


def to_dot(predicate: Predicate, predicate_string: str = "", show_optimized: bool = False):
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
    def add_node(name: str, *, label: str):
        node = next(node_nr)
        unique_name = f"{name}_{node}"
        dot.node(unique_name, label=label)
        return unique_name

    def to_value(predicate: Predicate):
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
            case EqPredicate(v):
                return add_node("eq", label=f"x = {v}")
            case FnPredicate(predicate_fn):
                name = predicate_fn.__code__.co_name
                # code = inspect.getsource(predicate_fn)
                # m = re.match(r".*\(predicate_fn=(.*)\)", code)
                return add_node("fn", label=f"fn: {name}")
            case GePredicate(v):
                return add_node("ge", label=f"x ≥ {v}")
            case GtPredicate(v):
                return add_node("gt", label=f"x > {v}")
            case InPredicate(v):
                items = ", ".join(str(item) for item in v)
                return add_node("in", label=f"x ∈ {{{items}}}")
            case LePredicate(v):
                return add_node("le", label=f"x ≤ {v}")
            case LtPredicate(v):
                return add_node("lt", label=f"x < {v}")
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
