# Vendoring Management

As detailed in {doc}`../../policies/vendoring`, pip's dependencies are vendored
and shipped as a part of pip.

The vendoring process is managed using the {pypi}`vendoring` tool, which has
only one intended user, at the time of writing: pip.

## Synchronising vendored libraries

```
nox -s vendoring
```

This command will run `vendoring sync`, which will do the following:

- Cleanup any existing vendored files.
- Vendor the dependencies, as configured via `pyproject.toml`.
- Generate typing stubs, for the vendored dependencies.
- Fetch and include the licenses, for the vendored dependencies.

## Updating vendored libraries

```
nox -s vendoring -- --upgrade
```

This command will read through each line in `src/pip/_vendor/vendor.txt`
and run `vendoring update . {name}` for each package name in that
listing. If there's a newer version available, this will be followed by
`vendoring sync` and creating a dedicated commit.

To exclude a certain package upgrade, you can typically perform an interactive
rebase (typically `git rebase -i origin/main`) and remove the corresponding
commit.
