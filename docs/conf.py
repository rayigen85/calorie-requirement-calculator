"""Sphinx configuration."""
project = "Calorie Requirement Calculator"
author = "Raymond Baruth"
copyright = "2022, Raymond Baruth"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
