---
title: python
hide:
    # - navigation
    # - toc
    - footer
---

## changing jupyter notebook path

!!! pan-right ""

    [Source](https://stackoverflow.com/questions/15680463/change-ipython-jupyter-notebook-working-directory){target="_blank"}

    - Open Conda if Anaconda else PowerShell in Admin mode
        - Go to Path: C:\Users\your_user_name\.jupyter
        - run: `jupyter notebook --generate-config`
        - open: `jupyter_notebook_config.py`
        - search for `c.NotebookApp.notebook_dir`
        - uncomment (remove #) or change path to `c.NotebookApp.notebook_dir = 'C:/your/new/path'`
            - E.g. `c.NotebookApp.notebook_dir = 'C:/Users/Ashutosh Gaur'`
    


## changing jupyter launch applicaiton to edge

!!! pan-right ""

    `~does not work, change default browser`

    Better take the hosting path from jupyter console at it is launched.

    [Source](https://stackoverflow.com/questions/60504844/how-to-make-jupyter-able-to-launch-ms-edge){target="_blank"}

    - Open Conda if Anaconda else PowerShell in Admin mode
        - Go to Path: C:\Users\your_user_name\.jupyter
        - run: `jupyter notebook --generate-config`
        - open: `jupyter_notebook_config.py`
        - Modify #c.NotebookApp.browser = '' to `c.NotebookApp.browser = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s'`


## Install multiple packages using pip

<iframe
  src="edupunk\software\settings\python\requirements.txt"
  style="width:100%; height:60px;" frameborder="0" allowfullscreen
></iframe>

!!! pan-right ""

    1. Create a text file `requirements.txt` containing 1 package name in each line as above
    2. Run: pip install -r requirements.txt



## Mkdocs commands

!!! pan-right ""

    ```py title="upgrade pip"
    python.exe -m pip install --upgrade pip
    ```

    ```py title="build"
    mkdocs build
    ```

    ```py title="build alternate"
    python -m mkdocs build
    ```

    ```py title="install packages"
    pip install -r "<filename.txt>"
    ```




## start server

!!! pan-right ""

        `python -m http.server`

		pip cache purge




[^0]: [Tutorials](https://realpython.com/){target="_blank"},



