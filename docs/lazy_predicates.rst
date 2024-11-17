Lazy predicates
===============

Lazy predicates are a more advanced feature that allow composing predicates that reference
themself, or even having predicates with mutual references.

There are 3 types of lazy predicates:

#. lazy_p: references another predicate by name.
#. this_p: refers to the predicate to which the this_p belongs
#. root_p: refers to the root predicate, i.e. the fully composed predicate

In the next chapters we will explain them in more detail

.. include:: lazy_p.rst
.. include:: this_p.rst
.. include:: root_p.rst
