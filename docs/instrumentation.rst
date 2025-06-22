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

The function max_int_with_bugs contains an annoying bug. As long as x is the largest value,
everything is fine, but if y is the maximum, then suddenly a string is returned instead of
an integer.

Looking at the specification, you first see the ``args`` keyword. This defines the predicates for the
arguments. If the arguments are annotated, a specification will be derived from that annotation.
For example 'x: int' will automatically result in is_int_p.

The next keyword is ``ret``. This specifies the predicate that the return value will be evaluated against.
In this example we define that it must be an int.

And finally the optional ``fn`` keyword defines how the input and the return value relate.

Given this example we can try:

.. code-block:: python

    result = max_int_with_bug(3, 4)

This is going to be fine since the parameters and the resulting value all satisfy the constraints.

However,

.. code-block:: python

    result = max_int_with_bug(4, 3)

Will trigger the faulty behaviour. You will probably see something like:

.. code-block::

    ValueError: Return predicate for function max_int_with_bug failed.
