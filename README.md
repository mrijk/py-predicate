![Documentation](https://github.com/mrijk/py-predicate/actions/workflows/pages.yaml/badge.svg)
![Test](https://github.com/mrijk/py-predicate/actions/workflows/test.yaml/badge.svg)
[![codecov](https://codecov.io/gh/mrijk/py-predicate/graph/badge.svg?token=KMBDJNC3W9)](https://codecov.io/gh/mrijk/py-predicate)

# py-predicate

A typed Python library for composable predicates.

Predicates are first-class objects that can be combined with boolean operators, optimized algebraically, compiled to native callables for performance, serialized to multiple formats, and used to instrument functions with runtime contracts.

Full documentation: [mrijk.github.io/py-predicate](https://mrijk.github.io/py-predicate/)

## Installation

```bash
pip install py-predicate
```

## Quick start

```python
from predicate import ge_p, le_p

ge_2 = ge_p(2)
le_5 = le_p(5)

between = ge_2 & le_5

between(3)   # True
between(7)   # False

filtered = [x for x in range(10) if between(x)]  # [2, 3, 4, 5]
```

Predicates compose with standard Python operators:

| Operator | Meaning |
|----------|---------|
| `p & q`  | both must hold (`AndPredicate`) |
| `p \| q` | either must hold (`OrPredicate`) |
| `p ^ q`  | exactly one must hold (`XorPredicate`) |
| `~p`     | negation (`NotPredicate`) |

## Built-in predicates

**Comparisons:** `eq_p`, `ne_p`, `gt_p`, `ge_p`, `lt_p`, `le_p`, `is_close_p`

**Ranges:** `ge_le_p`, `ge_lt_p`, `gt_le_p`, `gt_lt_p` (compiled to chained comparisons)

**Type checks:** `is_int_p`, `is_str_p`, `is_float_p`, `is_bool_p`, `is_list_p`, `is_dict_p`, `is_none_p`, `is_not_none_p`, `is_instance_p`, and many more

**Collections:** `all_p`, `any_p`, `in_p`, `not_in_p`, `has_length_p`, `is_empty_p`, `is_not_empty_p`, `has_key_p`, `has_path_p`

**Typed collections:** `is_list_of_p`, `is_set_of_p`, `is_dict_of_p`, `is_tuple_of_p`

**Strings:** `regex_p`, `starts_with_p`, `ends_with_p`, `is_alpha_p`, `is_digit_p`, `is_upper_p`, `is_lower_p`, and more

**Logic:** `always_p`, `never_p`, `implies_p`, `fn_p`

**Numeric:** `is_even_p`, `is_odd_p`, `is_nan_p`, `is_inf_p`, `is_finite_p`, `pos_p`, `neg_p`, `zero_p`

## Failure explanation

Use `explain` to get a structured description of why a predicate failed:

```python
from predicate import explain, ge_p, le_p

between = ge_p(2) & le_p(5)
explain(between, 8)
# {'reason': 'Right predicate failed', 'right': {'reason': 'Expected 8 <= 5'}}
```

## Optimizer

Predicate trees can be algebraically simplified:

```python
from predicate import ge_p, le_p, optimize, can_optimize

p = ge_p(2) & le_p(5)
can_optimize(p)   # True (may simplify to a range predicate, etc.)
optimized = optimize(p)
```

The optimizer handles identities like `p & always_true == p`, `p | always_true == always_true`, double-negation elimination, De Morgan's laws, and more.

## Compile to native callables

`compile_predicate` translates a predicate tree into a native Python lambda via AST generation, removing interpreter overhead on hot paths:

```python
from predicate import compile_predicate, ge_p, le_p

between = ge_p(2) & le_p(5)
fast = compile_predicate(between)  # returns a CompiledPredicate

fast(3)   # True  — evaluated by a native lambda: lambda x: x >= 2 and x <= 5
fast(8)   # False

# Introspection is preserved
repr(fast)            # same as repr(between)
fast.explain_failure  # delegates to the original predicate
```

Use `try_compile_predicate` to fall back to the original when compilation is not supported (e.g. `fn_p`, `regex_p`):

```python
from predicate import try_compile_predicate

safe = try_compile_predicate(some_predicate)  # always returns a callable
```

## Value generation

Predicates can drive property-based testing by generating values that satisfy or violate them:

```python
from predicate import generate_true, generate_false, ge_p, le_p
from more_itertools import take

between = ge_p(2) & le_p(5)

take(5, generate_true(between))   # e.g. [2, 3, 4, 5, 2]
take(5, generate_false(between))  # e.g. [0, 1, 6, 7, -1]
```

## Recursive predicates

Use `root_p` (or `this_p`) to define self-referencing predicates over arbitrarily nested structures without writing recursive functions:

```python
from predicate import all_p, is_list_p, is_str_p, root_p

# Matches a string, or a list of strings/lists (recursively)
str_or_nested = is_str_p | (is_list_p & all_p(root_p))

str_or_nested("hello")            # True
str_or_nested(["a", ["b", "c"]]) # True
str_or_nested(["a", 1])          # False
```

For mutually recursive predicates, use `mutual_recur_p`.

## Runtime instrumentation (Spec)

Instrument functions with predicate-based contracts that are checked at call time:

```python
from predicate import ge_p, instrument, is_int_p, is_str_p, le_p

@instrument({"args": {"x": is_int_p & ge_p(0) & le_p(100)}, "ret": is_str_p})
def grade(x: int) -> str:
    return "pass" if x >= 50 else "fail"

grade(75)   # "pass"
grade(-1)   # raises ValueError: Parameter predicate for function grade failed
```

You can also instrument all functions in a module or class:

```python
from predicate import instrument_module, instrument_class

instrument_module(my_module)
instrument_class(MyClass)
```

Specs can include cross-argument constraints via `fn` or `fn_p` keys, and expected exception types via `raises`.

## Analysis

Check logical properties of predicates:

```python
from predicate import are_equivalent, is_satisfiable, is_tautology, ge_p, le_p, always_p

is_tautology(always_p)               # True
is_satisfiable(ge_p(5) & le_p(3))   # False (unsatisfiable)
are_equivalent(~~ge_p(2), ge_p(2))  # True
```

## Serialization

Export predicates to multiple formats:

```python
from predicate import ge_p, le_p, to_json, to_yaml, to_dot, to_latex

p = ge_p(2) & le_p(5)

to_json(p)   # JSON string
to_yaml(p)   # YAML string
to_dot(p)    # Graphviz DOT for visualization
to_latex(p)  # LaTeX expression
```

Deserialize from JSON:

```python
from predicate.formatter.from_json import from_json

p = from_json('{"and": [{"ge": 2}, {"le": 5}]}')
```
