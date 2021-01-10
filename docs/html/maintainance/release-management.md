# Release Management

## Release Cadence

The pip project has a release cadence of releasing whatever is on ``master``
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

## Always be ready for release

Since releases are made direct from the ``master`` branch, it is essential
that ``master`` is always in a releasable state.

It is acceptable to merge PRs that partially implement a new feature, but only
if the partially implemented version is usable in that state (for example, with
reduced functionality or disabled by default).

In the case where a merged PR is found to need extra work before being
released, the release manager always has the option to back out the partial
change prior to a release. The PR can then be reworked and resubmitted for the
next release.

## Making releases

### Release manager

Every pip release has a release manager. The main responsibility of the release 
manager is to coordinate:

- deciding whether a change needs additional work before being released
- publishing of the release
- communicating about the publication of the release to the community

The release manager will be a member of the pip team, usually someone with
commit access to the project. Picking a release manager for a certain release
is via concensus amongst pip's committers.

### Release process

```{note}
There is an ongoing effort to further automate our release process:
{issue}`2314`. Notably, in July 2020, @pradyunsg listed the exact commands he
has to run for a normal release [here](https://github.com/pypa/pip/issues/8511#issuecomment-665414625).
```
