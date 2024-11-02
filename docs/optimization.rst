Optimization
============

py-predicate can optimize predicates in many ways.

For example:

.. code-block:: python

    ge_2 = ge_p(2)
    lt_2 = ~ge_2

    predicate = ge_2 & lt_2

    # Optimize

    optimized = optimize(predicate)

    assert optimized == always_false_p

When visualized this looks like this:

.. graphviz:: optimized.dot