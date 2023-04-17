# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.append(os.path.abspath('.'))
import metamodel

# -- Project information

project = 'ReConf 2023 X-As-Code'
copyright = '2023, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.1.0'

# -- General configuration

on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    #'sphinx.ext.intersphinx',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# -- Options for HTML output

html_theme = 'alabaster'
# html_theme = 'sphinx_material'
# html_theme = 'sphinx_rtd_theme'

html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# sphinxcontrib.plantuml configuration

# local_plantuml_path is from https://github.com/useblocks/sphinx-needs/blob/master/docs/conf.py
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    # Deactivated using rtd plantuml version as it looks quite old.
    # plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

plantuml_output_format = 'svg'

# sphinx_needs configuration

needs_build_json = True

needs_id_regex = metamodel.needs_id_regex

needs_types = metamodel.needs_types

needs_extra_options = metamodel.needs_extra_options

needs_extra_links = metamodel.needs_extra_links

needs_services = metamodel.needs_services

needs_layouts = metamodel.needs_layouts

needs_functions = metamodel.needs_functions

needs_global_options = metamodel.needs_global_options

needs_warnings = metamodel.needs_warnings


# sphinx.ext.intersphinx configuration

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']
