Standard predicates
===================

Info about predicates

all_p
-----

This predicate tests if for all elements in an Iterable, the enclosed predicate is True:

.. code-block:: python

    from predicate import all_p, is_int_p

    # Predicate to test if all items in an iterable are of type int
    all_int = all_p(is_int_p)

    assert all_int([1, 2, 3])
    assert not all_int([None, 2, 3])

The equivalent code without using predicates could be something like:

.. code-block:: python

    def all_int(iter: Iterable) -> bool:
        return all(isinstance(ele, int) for ele in iter)


any_p
-----

This predicate tests if for any element in an Iterable, the enclosed predicate is True:

.. code-block:: python

    from predicate import any_p, is_int_p

    # Predicate to test if any of the items in an iterable is of type int
    any_int = any_p(is_int_p)

    assert not any_int(())
    assert any_int((1, 2, 3))
    assert any_int([1, 2, 3])
    assert any_int([None, 2, 3])

eq_p
----

This predicates tests for equality.

.. code-block:: python

    from predicate import eq_p

    eq_2 = eq_p(2)

    assert eq_2(2)
    assert not eq_2(3)



ge_p
----

This predicates tests for greater or equal a value.

.. code-block:: python

    from predicate import ge_p

    ge_2 = ge_p(2)

    assert ge_2(2)
    assert not ge_2(1)

gt_p
----

This predicates tests for greater than a value.

.. code-block:: python

    from predicate import gt_p

    gt_2 = gt_p(2)

    assert not gt_2(2)
    assert gt_2(3)

is_falsy_p
----------

This predicate tests for falsy values, for example False, "", {}, [], 0, etc.

.. code-block:: python

    from predicate import is_falsy_p

    assert is_falsy_p(0)
    assert is_falsy_p({})

is_range_p
----------

This predicate tests if value is a range.

.. code-block:: python

    from predicate import is_range_p

    assert not is_range_p(0)
    assert is_range_p(range(5))

is_truthy_p
-----------

This predicate tests for truthy values, for example True, "foo", {"foo"}, [1], 13, etc.

.. code-block:: python

    from predicate import is_truthy_p

    assert is_truthy_p(1)
    assert is_truthy_p({"foo"})

le_p
----

This predicates tests for less than or equal a value.

.. code-block:: python

    from predicate import le_p

    le_2 = le_p(2)

    assert le_2(2)
    assert not le_2(3)

lt_p
----

This predicates tests for less than a value.

.. code-block:: python

    from predicate import lt_p

    lt_2 = lt_p(2)

    assert not lt_2(2)
    assert lt_2(1)

ne_p
----

This predicate tests for non equality


.. code-block:: python

    from predicate import ne_p

    ne_2 = ne_p(2)

    assert not ne_2(2)
    assert ne_2(3)


tee_p
-----

Predicate that always returns True, but is useful for handling side-effects.

.. code-block:: python

    from predicate import all_p, lt_p, tee_p

    log = tee_p(print)

    all_lt_2 = all_p(log | lt_p(2))
