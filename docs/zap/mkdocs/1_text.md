---
title: Text
hide:
    # - navigation
    # - toc
    - footer
---

## General text

!!! check ""

    !!! pan-right ""

		    `Plain text.`

    !!! pan-right ""

		    Normal text.

	!!! pan-right ""
	
			# Heading1

	!!! pan-right ""
	
			## Heading2

	!!! pan-right ""
		
			### Heading3



## [Formatting](https://squidfunk.github.io/mkdocs-material/reference/formatting/#highlighting-changes){target="_none"}

### Basics

!!! check ""

    !!! check ""
        ```
        **This is bold text**
        ```

        **This is bold text**

    !!! check ""
        ```
        *This is italic text*
        ```
        
        *This is italic text*


    !!! check ""
        ```
        ***This is bold italic text***
        ```

        ***This is bold italic text***


    !!! check ""
        ```
        ~~this is strikethrough~~
        ```

        ~~this is strikethrough~~


    !!! check ""
        ```
        ~~***This is strikethrough bold italic text***~~
        ```

        ~~***This is strikethrough bold italic text***~~


### Subscript Superscript

!!! check ""

    ```
    - H~2~O
    - A^T^A
    ```

    - H~2~O
    - A^T^A


### Underline strikethrough

!!! check ""

    ```
    - ^^This was inserted^^
    - ~~This was deleted~~
    ```

    - ^^This was inserted^^
    - ~~This was deleted~~


### Highlighting

<iframe
    src="docs/highlighting.txt"
    style="width:100%; height:180px;" frameborder="0" allowfullscreen
></iframe>

Text can be {--deleted--} and replacement text {++added++}. This can also be
combined into {~~one~>a single~~} operation. {==Highlighting==} is also
possible {>>and comments can be added inline<<}.

{==
Formatting can also be applied to blocks by putting the opening and closing
tags on separate lines and adding new lines between the tags and the content.
==}

- ==This was marked==





## Blocks

!!! check ""

    !!! check ""
	    
                `Plain text starting with a tab puts it into a highlighted block.`

    !!! check ""
	    
                Normal text starting with a tab puts it into a highlighted block.



## [Code Block](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#highlighting-inline-code-blocks){target="_blank"}

### Block syntax

!!! check ""

    ```
     ```py
     import tensorflow as tf
     ```
    ```

    ``` py
    import tensorflow as tf
    ```


### In line

!!! check ""

    ```
    The `#!python range()` function is used to generate a sequence of numbers.
    ```

    The `#!python range()` function is used to generate a sequence of numbers.



### Single line

!!! check ""

    ```
    >D3 was created using JavaScript.
    
    >D3 (in general) uses SVG to create the graphical elements.
    ```

    >D3 was created using JavaScript.
    
    >D3 (in general) uses SVG to create the graphical elements.



### Title

!!! check ""
    ```
     ``` py title="bubble_sort.py"
     def bubble_sort(items):
         for i in range(len(items)):
             for j in range(len(items) - 1 - i):
                 if items[j] > items[j + 1]:
                     items[j], items[j + 1] = items[j + 1], items[j]
     ```
    ```

    ``` py title="bubble_sort.py"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```



### Line numbers

!!! check ""
    ```
     ``` py linenums="1"
     def bubble_sort(items):
         for i in range(len(items)):
             for j in range(len(items) - 1 - i):
                 if items[j] > items[j + 1]:
                     items[j], items[j + 1] = items[j + 1], items[j]
     ```
    ```

    ``` py linenums="1"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```




### Highlight lines

!!! check ""
    ```
     ``` py hl_lines="2 3"
     def bubble_sort(items):
         for i in range(len(items)):
             for j in range(len(items) - 1 - i):
                 if items[j] > items[j + 1]:
                     items[j], items[j + 1] = items[j + 1], items[j]
     ```
    ```

    ``` py hl_lines="2 3"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```




### Anotations

!!! check ""
    ```
     ``` yaml
     theme:
         features:
         - content.code.annotate # (1)
     ```
     
     1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
         text__, images, ... basically anything that can be written in Markdown.
     ```

    ``` yaml
    theme:
      features:
        - content.code.annotate # (1)
    ```
    
    1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
        text__, images, ... basically anything that can be written in Markdown.








### YAML

Yet Another Markup Language allows text with description in different color formatting.

!!! check ""

    ```
     ```yaml
     epub-cover-image : ${.}/cover.jpg
     epub-metadata    : ${.}/meta.xml
     
     resource-path:
     - .              # the working directory from which pandoc is run
     - ${.}/images    # the images subdirectory of the directory
                         # containing this defaults file
     ```
    ```

    ```yaml
    epub-cover-image : ${.}/cover.jpg
    epub-metadata    : ${.}/meta.xml
    
    resource-path:
    - .              # the working directory from which pandoc is run
    - ${.}/images    # the images subdirectory of the directory
                     # containing this defaults file
    ```




