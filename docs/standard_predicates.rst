Standard predicates
===================

This section describes the predicates that are included in py-predicate.

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


always_false_p
--------------

This predicate ignores any arguments and always returns False:

.. code-block:: python

    from predicate import always_false_p

    assert not always_false_p(13)


This might be the result of an optimization.

always_true_p
-------------

This predicate ignores any arguments and always returns True:

.. code-block:: python

    from predicate import always_true_p

    assert always_true_p(13)


This might be the result of an optimization.

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


eq_false_p
----------

This predicates tests if the argument is False.

.. code-block:: python

    from predicate import eq_false_p

    assert eq_false_p(False)
    assert not eq_false_p(True)

Note that this tests for the exact boolean value False. If you want to test for falsy values, see:
:ref:`is_falsy_p`.

eq_p
----

This predicates tests for equality.

.. code-block:: python

    from predicate import eq_p

    eq_2 = eq_p(2)

    assert eq_2(2)
    assert not eq_2(3)

eq_true_p
----------

This predicates tests if the argument is True.

.. code-block:: python

    from predicate import eq_true_p

    assert not eq_true_p(False)
    assert eq_true_p(True)

Note that this tests for the exact boolean value True. If you want to test for falsy values, see:
:ref:`is_truthy_p`.

fn_p
----

This predicate can be used to wrap any (lambda) function:

.. code-block:: python

    from predicate import fn_p

    square_ge_2 = fn_p(lambda x: x * x >= 2)

    assert not square_ge_2(1)
    assert square_ge_2(2)

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

is_bool_p
---------
.. code-block:: python

    from predicate import is_bool_p

is_callable_p
-------------
.. code-block:: python

    from predicate import is_callable_p

is_complex_p
------------
.. code-block:: python

    from predicate import is_complex_p

is_container_p
--------------
.. code-block:: python

    from predicate import is_container_p

is_datetime_p
-------------
.. code-block:: python

    from predicate import is_datetime_p

is_dict_p
---------
.. code-block:: python

    from predicate import is_dict_p

is_empty_p
----------
.. code-block:: python

    from predicate import is_empty_p

.. _is_falsy_p:

is_falsy_p
----------

This predicate tests for falsy values, for example False, "", {}, [], 0, etc.

.. code-block:: python

    from predicate import is_falsy_p

    assert is_falsy_p(0)
    assert is_falsy_p({})

is_finite_p
-----------
.. code-block:: python

    from predicate import is_finite_p

is_float_p
----------
.. code-block:: python

    from predicate import is_float_p

is_hashable_p
-------------
.. code-block:: python

    from predicate import is_hashable_p

is_inf_p
--------
.. code-block:: python

    from predicate import is_inf_p

is_instance_p
-------------
.. code-block:: python

    from predicate import is_instance_p

is_int_p
--------
.. code-block:: python

    from predicate import is_int_p

is_iterable_of_p
----------------
.. code-block:: python

    from predicate import is_iterable_of_p

is_iterable_p
-------------
.. code-block:: python

    from predicate import is_iterable_p

is_list_of_p
------------
.. code-block:: python

    from predicate import is_list_of_p

is_list_p
---------
.. code-block:: python

    from predicate import is_list_p

is_none_p
---------
.. code-block:: python

    from predicate import is_none_p

is_not_none_p
-------------
.. code-block:: python

    from predicate import is_not_none_p

is_predicate_p
--------------
.. code-block:: python

    from predicate import is_predicate_p

is_range_p
----------

This predicate tests if value is a range.

.. code-block:: python

    from predicate import is_range_p

    assert not is_range_p(0)
    assert is_range_p(range(5))

is_set_of_p
-----------
.. code-block:: python

    from predicate import is_set_of_p

is_set_p
--------
.. code-block:: python

    from predicate import is_set_p

is_str_p
--------
.. code-block:: python

    from predicate import is_str_p

.. _is_truthy_p:

is_truthy_p
-----------

This predicate tests for truthy values, for example True, "foo", {"foo"}, [1], 13, etc.

.. code-block:: python

    from predicate import is_truthy_p

    assert is_truthy_p(1)
    assert is_truthy_p({"foo"})

is_tuple_of_p
-------------
.. code-block:: python

    from predicate import is_tuple_of_p

is_tuple_p
----------
.. code-block:: python

    from predicate import is_tuple_p

is_uuid_p
---------
.. code-block:: python

    from predicate import is_uuid_p

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
