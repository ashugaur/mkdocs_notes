---
title: Insert
hide:
    # - navigation
    # - toc
    - footer
---


## [Buttons](https://squidfunk.github.io/mkdocs-material/reference/buttons/#buttons){target="_blank"}

!!! pan-right ""

    [Subscribe to our newsletter](#){ .md-button }

    [Send :fontawesome-solid-paper-plane:](mailto: ashutoshgaur@live.com){ .md-button }


## Table of contents

!!! pan-right ""

    ```
    [TOC]
    ```

    ??? pan-right ""

        [TOC]



## Horizontal line

!!! pan-right ""

    ```
    <hr>
    ```
    
    <hr>



## Images

!!! pan-right ""

    ### Relative reference

    !!! pan-right ""

        ```
        ![relative reference](img\relative_reference.png){#id .class width=10% height=10%; loading=lazy}
        ```

        ![relative reference](img\relative_reference.png){#id .class width=10% height=10%; loading=lazy}


    ### Captions

    !!! pan-right ""

        ```
        <figure markdown>![Image title](img/relative_reference.png){ width=30%; loading=lazy }<figcaption>write_image_caption</figcaption></figure>
        ```

        <figure markdown>![Image title](img/relative_reference.png){ width=30%; loading=lazy }<figcaption>write_image_caption</figcaption></figure>


    ### Align right

    !!! pan-right ""

        ```
        ![align_right](img/aurelative_referencehg.png){: .right style="height: 15%; width: 15%; border-radius: 5px;" loading=lazy}
        ```

        ![align_right](img/relative_reference.png){: .right style="height: 15%; width: 15%; border-radius: 5px;" loading=lazy}


    ### Align center

    !!! pan-right ""

        ```
        ![align_center](img/relative_reference.png){: .center style="height: 15%; width: 15%; border-radius: 5px;" loading=lazy}
        ```

        ![align_center](img/relative_reference.png){: .center style="height: 15%; width: 15%; border-radius: 5px;" loading=lazy}



## iFrame

### .txt

```
<iframe
  src="docs/iframe_text.txt"
  style="width:100%; height:60px;" frameborder="0" allowfullscreen
></iframe>
```

<iframe
  src="docs/iframe_text.txt"
  style="width:100%; height:60px;" frameborder="0" allowfullscreen
></iframe>




### .pdf

```
<iframe
  src="docs/hypothesis_testing_useful table.pdf" frameborder="0" allowfullscreen
  style="width:100%; height400px;"
></iframe>
```

<iframe
  src="docs/hypothesis_testing_useful table.pdf" frameborder="0" allowfullscreen
  style="width:100%; height:400px;" 
></iframe>



### .html

```
<iframe
  src="docs/search_results.html"
  style="width:100%; height:500px;" frameborder="0" allowfullscreen
></iframe>
```

<iframe
  src="docs/search_results.html"
  style="width:100%; height:100px;" frameborder="1" allowfullscreen
></iframe>





### Youtube

```
<div class="video-wrapper">
  <iframe width=60% height=40% src="https://www.youtube.com/embed/LXb3EKWsInQ" frameborder="0" allowfullscreen></iframe>
</div>
```

<div class="video-wrapper">
  <iframe width=60% height=40% src="https://www.youtube.com/embed/LXb3EKWsInQ" frameborder="0" allowfullscreen></iframe>
</div>




## Tweet

Copy paste the embed text form twitter.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">In the meantime, semaglutide (aka Ozempic/Rybelsus) appears to be effective in appetite control with minor side effects</p>&mdash; Elon Musk (@elonmusk) <a href="https://twitter.com/elonmusk/status/1518222204097413122?ref_src=twsrc%5Etfw">April 24, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>





## Table

### Markdown table

!!! pan-right ""

    ```
    | Column 1 Header | Column 2 Header | Column 3 Header |
    | --------------- | --------------- | --------------- |
    | Row 1 Column 1 | Row 1 Column 2 | Row 1 Column 3 |
    | Row 2 Column 1 | Row 2 Column 2 | Row 2 Column 3 |
    | Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |
    ```
        
    | Column 1 Header | Column 2 Header | Column 3 Header |
    | --------------- | --------------- | --------------- |
    | Row 1 Column 1 | Row 1 Column 2 | Row 1 Column 3 |
    | Row 2 Column 1 | Row 2 Column 2 | Row 2 Column 3 |
    | Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |





### Icons & emojis

!!! pan-right ""

    ```
    | Method      | Description                          |
    | ----------- | ------------------------------------ |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ```
        
    | Method      | Description                          |
    | ----------- | ------------------------------------ |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |







### Alignment

!!! pan-right ""

    ```
    | Method      | Description                          |
    | :---------- | :----------------------------------- |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ```

    | Method      | Description                          |
    | :---------- | :----------------------------------- |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |





### [Excel file](https://timvink.github.io/mkdocs-table-reader-plugin/){target="_none"}

<iframe
src="docs/iframe_text.txt"
style="width:100%; height:60px;" frameborder="0" allowfullscreen
></iframe>

{{ read_excel('docs/tables/mathjax_maths.xlsx', sheet_name='mathjax', engine='openpyxl') }}



## [Jupyter Notebooks](https://github.com/danielfrg/mkdocs-jupyter){target="_none"}

Copy .ipynb or .py file into the directory to be rendered as a .html page.


## Markdown Exec

Execute code blocks in Markdown file.


### System information

!!! pan-right ""

    ```py
     ```python exec="true" html="true"
     import platform
 
     print(
         f"""
         <ul>
         <li>machine: <code>{platform.machine()}</code></li>
         <li>version: <code>{platform.version()}</code></li>
         <li>platform: <code>{platform.platform()}</code></li>
         <li>system: <code>{platform.system()}</code></li>
         </ul>
         """
     )
     ```
    ```

    ```python exec="true" html="true"
    import platform

    print(
        f"""
        <ul>
        <li>machine: <code>{platform.machine()}</code></li>
        <li>version: <code>{platform.version()}</code></li>
        <li>platform: <code>{platform.platform()}</code></li>
        <li>system: <code>{platform.system()}</code></li>
        </ul>
        """
    )
    ```


### visualize directory tree

!!! pan-right ""

    ```yml
     ```tree
     root1
         file1
         dir1
             file
         dir2
             file1
             file2
         file2
         file3
     root2
         file1
     ```
    ```

    ```tree
    root1
        file1
        dir1
            file
        dir2
            file1
            file2
        file2
        file3
    root2
        file1
    ```




# Markmap or mindmap

`This can be put as an independent site and linked, as`

:   Tested, there is an issue with superfences when integrating. Independently works fine after some tweaks.

:   Tested building a standalone page for iframe however does not export the graph to stanalone file.

