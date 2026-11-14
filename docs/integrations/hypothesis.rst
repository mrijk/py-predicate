Hypothesis
----------

`Hypothesis <https://hypothesis.readthedocs.io>`_ generates test inputs from *strategies*. A predicate is a data
structure, not an opaque function, so py-predicate can turn it into a strategy that generates values satisfying it,
including the arguments of a function described by a :doc:`Spec <instrumentation>`. Install the optional dependency
first:

.. code-block:: bash

    pip install py_predicate[hypothesis]

Everything is importable from ``predicate.hypothesis``, which is a short alias for
``predicate.integrations.hypothesis``.

Strategies from predicates
^^^^^^^^^^^^^^^^^^^^^^^^^^

``from_predicate`` returns a regular Hypothesis strategy, so it can be used with ``@given``, ``st.lists`` and the
rest. ``given_predicate`` is a shortcut for ``@given`` that takes predicates instead of strategies, positionally or
by keyword:

.. code-block:: python

    from hypothesis import given

    from predicate import ge_le_p, ge_p, is_list_of_p, lt_p
    from predicate.hypothesis import from_predicate, given_predicate


    @given_predicate(ge_p(0) & lt_p(100))
    def test_range(x):
        assert 0 <= x < 100


    @given_predicate(x=ge_p(0), y=lt_p(0))
    def test_signs(x, y):
        assert x >= 0 > y


    @given(from_predicate(is_list_of_p(ge_le_p(1, 6))))
    def test_dice(rolls):
        assert all(1 <= roll <= 6 for roll in rolls)

``from_predicate_false`` is the opposite: it generates values that do *not* satisfy the predicate, which is handy for
testing that invalid input is rejected. It is ``from_predicate(~predicate)``, so it supports the same predicates, for
example ``from_predicate_false(ge_p(0))`` generates negative numbers. Negating ``is_list_of_p`` isn't supported yet.

``given_predicate`` returns a real ``hypothesis.given`` decorator, so ``@settings``, ``@example`` and pytest fixtures
work as usual. It doesn't mix plain strategies and predicates in one call.

How predicates are translated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==============================================================  ============================================================
Predicate                                                       Strategy
==============================================================  ============================================================
``eq_p``                                                        ``st.just``
``in_p``                                                        ``st.sampled_from``
``ge_p``, ``gt_p``, ``le_p``, ``lt_p``, ``ge_le_p``, ...        ``st.integers`` or ``st.floats``, the bounds of an ``&``
                                                                chain are merged into one strategy
``p | q``                                                       ``st.one_of``
``p & q``                                                       bounds merged, any other operand applied as a filter
``~p``                                                          the negation is pushed inwards (De Morgan, ``ge_p``
                                                                becomes ``lt_p``, ...), otherwise generate and filter
``p ^ q``                                                       rewritten to ``(p & ~q) | (~p & q)``
``is_none_p``                                                   ``st.none``
``is_not_none_p``, ``is_truthy_p``, ``always_true_p``           arbitrary objects, filtered by the predicate
``is_falsy_p``                                                  a mix of falsy values: ``None``, ``0``, ``""``, empty
                                                                collections, ...
``always_false_p``                                              ``st.nothing``, so no values are generated
``is_alpha_p``, ``is_digit_p``, ``is_upper_p``, ...             ``st.text`` over the matching Unicode categories, for
                                                                example letters for ``is_alpha_p``
``starts_with_p``, ``ends_with_p``                              ``st.text`` with the prefix or suffix added
``regex_p``                                                     ``st.from_regex``, generating strings that match fully
``is_regex_p``                                                  ``st.text``, filtered for valid regular expressions
``is_subset_p``, ``is_superset_p``, ``intersects_p``, ...       ``st.sets`` of elements of the given set, plus extra elements
                                                                of the same type for supersets
``has_length_p``, ``is_empty_p``, ``is_not_empty_p``            a list of ints whose length satisfies the length predicate
                                                                (lengths up to 100)
``has_key_p``                                                   a dict with a key satisfying the key predicate, plus other
                                                                keys of the same type
``is_even_p``, ``is_odd_p``                                     ``st.integers``, mapped to even or odd numbers
``is_finite_p``, ``is_inf_p``, ``is_nan_p``, ``is_normal_p``    ``st.floats`` with matching flags, or the infinities and NaN
``is_subclass_p``, ``is_enum_p``, ``is_int_enum_p``, ...        ``st.sampled_from`` the class and its subclasses that are
                                                                loaded at that moment
