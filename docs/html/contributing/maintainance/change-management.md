# Change Management

Any change to pip that removes or significantly alters user-visible behaviour
that is described in the pip documentation will be deprecated for a minimum of
6 months before the change occurs. Deprecation will take the form of a warning
being issued by pip when the deprecated behaviour is used.

Certain changes may be fast tracked and have a deprecation period of 3 months.
This requires at least two members of the pip team to be in favour of doing so,
and no pip maintainers opposing.

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

```{admonition} For pip's maintainers
:class: seealso
[Implementation mechanisms](../reference/change-management) that make it easier
to make changes that are compliant with our promises here.
```
