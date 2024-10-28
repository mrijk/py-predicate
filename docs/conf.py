# -- Project information -----------------------------------------------------

project = "py-predicate"
author = "Maurits Rijk"
copyright = "2024, " + author

# The full version, including alpha/beta/rc tags
version = release = "0.1"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    # 'sphinx_copybutton',
]

pygments_style = "sphinx"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The document name of the “master” document, that is,
# the document that contains the root toctree directive.
# Default is 'index', we set it here for supporting Sphinx<2.0
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# A boolean that decides whether codeauthor and sectionauthor directives
# produce any output in the built files.
show_authors = True
