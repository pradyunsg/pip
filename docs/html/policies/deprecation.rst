.. _`Deprecation Policy`:

==================
Deprecation Policy
==================

Any change to pip that removes or significantly alters user-visible behaviour
that is described in the pip documentation will be deprecated for a minimum of
6 months before the change occurs.

Certain changes may be fast tracked and have a deprecation period of 3 months.
This requires at least two members of the pip team to be in favour of doing so,
and no pip maintainers opposing.

Deprecation will take the form of a warning being issued by pip when the
feature is used. Longer deprecation periods, or deprecation warnings for
behaviour changes that would not normally be covered by this policy, are also
possible depending on circumstances, but this is at the discretion of the pip
maintainers.

Note that the documentation is the sole reference for what counts as agreed
behaviour. If something isn't explicitly mentioned in the documentation, it can
be changed without warning, or any deprecation period, in a pip release.
However, we are aware that the documentation isn't always complete - PRs that
document existing behaviour with the intention of covering that behaviour with
the above deprecation process are always acceptable, and will be considered on
their merits.

.. note::

  pip has a helper function for making deprecation easier for pip maintainers.
  The supporting documentation can be found in the source code of
  ``pip._internal.utils.deprecation.deprecated``. The function is not a part of
  pip's public API.


.. _`Feature Flags`:

Feature Flags
=============

Certain feature flags are available to provide opt-in/opt-out semantics for the
behaviour of pip, allowing for more gradual transition strategies.

``--use-deprecated``
--------------------

Example: ``--use-deprecated=legacy-resolver``

Use for features that will be deprecated. Deprecated features should remain
available behind this flag for at least six months, as per the deprecation
policy.

Features moved behind this flag should always include a warning that indicates
when the feature is scheduled to be removed.

Once the feature is removed, users who use the flag should be shown an error.

``--use-feature``
-----------------

Example: ``--use-feature=2020-resolver``

Use for new features that users can test before they become pip's default
behaviour (e.g. alpha or beta releases).

Once the feature becomes the default behaviour, this flag can remain in place,
but should issue a warning telling the user that it is no longer necessary.
