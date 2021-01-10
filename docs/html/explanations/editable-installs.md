# Editable installs

Editable installs are fundamentally [setuptools's "development mode"][dev-mode]
installs. You can install local projects or VCS projects in "editable" mode:

````{tab} Unix
```shell
python -m pip install -e path/to/SomeProject
python -m pip install -e git+http://repo/my_project.git#egg=SomeProject
```
````

````{tab} macOS
```shell
python -m pip install -e path/to/SomeProject
python -m pip install -e git+http://repo/my_project.git#egg=SomeProject
```
````

````{tab} Windows
```shell
py -m pip install -e path/to/SomeProject
py -m pip install -e git+http://repo/my_project.git#egg=SomeProject
```
````

For local projects, the "SomeProject.egg-info" directory is created relative to
the project path. This is one advantage over just using ``setup.py develop``,
which creates the "egg-info" directly relative the current working directory.

```{seealso}
{ref}`VCS Support` section for more information on VCS-related syntax.
```

```{important}
As of 30 Dec 2020, PEP 517 does not support editable installs. Various members
of the Python community are working on a new standard to [address this
limitation](https://discuss.python.org/t/4098).
```

[dev-mode]: https://setuptools.readthedocs.io/en/latest/userguide/development_mode.html#development-mode
