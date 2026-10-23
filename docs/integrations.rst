Integrations
============

Predicates are plain callables, so they work with any library that accepts a function
returning a ``bool``. For some libraries py-predicate provides ready-made wrappers.

ReactiveX
---------

The ``predicate.rx`` module wraps the `ReactiveX <https://github.com/ReactiveX/RxPY>`_ operators that take a
predicate, so they can be used directly in a ``pipe``. Install the optional dependency first:

.. code-block:: bash

    pip install py_predicate[rx]

Then filter a stream with a predicate:

.. code-block:: python

    import reactivex as rx

    from predicate import gt_p
    from predicate.rx import filter_p

    rx.of(1, 2, 3, 4).pipe(filter_p(gt_p(2))).subscribe(print)  # prints 3 and 4

The following operators are available:

========================  =================================================================================
Operator                  Description
========================  =================================================================================
``filter_p``              only lets through items satisfying the predicate
``take_while_p``          lets through items as long as the predicate holds (``inclusive`` keeps the first
                          item that fails)
``skip_while_p``          skips items as long as the predicate holds
``partition_p``           splits a stream into ``[matching, non_matching]`` observables
``all_p``                 emits whether all items satisfy the predicate
``some_p``                emits whether any item satisfies the predicate
``count_p``               emits the number of items satisfying the predicate
``first_p``               emits the first item satisfying the predicate, errors if there is none
``last_p``                emits the last item satisfying the predicate, errors if there is none
``single_p``              emits the only item satisfying the predicate, errors if there is not exactly one
``first_or_default_p``    like ``first_p``, but emits ``default_value`` if there is none
``last_or_default_p``     like ``last_p``, but emits ``default_value`` if there is none
``single_or_default_p``   like ``single_p``, but emits ``default_value`` if there is none
``find_p``                emits the first item satisfying the predicate, or ``None`` if there is none
``find_index_p``          emits the index of the first item satisfying the predicate, or ``-1`` if there is none
========================  =================================================================================

``all_p`` and ``count_p`` share their names with core predicates, so alias them when you need both:

.. code-block:: python

    from predicate import all_p
    from predicate.rx import all_p as rx_all_p

.. note::

    ``partition_p`` subscribes to the source once per output stream. With a cold source such as ``rx.of``, the
    first subscription consumes all items before the second one starts. Use a hot source when both streams need
    to see the items, e.g. a ``Subject`` or a published source:

    .. code-block:: python

        import reactivex as rx
        import reactivex.operators as ops

        from predicate import gt_p
        from predicate.rx import partition_p

        source = rx.of(1, 2, 3, 4).pipe(ops.publish())
        matching, non_matching = source.pipe(partition_p(gt_p(2)))

        matching.subscribe(print)  # prints 3 and 4
        non_matching.subscribe(print)  # prints 1 and 2
        source.connect()