``is_same_p``                                                   ``st.just`` of the given predicate
``count_p``, ``exactly_one_p``, ``exactly_zero_p``              a shuffled list with a number of matching elements that
                                                                satisfies the count predicate (up to 10), plus others
``recur_p``, ``mutual_recur_p``                                 a chain of 1 to 5 elements, each drawn from the predicate
                                                                of the one before; starts from an int or a str
``is_int_p``, ``is_str_p``, ... (``is_instance_p``)             ``st.from_type``
``all_p``, ``is_list_of_p``                                     ``st.lists``
``any_p``                                                       ``st.lists`` with at least one item
``is_set_of_p``, ``is_frozenset_of_p``                          ``st.sets``, ``st.frozensets``
``is_tuple_of_p``                                               ``st.tuples``, one strategy per position
``is_dict_of_p``                                                one small dict per key/value pair, merged and filtered
``is_frozendict_of_p``                                          like ``is_dict_of_p``, needs Python 3.15 for ``frozendict``
==============================================================  ============================================================

Merging bounds means ``ge_p(0) & lt_p(100)`` generates from ``st.integers(0, 99)`` directly, without throwing away
random integers. Bounds that can't be satisfied, such as ``ge_p(10) & lt_p(5)``, give a strategy that generates
nothing.

``has_length_p`` only constrains the length, so its lists hold ints. Combined with an element predicate, put the
element predicate first and keep the length small: ``is_list_of_p(is_str_p) & has_length_p(eq_p(3))`` works, while
``has_length_p(eq_p(3)) & is_list_of_p(is_str_p)`` starts from lists of ints and is filtered down to almost nothing.

Any other predicate is generated from its type and filtered, so the result is always correct. It can be slow when the
predicate rarely holds, in which case Hypothesis fails with a ``filter_too_much`` health check.

A predicate that has no type, such as ``is_lambda_p`` or ``implements_protocol_p``, falls back to a pool of 20 values
from the ``generate_true`` generator. That pool is random, so it differs between runs and doesn't shrink. If the
predicate has no generator either, ``from_predicate`` raises a ``TypeError``. This is the case for ``fn_p``,
``has_path_p``, ``comp_p``, ``implies_p``, ``lazy_p``, ``root_p`` and ``this_p``. Combine such a predicate with a typed
one to give it a type:

.. code-block:: python

    from predicate import fn_p, is_int_p

    @given_predicate(is_int_p & fn_p(lambda x: x % 7 == 0))
    def test_multiple_of_seven(x):
        assert x % 7 == 0

Specs
^^^^^

A :doc:`Spec <instrumentation>` describes the arguments and the result of a function. ``given_spec`` turns it into
a property test: it calls the function with generated arguments and verifies the result against ``ret``, ``fn``,
``fn_p`` and ``raises``, just like ``exercise`` does. A violation comes with Hypothesis' shrinking and replay.
Parameters that the spec doesn't mention are generated from their annotations.

.. code-block:: python

    from predicate import ge_p, is_int_p
    from predicate.hypothesis import from_spec, given_spec


    def clamp(x, low, high):
        return min(max(x, low), high)


    spec = {
        "args": {"x": is_int_p, "low": is_int_p, "high": is_int_p},
        "ret": is_int_p,
        "pre": lambda x, low, high: low <= high,
        "fn": lambda x, low, high, ret: low <= ret <= high,
    }

    test_clamp = given_spec(clamp, spec)  # pytest collects this; or call test_clamp() directly

``given_spec`` returns the test, it doesn't decorate one. When a function violates its spec, Hypothesis reports the
smallest failing input:

.. code-block:: python

    def broken(x):
        return x if x < 100 else "oops"


    given_spec(broken, {"args": {"x": ge_p(0) & lt_p(1000)}, "ret": is_int_p})()
    # SpecViolationError, with: Failing test case: check_broken(value={'x': 100})

``from_spec`` returns just the strategy of arguments, a dict of ``{parameter: value}``, with ``pre`` applied. Use it
when you want to write the test body yourself:

.. code-block:: python

    from hypothesis import given

    @given(from_spec(clamp, spec))
    def test_clamp_is_idempotent(arguments):
        once = clamp(**arguments)
        assert clamp(**{**arguments, "x": once}) == once

.. note::

    ``given_spec`` supports plain synchronous functions. Async functions, generators and classes raise a
    ``NotImplementedError``; use ``exercise`` for those.

.. note::

    Hypothesis warns about pytest fixtures with a function scope under ``@given``, because they aren't reset for each
    generated input. Use a module or session scoped fixture, or suppress ``HealthCheck.function_scoped_fixture``.
