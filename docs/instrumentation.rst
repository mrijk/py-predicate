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

``raises`` *(optional)*
    One exception type, or a tuple of exception types, that the function is allowed to raise.
    When the function raises an exception that matches, it propagates to the caller normally.
    When the function raises an exception that does *not* match, ``on_error`` is called and the
    unexpected exception is re-raised.

    If ``raises`` is absent and the function raises, the exception propagates unchanged — there
    is no validation.

    .. code-block:: python

        "raises": ValueError

        # or multiple types:
        "raises": (ValueError, KeyError)

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

Specifying expected exceptions
------------------------------

Use the ``raises`` key to declare which exception types a function may raise:

.. code-block:: python

    from predicate import instrument, Spec, is_int_p

    spec: Spec = {
        "args": {"n": is_int_p},
        "raises": ValueError,
    }

    @instrument(spec)
    def checked_sqrt(n: int) -> float:
        if n < 0:
            raise ValueError(f"Cannot take square root of {n}")
        return n ** 0.5

Calling with a negative number re-raises the ``ValueError`` as expected:

.. code-block:: python

    checked_sqrt(-1)  # raises ValueError: Cannot take square root of -1

If the function raises a *different* exception type, ``on_error`` is called first:

.. code-block:: python

    spec: Spec = {"args": {}, "raises": ValueError}

    @instrument(spec)
    def f() -> int:
        raise TypeError("unexpected")

    f()
    # raises ValueError: Unexpected exception TypeError for function f
    # followed by the original TypeError

To allow several exception types, pass a tuple:

.. code-block:: python

    spec: Spec = {
        "args": {"key": is_str_p},
        "raises": (KeyError, ValueError),
    }

Async support
-------------

``instrument`` and ``instrument_function`` work transparently with ``async def`` functions.
The same spec keys apply; argument checking happens before the coroutine is awaited and
return / constraint checking happens after:

.. code-block:: python

    import asyncio
    from predicate import instrument, Spec, is_int_p, ge_p

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    @instrument(spec)
    async def async_max(x: int, y: int) -> int:
        return x if x >= y else y

    result = asyncio.run(async_max(3, 7))  # returns 7

Async functions that raise are handled identically to sync functions — use the ``raises``
key in the spec to declare expected exception types:

.. code-block:: python

    spec: Spec = {
        "args": {"key": is_str_p},
        "raises": KeyError,
    }

    @instrument(spec)
    async def fetch(key: str) -> str:
        raise KeyError(key)

    asyncio.run(fetch("missing"))  # raises KeyError as expected

Instrumenting whole modules
---------------------------

``instrument_module`` applies an empty spec (derived entirely from annotations) to every
function in a module:

.. code-block:: python

    import mymodule
    from predicate import instrument_module

    instrument_module(mymodule)

An optional ``pattern`` argument (fnmatch-style) limits which functions are instrumented:

.. code-block:: python

    instrument_module(mymodule, pattern="get_*")

Custom error handling
---------------------

By default, spec violations raise ``ValueError``. Pass ``on_error`` to override:

.. code-block:: python

    import logging

    errors = []

    @instrument(on_error=errors.append)
    def add(x: int, y: int) -> int:
        return x + y

    add("oops", 1)       # on_error called, but function still runs
    print(errors)        # ['Parameter predicate for function add failed. Reason: ...']

The same ``on_error`` parameter is accepted by ``instrument_function`` and
``instrument_module``.