### Tabs

!!! check ""

    === "Python"
        ``` python linenums="1"
        amount = 0
        if amount < 0:
            print('Negative amount')
        elif amount > 0:
            print('Positive amount')
        else:
            print('Zero')
        ``` 
    === "Java"
        ``` java linenums="1"
        int amount = 0;
        if (amount < 0) {
            System.out.println("Negative amount");
        } else if (amount > 0) {
            System.out.println("Positive amount");
        } else {
            System.out.println("Zero");
        }
        ``` 
    === "Ruby"
        ``` ruby linenums="1"
        amount = 0
        if amount < 0
            puts "Negative amount"
        elsif amount > 0
            puts "Positive amount"
        else
            puts "Zero"
        ``` 
    === "Markdown"
        ```
        === "Python"
            ``` python linenums="1"
            amount = 0
            if amount < 0:
                print('Negative amount')
            elif amount > 0:
                print('Positive amount')
            else:
                print('Zero')
            ```
        === "Java"
            ``` java linenums="1"
            int amount = 0;
            if (amount < 0) {
                System.out.println("Negative amount");
            } else if (amount > 0) {
                System.out.println("Positive amount");
            } else {
                System.out.println("Zero");
            }
            ``` 
        === "Ruby"
            ``` ruby linenums="1"
            amount = 0
            if amount < 0
                puts "Negative amount"
            elsif amount > 0
                puts "Positive amount"
            else
                puts "Zero"
            ``` 
        ```




### [Attach external files](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#embedding-external-files){target="_blank"}

<iframe
src="docs/iframe_external_file_in_code_block.txt"
style="width:100%; height:60px;" frameborder="0" allowfullscreen
></iframe>

```.py linenums="1" title="embedding external files"
--8<-- "automation/analysis flow/01_dependencies/os_functions.py"
```





## Lists

### Simple list

!!! check ""

    ```
    - `topic 1`:  description for topic 1
    - `topic 2`:  description for topic 2
    	- `topic 2.1`: description for topic 2.1
    ```

    - `topic 1`:  description for topic 1
    - `topic 2`:  description for topic 2
    	- `topic 2.1`: description for topic 2.1



### Bullet list

!!! check ""

    ```
    * topic 1
    * topic 2
    ```

    * topic 1
    * topic 2


### Numbered list

!!! check ""

    ```
    1. topic 1
    2. topic 2
    ```

    1. topic 1
    2. topic 2




### Indented list

!!! check ""

    ```
    1. This is a multi-line list item.
    	This is also part of the list item.
    	And so is this
    2. Here is another one.
    
    	Where this is also part of the list item.
    
    	Doing that will give you this list:
    	
    	1. This is a multi-line list item. This is also part of the
    		list item. And so is this.
    	2. Here is another one. Where this is also part of the list
    		item.
    ```

    1. This is a multi-line list item.
    	This is also part of the list item.
    	And so is this
    2. Here is another one.
    
    	Where this is also part of the list item.
    
    	Doing that will give you this list:
    	
    	1. This is a multi-line list item. This is also part of the
    		list item. And so is this.
    	2. Here is another one. Where this is also part of the list
    		item.



### Indented continued list

!!! check ""

    ```
        1. This is a multi-line list item.
        	This is also part of the list item.
        	And so is this
        2. Here is another one.
        
        	Where this is also part of the list item.
        
        	Doing that will give you this list:
        	
        	1. This is a multi-line list item. This is also part of the
        		list item. And so is this.
        	2. Here is another one. Where this is also part of the list
        		item.
        
                ![Placeholder](img/relative_reference.png){ align=left style="height: 10%; width: 10%; border-radius: 5px;" loading=lazy}
    
    
        3. Some more points
        4. And more points
    ```

    1. This is a multi-line list item.
    	This is also part of the list item.
    	And so is this
    2. Here is another one.
    
    	Where this is also part of the list item.
    
    	Doing that will give you this list:
    	
    	1. This is a multi-line list item. This is also part of the
    		list item. And so is this.
    	2. Here is another one. Where this is also part of the list
    		item.
    
            ![Placeholder](img/relative_reference.png){ align=left style="height: 10%; width: 10%; border-radius: 5px;" loading=lazy}


    3. Some more points
    4. And more points




### Definition list

!!! check ""

    ```
    `Lorem ipsum dolor sit amet`
    
    :   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
        tellus non sem sollicitudin, quis rutrum leo facilisis.
    
    `Cras arcu libero`
    
    :   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
        ut eros sed sapien ullamcorper consequat. Nunc ligula ante.
    
        Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
        Nam vulputate tincidunt fringilla.
        Nullam dignissim ultrices urna non auctor.
    ```

    `Lorem ipsum dolor sit amet`
    
    :   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
        tellus non sem sollicitudin, quis rutrum leo facilisis.
    
    `Cras arcu libero`
    
    :   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
        ut eros sed sapien ullamcorper consequat. Nunc ligula ante.
    
        Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
        Nam vulputate tincidunt fringilla.
        Nullam dignissim ultrices urna non auctor.




