# Sphinx configuration for the Sphinx-Needs Starter template.
#
# This is a STARTER file: the comments marked "← customize" point at the
# values you are expected to change for your own project. Everything else
# can usually stay as-is.
#
# Full Sphinx reference: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "My Documentation Project"   # ← customize: your project's name
author = "Your Organization"            # ← customize: your name or org
copyright = "2026, Your Organization"   # ← customize: year + holder
release = "0.1.0"                       # ← customize: your project's version

# -- General configuration ---------------------------------------------------

# Sphinx extensions. `sphinx_needs` adds requirements management; `ubt_sphinx`
# provides the `ubtrace` builder (sphinx-build -b ubtrace).
extensions = [
    "sphinx_needs",
    "ubt_sphinx",
    # Diagrams (rendered during the build):
    "sphinx.ext.graphviz",      # .. graphviz:: / .. digraph::  (needs `dot`)
    "sphinxcontrib.plantuml",   # .. uml::                      (needs `plantuml` + Java)
    "sphinxcontrib.mermaid",    # .. mermaid::                  (rendered client-side for HTML)
]

# -- HTML output -------------------------------------------------------------

# The Furo theme: clean, responsive docs theme.
html_theme = "furo"

# Optional branding. Uncomment and point at files under source/_static/.
# The ubtrace builder emits an advisory warning when these are unset — that
# warning is harmless; set them when you have brand assets.
# html_logo = "_static/logo.png"        # ← optional
# html_favicon = "_static/favicon.ico"  # ← optional

# -- Sphinx-Needs configuration ----------------------------------------------

# Need types (req/spec/test, IDs, etc.) are NOT defined here. They live in
# `ubproject.toml` at the repo root, which is the single source of truth shared
# with the `ubc` linter. Sphinx-Needs loads them via `needs_from_toml`.
#
# Path is relative to THIS file (source/conf.py), so the repo-root TOML is one
# directory up.
#
# To add or change need types, edit `ubproject.toml`, not this file.
# Docs: https://sphinx-needs.readthedocs.io
needs_from_toml = "../ubproject.toml"

# -- Diagram configuration ---------------------------------------------------

# Graphviz: render to SVG (crisp, scalable) instead of the default PNG.
graphviz_output_format = "svg"

# PlantUML: invoked via the `plantuml` command on PATH. The dev container
# installs it (with Java); on a bare host install PlantUML + a JRE yourself.
# To use a JAR directly instead, set e.g.:
#   plantuml = "java -jar /path/to/plantuml.jar"
plantuml = "plantuml"
plantuml_output_format = "svg"

# Mermaid renders client-side in the browser for the HTML build, so no extra
# binary is required. For static image export (e.g. PDF) install mermaid-cli
# (`mmdc`) and set `mermaid_output_format`.

# -- ubtrace builder configuration -------------------------------------------

# Required by the `ubtrace` builder (from `ubt_sphinx`). All three are strings.
ubtrace_organization = "my-org"      # ← customize: your organization slug
ubtrace_project = "my-product"       # ← customize: your project slug
ubtrace_version = "v1"               # ← customize: the traced version
