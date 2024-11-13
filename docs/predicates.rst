Predicates
==========

These predicates form the building blocks (and, or, not, xor) to compose more complex predicates.

And predicate
-------------

The 'and' predicate combines two predicates into a new one, using the overloaded & operator.

The predicate evaluates to True if both predicates are True, otherwise False.

In the next example we combine 2 predicates (ge_2 and le_3) into a new one:

.. code-block:: python

    ge_2 = ge_p(2)
    le_3 = le_p(3)

    between_2_and_3 = ge_2 & le_3

    assert between_2_and_3(2) is True
    assert between_2_and_3(3) is True
    assert between_2_and_3(0) is False
    assert between_2_and_3(4) is False

Or predicate
------------

The 'or' predicate combines two predicates into a new one, using the overloaded | operator.

The predicate evaluates to True if any of the predicates is true, otherwise False.

Example:

.. code-block:: python

    ge_4 = ge_p(4)
    le_2 = le_p(2)

    le_2_or_ge_4 = le_2 | ge_4

    assert le_2_or_ge_4(2) is True
    assert le_2_or_ge_4(4) is True
    assert le_2_or_ge_4(3) is False

Xor predicate
-------------

The 'xor' predicate combines two predicates into a new one, using the overloaded ^ operator.

The predicate evaluates to True if exactly one of the two predicates is True, otherwise False.

Example:


.. code-block:: python

    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    ge_2_xor_ge_4 = ge_2 ^ ge_4

    assert ge_2_xor_ge_4(1) is False
    assert ge_2_xor_ge_4(2) is True
    assert ge_2_xor_ge_4(4) is False


Not predicate
-------------

The 'not' predicate negates a predicate, using the overloaded ~ operator

Example:

.. code-block:: python

    ge_2 = ge_p(2)

    lt_2 = ~ge_2

    assert lt_2(2) is False
    assert lt_2(1) is True
