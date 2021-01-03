# Welcome to pip's documentation!

pip is the [standard package installer][1] for Python.

It comes as a part of with all modern versions of Python and is installed
alongside Python by default [^footnote]. It is used to download, build and
install your projects' dependencies, and manage packages in a Python 
environment.
 
This documentation has 4 main sections:

````{panels}
:container: container pb-4
:column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
:card: shadow

---

[Getting Started](getting-started)

Get started with using pip with an explanation of the interface and basic
capabilities.

---

[Explanations](explanations)

Explanations provide detailed information on key topics and concepts.

---

[Reference Guide](reference)

Reference Guide explains the implementation and provides an entry-point for
pip's developers.

---

[Commands](cli/index)

Commands is a detailed description of the command line interface.
````

```{toctree}
:hidden:

getting-started
explanations
reference
cli/index
news
```

```{toctree}
:caption: Contributing
:hidden:

development/index
ux
GitHub <https://github.com/pypa/pip>
```

[1]: https://packaging.python.org/guides/tool-recommendations/

[^footnote]: Certain Linux distributions do not ship `pip` as a part of their
  default Python installation, since they consider `pip` to be a non-essential
  for using Python programs -- they expect their users to exclusively use the
  OS package manager's packages, or to install pip separately.
