===============
Release process
===============

.. _`Release Cadence`:


.. _`Deprecation Policy`:

Deprecation Policy
==================


.. _`Python 2 Support`:

Python 2 Support
----------------

pip 20.3 was the last version of pip that supported Python 2. Bugs reported
with pip which only occur on Python 2.7 will likely be closed as "won't fix"
issues by pip's maintainers.

Python Support Policy
---------------------

.. _`Feature Flags`:


Release Process
===============

Creating a new release
----------------------

#. Checkout the current pip ``master`` branch.
#. Ensure you have the latest ``nox`` installed.
#. Prepare for release using ``nox -s prepare-release -- YY.N``.
   This will update the relevant files and tag the correct commit.
#. Build the release artifacts using ``nox -s build-release -- YY.N``.
   This will checkout the tag, generate the distribution files to be
   uploaded and checkout the master branch again.
#. Upload the release to PyPI using ``nox -s upload-release -- YY.N``.
#. Push all of the changes including the tag.
#. Regenerate the ``get-pip.py`` script in the `get-pip repository`_ (as
   documented there) and commit the results.
#. Submit a Pull Request to `CPython`_ adding the new version of pip (and upgrading
   setuptools) to ``Lib/ensurepip/_bundled``, removing the existing version, and
   adjusting the versions listed in ``Lib/ensurepip/__init__.py``.


.. note::

  If the release dropped the support of an obsolete Python version ``M.m``,
  a new ``M.m/get-pip.py`` needs to be published: update the ``all`` task from
  ``tasks/generate.py`` in `get-pip repository`_ and make a pull request to
  `psf-salt repository`_ to add the new ``get-pip.py`` (and its directory) to
  ``salt/pypa/bootstrap/init.sls``.


.. note::

  If the ``get-pip.py`` script needs to be updated due to changes in pip internals
  and if the last ``M.m/get-pip.py`` published still uses the default template, make
  sure to first duplicate ``templates/default.py`` as ``templates/pre-YY.N.py``
  before updating it and specify in ``tasks/generate.py`` that ``M.m/get-pip.py``
  now needs to use ``templates/pre-YY.N.py``.


Creating a bug-fix release
--------------------------

Sometimes we need to release a bugfix release of the form ``YY.N.Z+1``. In
order to create one of these the changes should already be merged into the
``master`` branch.

#. Create a new ``release/YY.N.Z+1`` branch off of the ``YY.N`` tag using the
   command ``git checkout -b release/YY.N.Z+1 YY.N``.
#. Cherry pick the fixed commits off of the ``master`` branch, fixing any
   conflicts.
#. Run ``nox -s prepare-release -- YY.N.Z+1``.
#. Merge master into your release branch and drop the news files that have been
   included in your release (otherwise they would also appear in the ``YY.N+1``
   changelog)
#. Push the ``release/YY.N.Z+1`` branch to github and submit a PR for it against
   the ``master`` branch and wait for the tests to run.
#. Once tests run, merge the ``release/YY.N.Z+1`` branch into master, and follow
   the above release process starting with step 4.

.. _`get-pip repository`: https://github.com/pypa/get-pip
.. _`psf-salt repository`: https://github.com/python/psf-salt
.. _`CPython`: https://github.com/python/cpython
