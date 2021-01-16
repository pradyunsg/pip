# VCS Support

pip supports installing from various version control systems (VCS).
This support is controlled using URL prefixes:

- Git -- `git+`
- Mercurial -- `hg+`
- Subversion -- `svn+`
- Bazaar -- `bzr+`

```{note}
This support requires a working executable to be available, for the version
control system being used.
```

## Supported VCS

### Git

pip currently supports cloning over `git`, `git+http`, `git+https`,
`git+ssh`, `git+git` and `git+file`.

[TODO: finish me]

.. warning::

    Note that the use of `git`, `git+git`, and `git+http` is discouraged.
    The former two use `the Git Protocol`_, which lacks authentication, and HTTP is
    insecure due to lack of TLS based encryption.

Here are the supported forms::

    [-e] git+http://git.example.com/MyProject#egg=MyProject
    [-e] git+https://git.example.com/MyProject#egg=MyProject
    [-e] git+ssh://git.example.com/MyProject#egg=MyProject
    [-e] git+file:///home/user/projects/MyProject#egg=MyProject

Passing a branch name, a commit hash, a tag name or a git ref is possible like so::

    [-e] git+https://git.example.com/MyProject.git@master#egg=MyProject
    [-e] git+https://git.example.com/MyProject.git@v1.0#egg=MyProject
    [-e] git+https://git.example.com/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject
    [-e] git+https://git.example.com/MyProject.git@refs/pull/123/head#egg=MyProject

When passing a commit hash, specifying a full hash is preferable to a partial
hash because a full hash allows pip to operate more efficiently (e.g. by
making fewer network calls).

.. _`the Git Protocol`: https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols

### Mercurial

The supported schemes are: `hg+file`, `hg+http`, `hg+https`,
`hg+static-http`, and `hg+ssh`.

Here are the supported forms::

    [-e] hg+http://hg.myproject.org/MyProject#egg=MyProject
    [-e] hg+https://hg.myproject.org/MyProject#egg=MyProject
    [-e] hg+ssh://hg.myproject.org/MyProject#egg=MyProject
    [-e] hg+file:///home/user/projects/MyProject#egg=MyProject

You can also specify a revision number, a revision hash, a tag name or a local
branch name like so::

    [-e] hg+http://hg.example.com/MyProject@da39a3ee5e6b#egg=MyProject
    [-e] hg+http://hg.example.com/MyProject@2019#egg=MyProject
    [-e] hg+http://hg.example.com/MyProject@v1.0#egg=MyProject
    [-e] hg+http://hg.example.com/MyProject@special_feature#egg=MyProject

### Subversion

pip supports the URL schemes `svn`, `svn+svn`, `svn+http`, `svn+https`, `svn+ssh`.

Here are some of the supported forms::

    [-e] svn+https://svn.example.com/MyProject#egg=MyProject
    [-e] svn+ssh://svn.example.com/MyProject#egg=MyProject
    [-e] svn+ssh://user@svn.example.com/MyProject#egg=MyProject

You can also give specific revisions to an SVN URL, like so::

    [-e] svn+svn://svn.example.com/svn/MyProject#egg=MyProject
    [-e] svn+http://svn.example.com/svn/MyProject/trunk@2019#egg=MyProject

which will check out revision 2019.
`@{20080101}` would also check
out the revision from 2008-01-01. You can only check out specific
revisions using `-e svn+...`.

### Bazaar

pip supports Bazaar using the `bzr+http`, `bzr+https`, `bzr+ssh`,
`bzr+sftp`, `bzr+ftp` and `bzr+lp` schemes.

Here are the supported forms::

    [-e] bzr+http://bzr.example.com/MyProject/trunk#egg=MyProject
    [-e] bzr+sftp://user@example.com/MyProject/trunk#egg=MyProject
    [-e] bzr+ssh://user@example.com/MyProject/trunk#egg=MyProject
    [-e] bzr+ftp://user@example.com/MyProject/trunk#egg=MyProject
    [-e] bzr+lp:MyProject#egg=MyProject

Tags or revisions can be installed like so::

    [-e] bzr+https://bzr.example.com/MyProject/trunk@2019#egg=MyProject
    [-e] bzr+http://bzr.example.com/MyProject/trunk@v1.0#egg=MyProject

## Editable VCS installs

VCS projects can be installed in :ref:`editable mode <editable-installs>` (using
the :ref:`--editable <install_--editable>` option) or not.

* For editable installs, the clone location by default is
  `<venv path>/src/SomeProject` in virtual environments, and
  `<cwd>/src/SomeProject` for global installs.
  The :ref:`--src <install_--src>` option can be used to modify this location.
* For non-editable installs, the project is built locally in a temp dir and then
  installed normally. Note that if a satisfactory version of the package is
  already installed, the VCS source will not overwrite it without an
  `--upgrade` flag. VCS requirements pin the package version (specified
  in the `setup.py` file) of the target commit, not necessarily the commit
  itself.
* The :ref:`pip freeze` subcommand will record the VCS requirement specifier
  (referencing a specific commit) if and only if the install is done using the
  editable option.

The "project name" component of the URL suffix `egg=<project name>`
is used by pip in its dependency logic to identify the project prior
to pip downloading and analyzing the metadata. For projects
where `setup.py` is not in the root of project, the "subdirectory" component
is used. The value of the "subdirectory" component should be a path starting
from the root of the project to where `setup.py` is located.

If your repository layout is::

   pkg_dir
   ├── setup.py  # setup.py for package "pkg"
   └── some_module.py
   other_dir
   └── some_file
   some_other_file

Then, to install from this repository, the syntax would be:

.. tab:: Unix/macOS

   .. code-block:: shell

      python -m pip install -e "vcs+protocol://repo_url/#egg=pkg&subdirectory=pkg_dir"

.. tab:: Windows

   .. code-block:: shell

      py -m pip install -e "vcs+protocol://repo_url/#egg=pkg&subdirectory=pkg_dir"
