Set predicates
--------------

A collection of predicates that act on sets.

in_p
~~~~
Return True if the values are included in the container, otherwise False.

.. code-block:: python

    from predicate import in_p

    in_123 = in_p([1, 2, 3])

    assert not in_123(0)
    assert in_123(1)


is_subset_p
~~~~~~~~~~~
Return True if the value is a subset, otherwise False.

.. code-block:: python

    from predicate import is_subset_p

    sub_123 = is_subset_p({1, 2, 3})

    assert not sub_123({0, 1})
    assert sub_123({1, 2})


is_superset_p
~~~~~~~~~~~~~
Return True if the value is a superset, otherwise False.

.. code-block:: python

    from predicate import is_superset_p

    super_123 = is_superset_p({1, 2, 3})

    assert not super_123({1, 2, 4})
    assert super_123({1, 2, 3, 4})


is_real_subset_p
~~~~~~~~~~~~~~~~
Return True if the value is a real subset, otherwise False.

.. code-block:: python

    from predicate import is_real_subset_p

    sub_123 = is_real_subset_p({1, 2, 3})

    assert not sub_123({1, 2, 3})
    assert sub_123({1, 2})


is_real_superset_p
~~~~~~~~~~~~~~~~~~
Return True if the value is a real superset, otherwise False.

.. code-block:: python

    from predicate import is_real_superset_p

    super_123 = is_real_superset_p({1, 2, 3})

    assert not super_123({1, 2, 3})
    assert super_123({1, 2, 3, 4})


not_in_p
~~~~~~~~
Return True if the values are not in the container, otherwise False.

.. code-block:: python

    from predicate import not_in_p

    not_in_123 = not_in_p([1, 2, 3])

    assert not_in_123(0)
    assert not not_in_123(1)
