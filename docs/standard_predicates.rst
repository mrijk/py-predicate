Standard predicates
===================

This section describes the predicates that are included in py-predicate.

.. include:: set_predicates.rst
.. include:: str_predicates.rst

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

has_length_p
------------

This predicate tests the length of an iterable against another predicate.

.. code-block:: python

    from predicate import has_length_p, lt_p

    has_length_lt_2 = has_length_p(lt_p(2))

    assert not has_length_lt_2([1, 2, 3])
    assert has_length_lt_2({1})

is_bool_p
---------

This predicate tests if the value is of type ``bool``. Only True if the value is either ``False`` or ``True``.

.. code-block:: python

    from predicate import is_bool_p

    assert is_bool_p(False)
    assert is_bool_p(True)


is_callable_p
-------------

This predicate tests if the value is of type ``Callable``.

.. code-block:: python

    from predicate import is_callable_p

    assert is_callable(is_callable)
    assert is_callable(lambda x: x)
    assert is_callable(str.upper)



is_complex_p
------------

This predicate tests if the value is of type ``complex``.

.. code-block:: python

    from predicate import is_complex_p

    assert not is_complex(1)
    assert is_complex(complex(1, 1))
    assert is_complex(1 + 1j)

is_container_p
--------------

This predicate tests if the value is of type ``Container``.

.. code-block:: python

    from predicate import is_container_p

    assert is_container_p((1, 2, 3))
    assert is_container_p([1, 2, 3])
    assert is_container_p({1, 2, 3})
    assert is_container_p({"one": 1, "two": 2, "three": 3})
    assert is_container_p("one")  # a string is also a container!


is_datetime_p
-------------

This predicate tests if the value is of type ``datetime``.

.. code-block:: python

    from datetime import datetime
    from predicate import is_datetime_p

    assert is_datetime_p(datetime.now())

is_dict_p
---------

This predicate tests if the value is of type ``dict``.

.. code-block:: python

    from predicate import is_dict_p

    assert is_dict_p({"one": 1, "two": 2, "three": 3})



is_dict_of_p
------------

This predicate tests if the value is of type ``dict`` and the key and values match the predicates.

.. code-block:: python

    from predicate import is_dict_of_p, is_int_p, eq_p

    # test for dictionaries that have keys x and y. The values should be integers
    predicate = is_dict_of_p((eq_p("x"), is_int_p), (eq_p("y"), is_int_p))

    assert predicate({"x": 1, "y": 7})


is_empty_p
----------

This predicate tests if an iterable is empty.

.. code-block:: python

    from predicate import is_empty_p

    assert is_empty_p(())
    assert is_empty_p({})
    assert is_empty_p([])
    assert is_empty_p("")

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

    import math
    from predicate import is_finite_p

    assert not is_finite_p(math.inf)
    assert is_finite_p(42)

is_float_p
----------

This predicate tests if the value is of type ``float``.

.. code-block:: python

    from predicate import is_float_p

    assert not is_float_p(3)
    assert is_float_p(3.14)


is_hashable_p
-------------

This predicate tests if the value is hashable.

.. code-block:: python

    from predicate import is_hashable_p

    assert not is_hashable_p({})
    assert is_hashable_p("foo")

is_inf_p
--------

This predicate tests if the value is infinite.

.. code-block:: python

    import math
    from predicate import is_inf_p

    assert not is_inf_p(3)
    assert is_inf_p(math.inf)

is_instance_p
-------------
.. code-block:: python

    from predicate import is_instance_p

is_int_p
--------

This predicate tests if the value is of type ``int``.

.. code-block:: python

    from predicate import is_int_p

    assert not is_int_p(3.14)
    assert is_int_p(3)


is_iterable_of_p
----------------

.. code-block:: python

    from predicate import is_iterable_of_p

is_iterable_p
-------------

This predicate tests if the value is of type ``Iterable``.

.. code-block:: python

    from predicate import is_iterable_p

is_list_of_p
------------

This predicate predicate tests if the value if a list, where all items in the list conform to
a given predicate.

.. code-block:: python

    from predicate import is_list_of_p, is_str_p

    is_list_of_str = is_list_of_p(is_str_p)

    assert not is_list_of_str(["one", "two", 3])
    assert is_list_of_str(["foo"])


is_list_p
---------

This predicate tests if the value is of type ``list``.

.. code-block:: python

    from predicate import is_list_p

    assert not is_list_p({1, 2, 3})
    assert is_list_p([1, 2, 3])

is_nan_p
--------

.. code-block:: python

    import math
    from predicate import is_nan_p

    assert not is_nan_p(1)
    assert is_nan_p(math.nan)



is_none_p
---------
.. code-block:: python

    from predicate import is_none_p

    assert not is_none_p(13)
    assert is_none_p(None)


is_not_none_p
-------------
.. code-block:: python

    from predicate import is_not_none_p

    assert not is_not_none_p(None)
    assert is_not_none_p(13)

is_predicate_p
--------------

This predicate tests if the value is of type ``Predicate``.

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

This predicate predicate tests if the value if a set, where all items in the set conform to
a given predicate.

.. code-block:: python

    from predicate import is_set_of_p, is_str_p

    is_set_of_str = is_set_of_p(is_str_p)

    assert not is_set_of_str({"one", "two", 3})
    assert is_set_of_str({"foo"})


is_set_p
--------

This predicate tests if the value is of type ``set``.

.. code-block:: python

    from predicate import is_set_p

is_str_p
--------

This predicate tests if the value is of type ``str``.

.. code-block:: python

    from predicate import is_str_p

    assert not is_str_p(3.14)
    assert is_str_p("foo")

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

This predicate tests if the value is of type ``tuple``.

.. code-block:: python

    from predicate import is_tuple_p

is_uuid_p
---------

This predicate tests if the value is of type ``uuid``.

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
