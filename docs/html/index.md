# Welcome to pip's documentation!

pip is the [standard package installer][1] for Python.

It comes as a part of with all modern versions of Python and is installed
alongside Python by default [^footnote]. It is used to download, build and
install your projects' dependencies, and manage packages in a Python 
environment.

This documentation has 4 main sections:

[Getting Started](getting-started)
: Get started with using pip. If you're new to Python, start here.

[Explanations](explanations)
: Explanations provide detailed information on key topics and concepts.

[Reference Guide](reference)
: Reference Guide explains the implementation and provides an entry-point for
pip's developers.

[Commands](cli/index)
: Commands is a detailed description of the command line interface.

```{toctree}
:hidden:

getting-started
explanations
reference
cli/index
news
```

```{toctree}
:caption: Community
community
```

```{toctree}
:caption: Contributing
:hidden:

contributing/development/index
contributing/maintainance
contributing/ux
GitHub <https://github.com/pypa/pip>
```

[1]: https://packaging.python.org/guides/tool-recommendations/

[^footnote]: Certain Linux distributions do not ship `pip` as a part of their
  default Python installation, since they consider `pip` to be a non-essential
  for using Python programs -- they expect their users to exclusively use the
  OS package manager's packages, or to install pip separately.
