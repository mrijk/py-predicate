Instrumentation
===============

This is a powerful feature that allows you to do a run-time check on any given function.

Easiest way to explain this is by example.

.. code-block:: python

    from predicate import instrument_function, Spec, is_int_p


    def max_int_with_bug(x, y):
        return x if x > y else f"{y}"


    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    instrument_function(max_int_with_bug, spec=spec)

The function ``max_int_with_bug`` contains an annoying bug. As long as ``x`` is the largest value,
everything is fine, but if ``y`` is the maximum, then suddenly a string is returned instead of
an integer.

Spec keys
---------

``args``
    Predicates for each parameter. If the argument is annotated, a predicate will be derived
    automatically from the annotation — for example ``x: int`` becomes ``is_int_p``.

``ret`` *(optional)*
    Predicate that the return value is evaluated against. Omit if you only want to constrain
    arguments or the relationship between inputs and output.

``fn`` *(optional)*
    A callable that receives all arguments plus ``ret`` as keyword arguments and returns a
    ``bool``. Use this to express how inputs and the return value relate to each other.

    .. code-block:: python

        "fn": lambda x, y, ret: ret >= x and ret >= y

``fn_p`` *(optional)*
    A callable that receives the arguments and returns a ``Predicate`` which is then applied to
    the return value. Use this when the expected return predicate depends on the input values.

    .. code-block:: python

        "fn_p": lambda x, y: ge_p(x + y)

Using the decorator
-------------------

As an alternative to ``instrument_function``, the ``instrument`` decorator applies a spec
directly to a function definition:

.. code-block:: python

    from predicate import instrument, Spec, is_int_p

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    @instrument(spec)
    def max_int(x: int, y: int) -> int:
        return x if x >= y else y

Both forms are equivalent.

Examples
--------

Given the instrumented ``max_int_with_bug``, calling it with valid inputs:

.. code-block:: python

    result = max_int_with_bug(3, 4)

is fine — the parameters and return value all satisfy the spec.

However:

.. code-block:: python

    result = max_int_with_bug(4, 3)

triggers the bug and raises:

.. code-block::

    ValueError: Return predicate for function max_int_with_bug failed. Reason: 3 is not an instance of type int

Passing a wrong argument type:

.. code-block:: python

    result = max_int_with_bug(4, False)

raises:

.. code-block::

    ValueError: Parameter predicate for function max_int_with_bug failed. Reason: False is not an instance of type int

Note that argument predicates are checked *before* the function executes, so no side effects
occur when an argument is invalid.
