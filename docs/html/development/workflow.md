# Workflow

This page describes the tooling used during development of pip. It also serves as a reference for the various commands that you would use when working on this project.

## Overview

pip is a command line application written in Python. For developing pip, you
should [install Python] on your computer. The project follows the [GitHub Flow]
for collaboration.

- {pypi}`nox` is used for automating development tasks.
- {pypi}`sphinx` is used for generating this documentation.
- {pypi}`pytest` is used as the test runner.
- {pypi}`pre-commit` is used for managing the linters.

[install python]: https://realpython.com/installing-python/
[github flow]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/github-flow

## Initial Setup

To work on this project, you need Python 3.8 or newer. It is recommended to
[fork] pip's [GitHub repository][github-repo], and to add the original
repository as a [git remote][git-remote] named "upstream".

```console
$ git clone https://github.com/[your-username-here]/pip
$ cd pip
$ git remote add upstream https://github.com/pypa/pip
```

You'd also want to install {pypi}`nox`, since it is a major part of our
development workflow.

[fork]: https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo
[github-repo]: https://github.com/pypa/pip/
[git-remote]: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

## Code Linting

pip uses {pypi}`pre-commit` for managing linting of the codebase. `pre-commit`
performs various checks on all files in pip and uses tools that help follow a
consistent code style within the codebase.

To use linters locally, run:

```console
$ nox -s lint
```

```{note}
Avoid using `# noqa` comments to suppress linter warnings. Wherever possible,
these warnings should be fixed instead. `# noqa` comments are reserved for rare
cases where the recommended style causes severe readability problems.
```

## Running Tests

pip's tests are written using the {pypi}`pytest` test framework, {pypi}`mock`
and {pypi}`pretend`.

To run tests, with maximised parallelism:

```console
$ nox -s test-3.8 -- -n auto
```

```{important}
Due to how pip's tests work, it is preferable to run the tests in parallel.
When run without parallelisation, the tests can take a long time to finish.
```

It is also possible to run the tests without parallelism, although this is not
recommended unless you're running a really small part of pip's test suite.

```console
$ nox -s test-3.8
```

The example above runs tests against Python 3.8. You can also use other
versions like `test-3.9` and `pypy3`.

### Selecting specific tests to run

`nox` has been configured to forward any additional arguments it is given to
`pytest`. This enables the use of pytest's [rich CLI][pytest-cli]. As an
example, you can select tests using the various ways that pytest provides:

```console
$ # Using file name
$ nox -s test-3.8 -- tests/functional/test_install.py
$ # Using markers
$ nox -s test-3.8 -- -m unit
$ # Using keywords
$ nox -s test-3.8 -- -k "install and not wheel"
```

Running pip's test suite requires supported version control tools (subversion,
bazaar, git, and mercurial) to be installed. If you are missing one of the VCS
tools, you can tell pip to skip those tests:

```console
$ nox -s test-3.8 -- -k "not svn"
$ nox -s test-3.8 -- -k "not (svn or git)"
```

[pytest-cli]: https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests

## Building Documentation

pip's documentation is built using {pypi}`Sphinx`. The documentation is written
in Markdown (using {pypi}`myst-parser`) and reStructuredText.

To build it locally, run:

```console
$ nox -s docs
```

The built documentation can be found in the `docs/build` folder.

````{hint}
pip uses ReadTheDocs' [PR previews][pr-previews] feature, to build and deploy
documentation in each pull request. The URL for this preview follows the format:

```none
https://pip--<PR-NUMBER>.org.readthedocs.build/en/<PR-NUMBER>
```
````

### With "live-reload"

It is possible to use {pypi}`sphinx-autobuild` to build pip's documentation.
This is especially useful when authoring content for the documentation since it
shortens the number of actions in the feedback loop to see the rendered
documentation.

```console
$ nox -s docs-live
```

This will start a server on `localhost:8000` that serves the built documentation
and watches for changes in the `docs/html` directory. If it detects a change,
it will trigger an rebuild and auto-reload all open documentation pages on
the browser.

[pr-previews]: https://docs.readthedocs.io/en/stable/guides/autobuild-docs-for-pull-requests.html
