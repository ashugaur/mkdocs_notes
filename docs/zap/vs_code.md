---
title: Visual studio code
hide:
    # - navigation
    - toc
    - footer
---

## Keyboard shortcuts

!!! keyboard-outline "keyboard shortcuts"

    {{ read_excel('docs/tables/keyboard_shortcuts.xlsx', sheet_name='vscode', engine='openpyxl') }}

## Markmap

To generate mindmaps

## Settings

??? cog-outline "extensions.codemap"

    [marketplace](https://marketplace.visualstudio.com/items?itemName=oleg-shilo.codemap){target="_blank}
    `settings → ctrl+shift+p\settings.json`<br>
    [`adding custom mappers`](https://github.com/oleg-shilo/codemap.vscode/wiki/Adding-custom-mappers){target="_blank"}<br>
    [`hide run cell command`](https://stackoverflow.com/questions/55392171/is-there-a-way-to-remove-jupyter-run-cell-buttons-in-visual-studio-code){target="_blank"}

    ```javascript
    {
        "editor.accessibilitySupport": "off",
        "workbench.startupEditor": "none",
        "security.workspace.trust.untrustedFiles": "open",
        "codemap.py": [

            {
                "pattern": "(?<![^\\r\\n\\t\\f\\v .])class (.*?)[(|:]",
                "clear": "class|:|\\)|\\(",
                "prefix": "",
                "role": "class",
                "icon": "class"
            },
            {
                "pattern": "def (.*?)[(|:]",
                "clear": "def|:|\\(|\\)",
                "suffix": "()",
                "role": "function",
                "icon": "function"
            },
            {
                "pattern": "#%% (.*)",
                "clear": "#%%",
                "role": "cell",
                "icon": "document"
            },
            {
                "pattern": "#### (.*)",
                "clear": "####",
                "prefix": "┣━",
                "role": "block",
                "icon": "block"
            },
            {
                "pattern": "# (.*)",
                "clear": "#",
                "prefix": "┃",
                "role": "comment",
                "icon": "comment"
            }
        ],
        "codemap.sql": [

            {
                "pattern": "(?<![^\\r\\n\\t\\f\\v .])class (.*?)[(|:]",
                "clear": "class|:|\\)|\\(",
                "prefix": "",
                "role": "class",
                "icon": "class"
            },
            {
                "pattern": "def (.*?)[(|:]",
                "clear": "def|:|\\(|\\)",
                "suffix": "()",
                "role": "function",
                "icon": "function"
            },
            {
                "pattern": "/\\*([\\s\\S]*?)\\*/",
                "clear": "\/\\*|\\*\\/",
                "role": "cell",
                "icon": "document"
            },
            {
                "pattern": "-- (.*)",
                "clear": "-- ",
                "role": "comment",
                "icon": "comment"
            },
            {
                "pattern": "# (.*)",
                "clear": "# ",
                "role": "comment",
                "icon": "comment"
            },
            {
                "pattern": "// (.*)",
                "clear": "// ",
                "role": "comment",
                "icon": "comment"
            },
        ]
        ,
        "workbench.colorTheme": "Material Theme",
        "workbench.editor.enablePreview": false,
        "[python]": {
            "editor.formatOnType": true
        },
        "jupyter.interactiveWindow.codeLens.enable": false
    }
    ```


