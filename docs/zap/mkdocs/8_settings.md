---
title: Settings
hide:
    # - navigation
    # - toc
    - footer
---

# Settings

## .md page

!!! pan-right ""

    ```yaml
    ---
    title: page_title
    title: '' #hide page from site
    description: page_description
    author: AG
    date: 2023-04-13
    tags: my, page, tags
    image: /path/to/image.jpg
    nav_order: 1
    hide: false

    hide:
        # - navigation
        # - toc
        - footer

    search:
    exclude: true

    glightbox: false
    ---
    ```


## Spellcheck

!!! pan-right ""

    [mkdocs-Spellcheck](https://github.com/pawamoy/mkdocs-spellcheck){target="_none"}


## Load .aspx pages without server

!!! pan-right ""

    1. Install XAMPP on your computer. XAMPP is a free and open-source cross-platform web server solution that includes Apache, MySQL, PHP, and Perl.
    2. Launch the XAMPP Control Panel and start the Apache web server.
    3. Create a new folder inside the "htdocs" folder in the XAMPP installation directory. This folder will be used to store your ASPX page.
    4. Place your ASPX page inside the folder you just created.
    5. Open a web browser and navigate to "http://localhost/foldername/mypage.aspx". Replace "foldername" with the name of the folder you created in step 3, and "mypage.aspx" with the name of your ASPX page.


## [Export to html](https://timvink.github.io/mkdocs-print-site-plugin/how-to/export-HTML.html){target="_blank"}

!!! pan-right ""

    Template stored in `markdown\mkdocs_template`.

    ```markdown
    mkdocs build

    cd site/

    # when mkdocs.yml has use_directory_urls: true (the default)
    htmlark print_page/index.html -o standalone.html

    # when mkdocs.yml has use_directory_urls: false
    htmlark index.html -o standalone.html
    ```



## Offline Search

??? pan-right "old, not relevant"

    [https://github.com/wilhelmer/mkdocs-localsearch](https://github.com/wilhelmer/mkdocs-localsearch){target="_none"}

    1. Install the plugin using pip: `pip install mkdocs-localsearch`
    2. Activate the plugin in `mkdocs.yml`, in addition to the `search` plugin:
    ```
    plugins:
        - search
        - localsearch
    ```
    3. Make sure that the `use_directory_urls` setting is set to `false` in `mkdocs.yml` to have filenames in the URL (required when using the file:/// protocol).
    4. Add a `custom_dir` entry to the `theme` section in `mkdocs.yml`:
    ```
    theme:
        name: material
        custom_dir: theme
    ```
    5. Create a new file, save it in your project dir as `theme/main.html`, and add the following content:
    ```
    {% extends "base.html" %}
    {% block config %}
    {{ super() }}
    {% if "localsearch" in config["plugins"] %}
    <script src="https://unpkg.com/iframe-worker/polyfill"></script>
    <script src="{{ 'search/search_index.js' | url }}"></script>
    {% endif %}
    {% endblock %}
    ```
    **Note:** Don't use the `extra_javascript` option in `mkdocs.yml` to add the two scripts above. Scripts referenced via `extra_javascript` are placed at the bottom of the HTML page, i.e., after the search implementation, which is too late.
    6. If your documentation should work **offline**, i.e., without internet access:
        - Open [this file](https://unpkg.com/iframe-worker/polyfill){target="_none"} and save it as `iframe-worker.js` in your `docs_dir`.
        Example path: `docs/assets/javascripts/iframe-worker.js`
        - Edit theme/main.html and change the following line:
    ```
    <script src="https://unpkg.com/iframe-worker/polyfill"></script>
    ```
        to this:
    ```
    <script src="{{ 'assets/javascripts/iframe-worker.js' | url }}"></script>
    ```
