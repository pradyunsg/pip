# Installation

pip is already installed if you are using a modern version of Python (>= 3.5)
downloaded from [python.org](https://www.python.org) or if you are working
in a [virtual environment](pypug:Creating\ and\ using\ Virtual\ Environments)
created by [virtualenv](pypug:virtualenv) or [venv](pypug:venv).

```{tip}
If you do not have Python installed, read
[this guide by Real Python][realpython-installation-guide] on how to install
Python on your system.

[realpython-installation-guide]: https://realpython.com/installing-python/
```

## Checking if you have a working pip

The best way to check if you have a working pip installation is to run:

```{pip-cli} --version
```

If you see output of the following form:

```none
pip X.Y.Z from .../site-packages/pip (python X.Y)
```

Congratulations! You have a working pip in your environment. Skip ahead to the 
[Next steps](#next-steps) section on this page.

If not, read on. We're going to walk through setting up a Python environment
with pip available for use.

## Installing via get-pip.py

[TODO: complete me]

## Installing using ensurepip

[TODO: complete me]

## Next steps

### Learn to create and work in virtual environments

Virtual environments are an important part of Python development, which help
keep your Python environment for different projects separate. This simplifies
management of Python packages. It is strongly recommended to use a virtual
environment [^unless-you-have-a-good-reason].

[Creating and using Virtual Environments](pypug:Creating\ and\ using\ Virtual\ Environments)
on [packaging.python.org](pypug:index) provides more details and guidance.

### Upgrade to the newest pip version

It is strongly encouraged to use the latest version of pip. It has all the
newest bugfixes, enhancements and features. It also helps ensure that the
Python Packaging ecosystem can evolve and improve.

```{warning}
If you are using Python installed by your operating system's package manager
(eg: apt, yum, dnf), don't use the following command to update the `pip`
installed by your system package manager. Instead, it is recommended to use a
virtual environment for working, and to use an updated pip in that environment.
[^unless-you-have-a-good-reason]
```

```{pip-cli} install pip --upgrade
```

[^unless-you-have-a-good-reason]: This is a recommendation aimed at beginners,
  for nudging them toward best practices. If you have a good reason not to
  follow it, feel free to do so. However, if you're able to describe the
  situations where this recommendation does not apply, you're likely not the
  intended audience for this tutorial.
