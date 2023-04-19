---
title: Mkdocs
hide:
    # - navigation
    # - toc
    # - footer
---



## Install

!!! cog-outline "Dependencies"

	[Python](https://www.python.org/){target="_blank"}, packages from [requirements.txt](docs/requirements_mkdocs.txt){target="_blank"}

		pip install -r "<path-for-requirements_mkdocs.txt>"



## Run

!!! console-line "Powershell"

	```yaml linenums="1"
	Go to project folder 	: cd <folder-path>
	Create new project	 	: mkdocs new <project-name>
	Open project folder	 	: cd <project-name>
	Copy simple settings to	: project-name\mkdocs.yml
	Edit *.md files in  	: <project-name\docs>
	Serve project folder 	: mkdocs serve or python -m mkdocs serve
	Build project folder 	: mkdocs build or python -m mkdocs build
	```

	=== "simple settings"
		```yaml
		site_name	: Test
		site_author	: AG
		site_url	: https://test.com/
		```
	=== "complex settings"
		```
		# project information
		site_name			: default_v2
		site_author			: AG
		site_description	: "testing"
		site_url			: https://default_v2.com/
		use_directory_urls	: false

		# copyright
		# copyright: Copyright test

		theme:
			name: material
			palette:
				# light mode
				- media: "(prefers-color-scheme: light)"
				scheme: default
				toggle:
					icon: material/toggle-switch
					name: Switch to dark mode
				accent: orange
				primary: white

				# dark mode
				- media: "(prefers-color-scheme: dark)"
				scheme: slate
				toggle:
					icon: material/toggle-switch-off-outline
					name: Switch to light mode
				accent: orange
				primary: black

			font: false
				# text: Roboto
				# code: Roboto Mono

			icon:
				#logo: material/library-outline
				#logo: material/airplane
				#logo: material/layers-outline
				logo: octicons/book-24 # website logo
				admonition:
					info: material/code-tags-check # change icon
					question: material/lock-question
					todo: fontawesome/solid/question

			# logo: img/website_logo.png      #custom website logo
			# favicon: img/website_logo.png   #custom website favicon

			features:

				- header.autohide

				- navigation.tabs
				- navigation.sections
				# - navigation.tabs.sticky
				- navigation.top
				- navigation.footer
				- navigation.tracking
				- navigation.indexes
				# - navigation.expand

				- content.tabs.link
				- content.code.copy
				- content.code.annotate

				- toc.follow # experimental
				# - toc.integrate

				- search.suggest
				- search.highlight
				- search.share

		plugins:

			# - autolinks
			- plotly

			- glightbox:
			touchNavigation: true
			loop: false
			effect: zoom
			slide_effect: slide
			width: 100%
			height: auto
			zoomable: true
			draggable: true
			skip_classes:
				- skip-lightbox #usage: ![Hallstatt, Austria](../images/gallery/blueswen-hallstatt.jpeg){ .skip-lightbox }
			auto_caption: false
			caption_position: bottom

			- table-reader

			- mkdocs-video:
				# is_video: True
				# video_autoplay: True
				css_style:
				width: "30%"
				height: "22.172vw"

			# works but not in effect
			# - enumerate-headings:
			#     toc_depth: 6
			#     strict: true
			#     increment_across_pages: false
			#     exclude:
			#         - index.md
			#         - another_page.md
			#         - reveries.md
			#         - template/* #exclude entire folder

			- markdown-exec

			# hooks:
			# - mkdocs-simple-hooks:
			#     hooks:
					# on_files: 'hooks:on_files'

			- minify:
				minify_html: true
				minify_js: true
				minify_css: true
				htmlmin_opts:
					remove_comments: true
				cache_safe: true

			- search
			- offline:
				enabled: !ENV [OFFLINE, true]


			- print-site:
				enabled: false
				add_to_navigation: false
				print_page_title: 'Print Site'
				add_print_site_banner: false
				# Table of contents
				add_table_of_contents: true
				toc_title: 'Table of Contents'
				toc_depth: 6
				# Content-related
				add_full_urls: false
				enumerate_headings: false
				# enumerate_headings_depth: 6 #default is 6
				# enumerate_figures: false
				add_cover_page: false
				cover_page_template: ""
				path_to_pdf: ""
				include_css: true
				exclude:
					# - index.md
					# - subfolder/page.md
					# - folder/*

		markdown_extensions:

			- abbr
			- footnotes

			- attr_list
			- def_list
			- md_in_html

			- pymdownx.superfences:
				#run code within markdown
				custom_fences:
				- name: python
				class: python
				validator: !!python/name:markdown_exec.validator
				format: !!python/name:markdown_exec.formatter
				# ...one fence for each language we support:
				# bash, console, md, markdown, py, python, pycon, sh, tree

				- name: plotly
				class: mkdocs-plotly
				format: !!python/name:mkdocs_plotly_plugin.fences.fence_plotly

			- admonition
			- pymdownx.details
			- pymdownx.tabbed:
				alternate_style: true
			- pymdownx.inlinehilite
			- pymdownx.smartsymbols
			- pymdownx.keys

			- pymdownx.highlight:
				pygments_lang_class: true
				# auto_title: true
				linenums: false
				linenums_style: pymdownx-inline
				anchor_linenums: true
				line_spans: __span
				pygments_lang_class: true

			- pymdownx.betterem:
				smart_enable: all
			- pymdownx.caret
			- pymdownx.mark
			- pymdownx.tilde
			- pymdownx.critic
			- pymdownx.emoji:
				emoji_index: !!python/name:materialx.emoji.twemoji
				emoji_generator: !!python/name:materialx.emoji.to_svg
			- pymdownx.snippets:
				auto_append:
					- includes/abbreviations.md
			- pymdownx.magiclink
			- pymdownx.arithmatex:
				generic: true
			- pymdownx.tasklist:
				custom_checkbox: true
			- tables
			- meta
			- toc:
				title: Table of contents
				permalink: true #enable anchor
				# permalink: '#' #change anchor
				permalink_title: Anchor link to this section for reference
				toc_depth: 5
				baselevel: 1

		# extra:
		#     generator: false # remove made with mkdocs
			# social: # add social media icons (https://squidfunk.github.io/mkdocs-material/setup/setting-up-the-footer/#generator-notice)
			#   - icon: fontawesome/brands/linkedin
			#     link: https://www.linkedin.com/in/haoda-li/
			#   - icon: fontawesome/brands/github
			#     link: https://github.com/haoda-li/

		extra_javascript:
			- assets/javascripts/mathjax.js
			- https://polyfill.io/v3/polyfill.min.js?features=es6
			- https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
			- https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js
			- javascripts/tablesort.js

		extra_css:
			- stylesheets/extra.css
		```




## Reference

!!! bookmark-outline "&nbsp;"

	!!! border-radius "Resources"

		:	[`discussion`](https://github.com/squidfunk/mkdocs-material/discussions){target="_blank"}
			[`material for MkDocs`](https://squidfunk.github.io/mkdocs-material/setup/){target="_blank"}
			[`MkDocs MagicSpace`](https://mkdocs-magicspace.alnoda.org/tutorials/get-started/){target="_blank"}
			[`material icons`](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#icon-bundled){target="_blank"}<br>
			[`admonision icons`](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#admonition-icons){target="_blank"}<br>
			[`alchemy symbols`](https://unicode-table.com/en/blocks/alchemical-symbols/){target="_blank"}
			[`100+ unicode symbols`](https://tutorialzine.com/2014/12/you-dont-need-icons-here-are-100-unicode-symbols-that-you-can-use){target="_blank"}
			[`HTML symbols`](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references){target="_blank"}
			[`pictographs`](https://unicode-table.com/en/blocks/supplemental-symbols-and-pictographs/){target="_blank"}<br>
			[`hacks`](https://www.markdownguide.org/hacks/){target="_blank"}<br>


	!!! border-radius "Extensions"

		:	[`plugins`](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins){target="_blank"}
			[`pymdown-extensions`](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/){target="_blank"}
			[`abinit`](https://docs.abinit.org/developers/markdown/#markdown-quick-reference){target="_blank"}<br>


	!!! border-radius "To test"

		:	[`MkDocs+`](http://bwmarrin.github.io/MkDocsPlus/){target="_blank"}
			[`print-to-pdf`](https://www.codeinsideout.com/blog/site-setup/print-to-pdf/){target="_blank"}
			[`md-to-pdf`](https://www.npmjs.com/package/md-to-pdf){target="_blank"}
			[`mkdocs-pdf-export-plugin`](https://github.com/zhaoterryy/mkdocs-pdf-export-plugin){target="_blank"}
			[`hooks`](https://github.com/aklajnert/mkdocs-simple-hooks){target="_blank"}
			[`hooks.aspx`](https://github.com/mkdocs/mkdocs/discussions/2967){target="_blank"}
			[`macros`](https://github.com/fralau/mkdocs_macros_plugin){target="_blank"}
			[`print code results`](https://pawamoy.github.io/markdown-exec/){target="_blank"}
			[`side notes`](https://material-tufte.ale.sh/){target="_blank"}
			[`index headings`](https://pypi.org/project/mkdocs-enumerate-headings-plugin/){target="_blank"}
			[`svg inline`](https://pypi.org/project/mkdocs-plugin-inline-ext-svg/0.1.2/){target="_blank"}
			[`bulid documentaiton from source`](https://mkdocstrings.github.io/){target="_blank"}
			[`import statement`](https://github.com/Rj40x40/mkdocs-import-statement-plugin){target="_blank"}
			[`vegalite charts plugin`](https://timvink.github.io/mkdocs-charts-plugin/demo/){target="_blank"}
			[`glightbox, image library`](https://blueswen.github.io/mkdocs-glightbox/caption/caption/){target="_blank"}
			[`glossary plugin`](https://github.com/AngryMane/mkdocs-glossary-plugin){target="_blank"}
			[`d3blocks`](https://github.com/d3blocks/d3blocks){target="_blank"}
			[`d3graph`](https://erdogant.github.io/d3graph/pages/html/index.html){target="_blank"}
			[`sphinx-gallery`](https://smarie.github.io/mkdocs-gallery/){target="_blank"}
			[`docmark`](https://yakworks.github.io/docmark/){target="_blank"}


	!!! border-radius "Themes"

		:	[`Dracula`](https://dracula.github.io/mkdocs/){target="_blank"} [`real dracula`](https://gist.github.com/jonaprieto/32e6f0cb82ed2897ae76fee989202647){target="_blank"}


	!!! border-radius "Alternates to MkDocs"

		:	[`Markdoc`](https://github.com/markdoc/markdoc){target="_blank"}
			[`Pandoc`](https://pandoc.org/){target="_blank"}
			[`R Markdown`](https://rmarkdown.rstudio.com/){target="_blank"}
			[`Sphinx`](https://www.sphinx-doc.org/en/master/){target="_blank"}
			[`Pydata-Sphinx`](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html){target="_blank"}

