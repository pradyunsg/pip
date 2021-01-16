---
hide-toc: true
---

# Compatibility

pip works on:

- Windows, MacOS and Linux.
- CPython (3.6, 3.7, 3.8, 3.9) and PyPy3.

Only the latest patch version release of pip is considered supported. Previous
patch versions are supported on a best effort approach.

## Support for Python versions

In general, a given Python version is supported until its usage on PyPI falls
below 5%. This is completely at the maintainers' discretion, in case
extraordinary circumstances arise.

```{admonition} Python 2 is not supported
:class: caution

pip 20.3 was the last version of pip that supported _any_ Python 2 release.
Bugs reported with pip which only occur on Python 2 will likely be closed as
"won't fix" by pip's maintainers.
```
