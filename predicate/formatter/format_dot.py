from itertools import count

import graphviz  # type: ignore

from predicate.optimizer.predicate_optimizer import optimize
from predicate.predicate import (
    AlwaysFalsePredicate,
    AlwaysTruePredicate,
    AndPredicate,
    EqPredicate,
    InPredicate,
    NePredicate,
    NotInPredicate,
    NotPredicate,
    OrPredicate,
    Predicate,
    XorPredicate,
)


def to_dot(predicate: Predicate, predicate_string: str, show_optimized: bool = False):
    dot = graphviz.Digraph(graph_attr={"label": predicate_string, "labelloc": "t"}, node_attr={"shape": "rectangle"})

    node_nr = count()

    render_original(dot, predicate, node_nr)

    if show_optimized:
        render_optimized(dot, predicate, node_nr)

    return dot


def render(dot, predicate: Predicate, node_nr):
    def add_node(name: str, label: str):
        node = next(node_nr)
        unique_name = f"{name}_{node}"
        dot.node(unique_name, label)
        return unique_name

    def to_value(predicate: Predicate):
        match predicate:
            case AlwaysFalsePredicate():
                return add_node("F", label="False")
            case AlwaysTruePredicate():
                return add_node("T", label="True")
            case AndPredicate(left, right):
                left_node = to_value(left)
                right_node = to_value(right)
                node = add_node("and", label="&")
                dot.edge(node, left_node)
                dot.edge(node, right_node)
                return node
            case EqPredicate(v):
                return add_node("eq", label=f"x = {v}")
            case InPredicate(v):
                items = ", ".join(str(item) for item in v)
                return add_node("in", label=f"x ∈ {{{items}}}")
            case NotInPredicate(v):
                items = ", ".join(str(item) for item in v)
                return add_node("in", label=f"x ∉ {{{items}}}")
            case NePredicate(v):
                return add_node("ne", label=f"x ≠ {v}")
            case NotPredicate(not_predicate):
                child = to_value(not_predicate)
                node = add_node("not", label="~")
                dot.edge(node, child)
                return node
            case OrPredicate(left, right):
                left_node = to_value(left)
                right_node = to_value(right)
                node = add_node("or", label="|")
                dot.edge(node, left_node)
                dot.edge(node, right_node)
                return node
            case XorPredicate(left, right):
                left_node = to_value(left)
                right_node = to_value(right)
                node = add_node("xor", label="^")
                dot.edge(node, left_node)
                dot.edge(node, right_node)
                return node

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
