"""Configuration file for pip's documentation."""

import glob
import os
import pathlib
import re
import sys

# Add the docs/ directory to sys.path, because pip_sphinxext.py is there.
docs_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, docs_dir)

# -- General configuration ------------------------------------------------------------

extensions = [
    # first-party extensions
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # our extensions
    "pip_sphinxext",
    # third-party extensions
    "myst_parser",
    "sphinx_panels",
    "sphinx_inline_tabs",
    "sphinxcontrib.towncrier",
]

# General information about the project.
project = "pip"
copyright = "2008-2020, PyPA"

# Find the version and release information.
# We have a single source of truth for our version number: pip's __init__.py file.
# This next bit of code reads from it.
file_with_version = os.path.join(docs_dir, "..", "src", "pip", "__init__.py")
with open(file_with_version) as f:
    for line in f:
        m = re.match(r'__version__ = "(.*)"', line)
        if m:
            __version__ = m.group(1)
            # The short X.Y version.
            version = ".".join(__version__.split(".")[:2])
            # The full version, including alpha/beta/rc tags.
            release = __version__
            break
    else:  # AKA no-break
        version = release = "dev"

print("pip version:", version)
print("pip release:", release)

# -- Options for intersphinx ----------------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pypug': ('https://packaging.python.org', None),
}

# -- Options for extlinks -------------------------------------------------------------

extlinks = {
    "issue": ("https://github.com/pypa/pip/issues/%s", "#"),
    "pull": ("https://github.com/pypa/pip/pull/%s", "PR #"),
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# -- Options for towncrier_draft extension --------------------------------------------

towncrier_draft_autoversion_mode = "draft"  # or: 'sphinx-release', 'sphinx-version'
towncrier_draft_include_empty = True
towncrier_draft_working_directory = pathlib.Path(docs_dir).parent
# Not yet supported: towncrier_draft_config_path = 'pyproject.toml'  # relative to cwd

# -- Options for myst-parser ----------------------------------------------------------

myst_enable_extensions = ["deflist"]
myst_url_schemes = ("http", "https", "mailto")
myst_heading_anchors = 2

# -- Options for HTML -----------------------------------------------------------------

html_theme = "furo"
html_title = f"{project} documentation v{release}"
html_css_files = ["custom.css"]
html_static_path = ["_static"]

# Disable the generation of the various indexes
html_use_modindex = False
html_use_index = False

# -- Options for Manual Pages ---------------------------------------------------------


# List of manual pages generated
def determine_man_pages():
    """Determine which man pages need to be generated."""

    def to_document_name(path, base_dir):
        """Convert a provided path to a Sphinx "document name"."""
        relative_path = os.path.relpath(path, base_dir)
        root, _ = os.path.splitext(relative_path)
        return root.replace(os.sep, "/")

    # Crawl the entire man/commands/ directory and list every file with appropriate
    # name and details.
    man_dir = os.path.join(docs_dir, "man")
    raw_subcommands = glob.glob(os.path.join(man_dir, "commands/*.rst"))
    if not raw_subcommands:
        raise FileNotFoundError(
            "The individual subcommand manpages could not be found!"
        )

    retval = [
        ("index", "pip", "package manager for Python packages", "pip developers", 1),
    ]
    for fname in raw_subcommands:
        fname_base = to_document_name(fname, man_dir)
        outname = "pip-" + fname_base.split("/")[1]
        description = "description of {} command".format(outname.replace("-", " "))

        retval.append((fname_base, outname, description, "pip developers", 1))

    return retval


man_pages = determine_man_pages()
