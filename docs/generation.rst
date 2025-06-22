Generation
==========

Given a predicate, py-predicate is able to generate sample data that satisfy that predicate:

NOTE: some generators might still be missing.

generate_true
-------------
This function returns an (potentially infinite, and potentially empty) iterable of values that satisfy the given
predicate. Use `take <https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.take>`_
from `More Itertools <https://more-itertools.readthedocs.io/>`_ to limit the number of return values.

.. code-block:: python

    from predicate import generate_true, is_int_p
    from more_itertools import take

    take(5, generate_true(is_int_p))

In this example we generate 5 values, that will result in True for this predicate.

generate_false
--------------
This function returns an (potentially infinite, and potentially empty) iterable of values that don't satisfy the given
predicate.

.. code-block:: python

    from predicate import generate_false, is_int_p
    from more_itertools import take

    take(5, generate_false(is_int_p))

In this example we generate 5 values, that will result in False for this predicate. Note that these
values can be anything (strings, floats, dicts, etc.)
