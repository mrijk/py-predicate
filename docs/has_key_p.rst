has_key_p
=========

This predicate tests if a mapping (e.g. a ``dict``) contains at least one key that satisfies a given predicate.

Basic usage — check for an exact key using ``eq_p``:

.. code-block:: python

    from predicate import eq_p, has_key_p

    has_name = has_key_p(eq_p("name"))

    assert has_name({"name": "Alice", "age": 30})
    assert not has_name({"age": 30})

Because the key argument is itself a predicate, you can match keys by any criterion.
For example, check whether any key starts with an underscore:

.. code-block:: python

    from predicate import has_key_p, starts_with_p

    has_private_key = has_key_p(starts_with_p("_"))

    assert has_private_key({"_id": 1, "name": "Alice"})
    assert not has_private_key({"name": "Alice"})

Or check whether any integer key is greater than 10:

.. code-block:: python

    from predicate import gt_p, has_key_p

    has_large_key = has_key_p(gt_p(10))

    assert has_large_key({5: "a", 15: "b"})
    assert not has_large_key({1: "a", 5: "b"})

You can also negate the predicate to check that no key satisfies a condition:

.. code-block:: python

    from predicate import eq_p, has_key_p

    no_name_key = ~has_key_p(eq_p("name"))

    assert no_name_key({"age": 30})
    assert not no_name_key({"name": "Alice", "age": 30})
