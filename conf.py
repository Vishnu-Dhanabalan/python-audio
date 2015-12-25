import sphinx_bootstrap_theme

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

master_doc = 'index'

project = 'python-audio'
author = 'Matthias Geier'
copyright = 'CC0 http://creativecommons.org/publicdomain/zero/1.0/'

exclude_patterns = ['_build', '**.ipynb_checkpoints']

source_suffix = ['.rst', '.ipynb']
source_parsers = {'ipynb': 'nbsphinx.NotebookParser'}

html_title = project
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'navbar_title': project,
    'navbar_site_name': 'Topics',
    'navbar_pagenav_name': 'This Page',
    #'navbar_fixed_top': 'false',
    'source_link_position': 'none',
    #'bootswatch_theme': 'cosmo',
    #'bootswatch_theme': 'lumen',
    #'bootswatch_theme': 'sandstone',
    'bootswatch_theme': 'spacelab',
}

latex_elements = {
    'papersize': 'a4paper',
}

latex_documents = [
    (master_doc, 'python-audio.tex', project, author, 'howto'),
]
