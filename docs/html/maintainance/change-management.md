# Change Management

Any change to pip that removes or significantly alters user-visible behaviour
that is described in the pip documentation will be deprecated for a minimum of
6 months before the change occurs.

Certain changes may be fast tracked and have a deprecation period of 3 months.
This requires at least two members of the pip team to be in favor of doing so,
and no pip maintainers opposing.

Deprecation of any behaviour will take the form of a warning being issued by
pip when the feature is used.

Longer deprecation periods, or deprecation warnings for behaviour changes that
would not normally be covered by this policy, are also possible depending on
circumstances, but this is at the discretion of the pip maintainers.

## Documentation is source of truth

This documentation is the sole reference for what counts as agreed user-visible 
behaviour. If something isn't explicitly mentioned in the documentation, it can
be changed without warning, or any deprecation period, in a pip release.

Note that there are areas where this documentation isn't complete -- pull
requests that document existing behaviour with the intention of covering that
behaviour with the above deprecation process are always acceptable, and will be
considered on their merits.

## `deprecated` helper

pip's developers are expected to use our internal helper function for handling
deprecations.

```{eval-rst}
.. autofunction:: pip._internal.utils.deprecation.deprecated
    :noindex:
```



pip also has feature flags, which take the form of 

| thing |  |  |  |  |
| ----- | --- | --- | --- | --- |
| old thing | default | default | behind `--use-deprecated` | not available |
| new thing | not available | behind `--use-feature` | default, `--use-feature` is no op | default, removed from `--use-feature` |

Feature Flags
=============

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
