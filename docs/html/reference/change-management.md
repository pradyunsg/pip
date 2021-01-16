# Change Management

This page describes the implemented designs/mechanisms we have available, for
managing changes in pip. This isn't an exhaustive description of how we manage
changes. Instead, these are mechanisms we have created over time that make it
easier to do the right thing.

Overall, pip has a _very large_ user base which does not get excited when we
make changes in pip.

## `deprecated` helper

pip's developers are expected to use our internal helper function for providing
deprecation warnings to users. The helper exists to make it easier to ensure
that we're including all the required information in our messages.

```{eval-rst}
.. autofunction:: pip._internal.utils.deprecation.deprecated
    :noindex:
```

## Feature flags 

pip also has feature flags which provide mechanism to test experimental
features in the codebase, without affecting existing users. It is also our
primary mechanism to provide users with the ability to "early opt-in" and
"late opt-out" when making disruptive changes (like
{issue}`changing our dependency resolver <6536>`).

### `--use-feature`

For new behaviours, before they become default.

Once the feature becomes the default behaviour, this flag can remain in place,
but should issue a warning telling the user that it is no longer necessary.

### `--use-deprecated`

For old behaviours that are deprecated.

Behaviours moved behind this flag should always include a warning that indicates
when the behaviour is scheduled to be removed.

Once the behaviour is removed, users who use the flag should be shown an error.

### Expected use for transitions

The way these flags are expected to be used is as per the following table:

```{eval-rst}
+---------+---------------+--------------------------+-----------------------------+--------------------------------+
| Variant | old times     | new beginnings           | transition!                 | new times                      |
+=========+===============+==========================+=============================+================================+
| **old** | default       | default                  | behind ``--use-deprecated`` | not available                  |
+---------+---------------+--------------------------+-----------------------------+--------------------------------+
| **new** | not available | behind ``--use-feature`` | default,                    | default,                       |
|         |               |                          | ``--use-feature`` is no-op  | removed from ``--use-feature`` |
+---------+---------------+--------------------------+-----------------------------+--------------------------------+
```

If we want to provide 2 code paths, we should instead treat this as a case
where we want to add a new CLI flag.
