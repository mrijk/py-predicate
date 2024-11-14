Standard predicates
===================

Info about predicates

all_p
-----

This predicate tests if for all elements in an Iterable, the enclosed predicate is True:

.. code-block:: python

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

    eq_2 = eq_p(2)

    assert eq_2(2)
    assert not eq_2(3)



ge_p
----

This predicates tests for greater or equal a value.

.. code-block:: python

    ge_2 = ge_p(2)

    assert ge_2(2)
    assert not ge_2(1)

gt_p
----

This predicates tests for greater than a value.

.. code-block:: python

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

    le_2 = le_p(2)

    assert le_2(2)
    assert not le_2(3)

lt_p
----

This predicates tests for less than a value.

.. code-block:: python

    lt_2 = lt_p(2)

    assert not lt_2(2)
    assert lt_2(1)

ne_p
----

This predicate tests for non equality


.. code-block:: python

    ne_2 = ne_p(2)

    assert not ne_2(2)
    assert ne_2(3)
