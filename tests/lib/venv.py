import shutil
import sys
import textwrap
import venv
from pathlib import Path
from types import SimpleNamespace
from typing import Optional


class VirtualEnvironment:
    def __init__(self, *, location: Path) -> None:
        self._location = location

        self._template: Optional["VirtualEnvironment"] = None
        self._ctx: Optional[SimpleNamespace] = None

    @classmethod
    def from_template(
        cls,
        *,
        location: Path,
        template: "VirtualEnvironment",
    ) -> "VirtualEnvironment":
        assert template.created, "cannot create from an uncreated parent"
        obj = cls(location=location)
        obj._template = template
        obj.create()
        return obj

    def __repr__(self) -> str:
        return (
            f"<VirtualEnvironment: created={self.created}, location={self._location}>"
        )

    @property
    def created(self) -> bool:
        return self._ctx is not None

    @property
    def location(self) -> Path:
        return self._location

    @property
    def site_packages_path(self) -> Path:
        """Determine the location of site-packages.

        This uses the same paths as `venv` (as of CPython 3.10.4, although it's been
        that way in CPython since the introduction of `venv`).
        """
        assert self._ctx, "test venv not created: can't locate site-packages"

        # TODO: PyPy?

        if sys.platform == "win32":
            return Path(self._ctx.env_dir) / "Lib" / "site-packages"

        return (
            Path(self._ctx.env_dir)
            / "lib"
            / f"python{sys.version_info.major}.{sys.version_info.minor}"
            / "site-packages"
        )

    @property
    def bin_path(self) -> Path:
        """Determine the location of site-packages.

        This uses the same paths as `venv` (as of CPython 3.10.4, although it's been
        that way in CPython since the introduction of `venv`).
        """
        assert self._ctx is not None, "test venv not created: can't locate bin"

        return Path(self._ctx.bin_path)

    def create(self) -> None:
        self._ctx = (
            self._create_from_scratch()
            if self._template is None
            else self._create_from_template()
        )
        self._protect_base_prefix()

    def _create_from_scratch(self) -> SimpleNamespace:
        builder = venv.EnvBuilder(system_site_packages=True)
        context = builder.ensure_directories(self._location)

        builder.create_configuration(context)
        builder.setup_python(context)

        return context

    def _create_from_template(self) -> SimpleNamespace:
        assert self._template
        assert self._template._ctx

        shutil.copytree(self._template._location, self._location, symlinks=True)

        builder = venv.EnvBuilder()
        context = builder.ensure_directories(self._location)

        return context

    def _protect_base_prefix(self) -> None:
        sitecustomize = self.site_packages_path / "sitecustomize.py"
        sitecustomize.write_text(
            textwrap.dedent(
                f"""
                import os
                import sys
                import site
                import traceback

                try:
                    # We won't want to modify the actual base prefix, or pick up things
                    # from there.
                    paths_to_remove = site.getsitepackages([sys.base_prefix])
                    for rm_path in paths_to_remove:
                        for path in sys.path:
                            if rm_path == path:
                                sys.path.remove(path)
                                break
                except Exception:
                    traceback.print_exc()
                """
            )
        )

    def clear(self) -> None:
        shutil.rmtree(self.site_packages_path)
        self.site_packages_path.mkdir()

    def move(self, *, to: Path) -> None:
        shutil.move(self._location, to)
        self._location = to

    def disable_global_and_user_site_packages(self) -> None:
        assert self._ctx, "test venv not created: can't disable global/user site"
        pyvenv = Path(self._ctx.env_dir) / "pyvenv.cfg"

        pyvenv_contents = pyvenv.read_text()
        assert "include-system-site-packages = true" in pyvenv_contents

        pyvenv.write_text(
            pyvenv_contents.replace(
                "include-system-site-packages = true",
                "include-system-site-packages = false",
            )
        )
