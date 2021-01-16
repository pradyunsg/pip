# Release Management

## Release Cadence

The pip project has a release cadence of releasing whatever is on `master`
every 3 months. Our release months are January, April, July, October.

This gives users a predictable pattern for when releases are going to happen
and prevents locking up improvements for fixes for long periods of time, while
still preventing massively fracturing the user base with version numbers.

### Skipping releases

The release date within that month will be up to the release manager for that
release. If there are no changes worth releasing, then that release month is
skipped and the next release will be 3 months later.

### Pre-releases

The release manager may, at their discretion, choose whether or not there
will be a pre-release period for a release. If there is, they may extend the
main release into the next month if needed.

### Always be ready for release

Since releases are made direct from the `master` branch, it is essential
that `master` is always in a releasable state.

It is acceptable to merge PRs that partially implement a new feature, but only
if the partially implemented version is usable in that state (for example, with
reduced functionality or disabled by default).

In the case where a merged PR is found to need extra work before being
released, the release manager always has the option to back out the partial
change prior to a release. The PR can then be reworked and resubmitted for the
next release.

## Release manager

Every pip release has a release manager. The main responsibility of the release 
manager is to coordinate:

- deciding whether a change needs additional work before being released
- publishing of the release
- communicating about the publication of the release to the community

The release manager will be a member of the pip team, usually someone with
commit access to the project. Picking a release manager for a certain release
is via concensus amongst pip's committers.

## Release process

```{note}
There is an ongoing effort to further automate our release process:
{issue}`2314`.

In July 2020, @pradyunsg listed the exact commands he has to run for a normal
release [here](https://github.com/pypa/pip/issues/8511#issuecomment-665414625).
```

### Creating a new release

1. Checkout the current pip `master` branch.
1. Ensure you have the latest `nox` installed.
1. Prepare for release using `nox -s prepare-release -- YY.N`.
   This will update the relevant files and tag the correct commit.
1. Build the release artifacts using `nox -s build-release -- YY.N`.
   This will checkout the tag, generate the distribution files to be
   uploaded and checkout the master branch again.
1. Upload the release to PyPI using `nox -s upload-release -- YY.N`.
1. Push all of the changes including the tag.
1. Regenerate [^get-pip-1] [^get-pip-2] the `get-pip.py` script in the
   [pypa/get-pip][get-pip] repository (as documented there) and commit the
   results.
1. Submit a Pull Request to CPython, adding the new version of pip (and
   upgrading setuptools) at `Lib/ensurepip/_bundled`, removing the existing
   version, and adjusting the versions listed in `Lib/ensurepip/__init__.py`.

[^get-pip-1]: If the release dropped the support of an obsolete Python version
  `M.m`, a new `M.m/get-pip.py` needs to be published: update the `all` task
  from `tasks/generate.py` in the [get-pip repository][get-pip] and make a pull
  request to the [psf-salt repository][psf-salt] to add the new `get-pip.py`
  (and its directory) to `salt/pypa/bootstrap/init.sls`.

[^get-pip-2]: If the `get-pip.py` script needs to be updated due to changes in
  pip internals and if the last `M.m/get-pip.py` published still uses the
  default template, make sure to first duplicate `templates/default.py` as
  `templates/pre-YY.N.py` before updating it and specify in `tasks/generate.py`
  that `M.m/get-pip.py` now needs to use `templates/pre-YY.N.py`.

[get-pip]: https://github.com/pypa/get-pip/
[psf-salt]: https://github.com/python/psf-salt

#### Bugfix releases

Sometimes, we need to release a bugfix release of the form `YY.N.Z+1`. In
order to create one of these the changes should already be merged into the
`master` branch.

1. Create a new `release/YY.N.Z+1` branch off of the `YY.N` tag using the
   command `git checkout -b release/YY.N.Z+1 YY.N`.
1. Cherry pick the fixed commits off of the `master` branch, fixing any
   conflicts.
1. Run `nox -s prepare-release -- YY.N.Z+1`.
1. Merge master into your release branch and drop the news files that have been
   included in your release (otherwise they would also appear in the `YY.N+1`
   changelog)
1. Push the `release/YY.N.Z+1` branch to github and submit a PR for it against
   the `master` branch and wait for the tests to run.
1. Once tests run, merge the `release/YY.N.Z+1` branch into master, and follow
   the above release process starting with step 4.
