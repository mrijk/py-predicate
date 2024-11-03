Predicates
==========

Info about predicates

all_p
-----

This predicate tests if for all elements in an Iterable, the enclosed predicate is True:

.. code-block:: python

    all_int = all_p(is_int_p)

    assert all_int([1, 2, 3])
    assert not all_int([None, 2, 3])

The equivalent code without using predicates could be something like:

.. code-block:: python

    def all_int(iter: Iterable) -> bool
        return all(isinstance(ele, int) for ele in iter)


any_p
-----

This predicate tests if for any element in an Iterable, the enclosed predicate is True:

.. code-block:: python

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

gt_p
----

le_p
----

lt_p
----

ne_p
----
