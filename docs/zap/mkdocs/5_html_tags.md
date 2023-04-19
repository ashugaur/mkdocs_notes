---
title: HTML tags
hide:
    # - navigation
    # - toc
    - footer
---

<!-- <h1 style="padding:0 margin-top:0px"></h1> -->

## Comment

!!! pan-right ""

    ```yaml title="Comment will remain hidden when .md is published"
    <!-- This is commented out. -->
    ```


## Hide heading from a page

!!! pan-right ""

    ```yaml
    <h1 style="padding:0 margin-top:0px"></h1>
    ```



## Add space

!!! keyboard-space ""

    ```yaml
    Type &nbsp; to add a single space.
    Type &ensp; to add 2 spaces.
    Type &emsp; to add 4 spaces.
    ```

    Type &nbsp; to add a single space.<br>
    Type &ensp; to add 2 spaces.<br>
    Type &emsp; to add 4 spaces.


## Underline

!!! pan-right ""

	```
	Some of these words <ins>will be underlined</ins>.
	```

	Some of these words <ins>will be underlined</ins>.


## Align centre

!!! pan-right ""

	```
	<center>This text is centered.</center>
	
	<p style="text-align:center">Center this text</p>
	```

	<center>This text is centered.</center>

	<p style="text-align:center">Center this text is.</p>


## Color

!!! pan-right ""

	```
	<font color="red">This text is red!</font>
	
	<p style="color:blue">Make this text blue.</p>
	```

	<font color="red">This text is red!</font>
	
	<p style="color:blue">Make this text blue.</p>



## Admonitions

!!! pan-right ""

	```
	> :warning: **Warning:** Do not push the big red button.

	> :memo: **Note:** Sunrises are beautiful.

	> :bulb: **Tip:** Remember to appreciate the little things in life.
	```

	> :warning: **Warning:** Do not push the big red button.

	> :memo: **Note:** Sunrises are beautiful.

	> :bulb: **Tip:** Remember to appreciate the little things in life.


## Hyperlink

!!! pan-right ""

    ```<a href="https://pythex.org/" target="_blank">regex.org</a>```

    <a href="https://pythex.org/" target="_blank">regex.org</a>


## Transparent page

```
<head>
    <meta charset="UTF-8">
    <title>Particles - D3blocks</title>

    <style>
      body { background: transparent; }
      circle.mouse { fill: none; }
    </style>

</head>
```


## Highlighting with HTML and CSS

!!! check ""

    ```
    <span style="font-family: serif; color: #f59842; font-size: 1.2rem;">Company is working on software for self-driving vehicles</span></br>
    <span style="font-family: serif; color: teal; font-size: 0.8rem;">I can't wait until my car suddenly stops in the middle of the highway and reboots to install updates.</span>
    ```

    <span style="font-family: serif; color: #f59842; font-size: 1.2rem;">Company is working on software for self-driving vehicles</span></br>
    <span style="font-family: serif; color: teal; font-size: 0.8rem;">I can't wait until my car suddenly stops in the middle of the highway and reboots to install updates.</span>


## Task list with html and css

<iframe
src="docs/task_list.txt"
style="width:100%; height:120px;" frameborder="0" allowfullscreen
></iframe>

<div style="display: flex; justify-content: center;" markdown="block">

- [X] One
- [X] Two
- [ ] Three

</div>