### Task list

!!! check ""

    ```
    - [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
    - [ ] Vestibulum convallis sit amet nisi a tincidunt
        * [x] In hac habitasse platea dictumst
        * [x] In scelerisque nibh non dolor mollis congue sed et metus
        * [ ] Praesent sed risus massa
    - [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
    ```

    - [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
    - [ ] Vestibulum convallis sit amet nisi a tincidunt
        * [x] In hac habitasse platea dictumst
        * [x] In scelerisque nibh non dolor mollis congue sed et metus
        * [ ] Praesent sed risus massa
    - [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque




## Footnotes

!!! check ""

    ```
    Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
    
    [^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    [^2]: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.
    ```

    Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
    
    [^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    [^2]: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.






## Tooltip

!!! check ""

    ```
    [Hover me](https://example.com "I'm a tooltip!")
    ```

    [Hover me](https://example.com "I'm a tooltip!")





## Tooltip with reference

!!! check ""

    ```
    [Hover me][example]

      [example]: https://example.com "How are you doing"
    ```

    [Hover me][example]

      [example]: https://example.com "How are you doing"



## Tooltip on abbreviation

!!! check ""

    ```
    The HTML specification is maintained by the W3C.
    
    *[HTML]: Hyper Text Markup Language
    *[W3C]: World Wide Web Consortium
    ```

    The HTML specification is maintained by the W3C.
    
    *[HTML]: Hyper Text Markup Language
    *[W3C]: World Wide Web Consortium



## Tooltip on icon

!!! check ""

    ```
    :material-information-outline:{ title="Important information" }
    ```

    :material-information-outline:{ title="Important information" }




## Hyperlinks

### Autolinks

Not using due to conflicts.

!!! check ""

    ```
	[link to mkdocs settings file](8_settings.md)
	```

	[link to mkdocs settings file](8_settings.md)


### Link

!!! check ""

    ```
    <https://www.alnoda.org>   
    ```

    <https://www.alnoda.org>   


### Opens in a new tab

!!! check ""

    ```
    [Cluster Analysis](C:\Users\Ashutosh Gaur\My Drive\edupunk\data science\cluster analysis\____archive\cluster analysis.html){target="_blank"}
    ```

    [Cluster Analysis](C:\Users\Ashutosh Gaur\My Drive\edupunk\data science\cluster analysis\____archive\cluster analysis.html){target="_blank"}


### Markdown objects

!!! check ""

    ```
    [Graphics](2_insert.md)
    
    [Image with Placeholder](2_insert.md#image-with-placeholder)
    
    [`RMSE`](../../machine learning/construct/rmse.md)

    [`RMSE`](../../machine_learning/construct.md#rmse)
    
    If your Markdown file is at c:/abc/123/docs and you want to link to c:/def/456, then your relative link would be: `../../../def/456`
    ```

    [Graphics](2_insert.md)
    
    [Image with Placeholder](2_insert.md#image-with-placeholder)
    
    <!-- [`RMSE`](../../machine_learning/construct.md#rmse) -->


### Within a block

!!! check ""

    ```
    <pre><code style="font-size:80%;"><a href="https://www.iimidr.ac.in/executive-programmes/long-duration-online-programmes/integrated-program-in-business-analytics-ipba/" target="_blank">IPBS</a> : About the program
    </code></pre>
    ```

    <pre><code style="font-size:80%;"><a href="https://www.iimidr.ac.in/executive-programmes/long-duration-online-programmes/integrated-program-in-business-analytics-ipba/" target="_blank">IPBS</a> : About the program
    </code></pre>


### Image

!!! check ""

    ```
    Works for links within project page.
    
    [![](flow\img\flow - sankey diagram titanic passenger survival by port of embarkment.png){align=left style="height: 20%; width: 20%; border-radius: 5px;" loading=lazy}](flow\index.md)
    ```


### Button

!!! check ""

    ```
    [Visit our Github page :fontawesome-brands-github-alt:](hhttps://github.com/bluxmit/alnoda-workspaces){ .md-button .md-button--primary }
    ```
    
    [Visit our Github page :fontawesome-brands-github-alt:](hhttps://github.com/bluxmit/alnoda-workspaces){ .md-button .md-button--primary }


### Within excel sheets

```
<a href="https://github.com/msasnur/Healthcare-Analytics/blob/main/Healthcare%20Analytics%20-%20Project%20Report.pdf"_blank">Project structure</a>
```

### Mailto

!!! check ""

    ```
    [`Contact us`](mailto: abc@abc.com)
    ```

    [`Contact us`](mailto: abc@abc.com)

