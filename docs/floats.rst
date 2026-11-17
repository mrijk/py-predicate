Float conveniences
==================

``is_integer_valued_p`` accepts floats such as ``3.0`` and ``-0.0`` and rejects
fractional values, infinities and NaN. It checks a float's value, not whether
an arbitrary object can be converted to a float.

``is_probability_p`` is ``ge_le_p(0.0, 1.0)``: both endpoints are included,
and NaN is outside the interval.

Use an absolute tolerance near zero or when relative slack is unwanted::

    from predicate import is_within_p

    nearby = is_within_p(1_000_000_000.0, 0.25)
    assert nearby(1_000_000_000.25)
    assert not nearby(1_000_000_000.5)

``is_within_p(target, delta)`` uses ``is_close_p`` with relative tolerance zero.
The target and delta must be finite and delta must be non-negative; invalid
parameters raise ``ValueError``. A zero delta accepts only exact equality.

All three conveniences work with ``generate_true`` and ``generate_false``.
The tolerance wrapper reuses the existing approximate-comparison generators.
