![Documentation](https://github.com/mrijk/py-predicate/actions/workflows/pages.yaml/badge.svg)
![Test](https://github.com/mrijk/py-predicate/actions/workflows/test.yaml/badge.svg)
[![codecov](https://codecov.io/gh/mrijk/py-predicate/graph/badge.svg?token=KMBDJNC3W9)](https://codecov.io/gh/mrijk/py-predicate)

# Introduction

py-predicate is a typed Python library to create composable predicates.

# Getting started

To get started, install the library with [pip](https://pip.pypa.io/en/stable/)

```
pip install py-predicate
```

The full documentation can be found [here](https://mrijk.github.io/py-predicate/). We give 2 small examples
to show what the library can do.

# Example 1

```python
filtered = [x for x in range(10) if x >= 2 and x <= 3]
```

## Version with predicates:

```python
from predicate import ge_p, le_p

ge_2 = ge_p(2)
le_3 = le_p(3)

between_2_and_3 = ge_2 & le_3
filtered = [x for x in range(10) if between_2_and_3(x)]
```

Of course this example looks way more complicated than the original version. The point here is that you can build
reusable predicates that can be used in multiple locations.

# Example 2

A unique (?) py-predicate feature is that you can define self referencing predicates.
This makes it easy to apply predicates to arbitrarily nested structures, like JSON data.

In the next example we define a predicate, that tests if a given data structure is
either a string, or a list of data that can again either be a string or a list of
data. Ad infinitum.

```python
from predicate import all_p, is_list_p, is_str_p, lazy_p

str_or_list_of_str = is_str_p | (is_list_p & all_p(lazy_p("str_or_list_of_str")))
```

Using plain Python, the above one-liner would have to be coded as a (recursive) function.
