---
title: Zap
hide:
    # - navigation
    # - toc
    # - footer
---

<h1 style="padding:0 margin-top:0px"></h1>

## Bookmarks

!!! bookmark-outline "&nbsp;"

	Development
	:	[`devdocs`](https://devdocs.io/){target="_blank"}

## Data structures

!!! pan-right ""

    A data structure is a particular way of organizing data in a computer so that it can be used effectively. E.g. Array, Hashing, Matrix, Graph.



## Strictness vs Laziness

!!! pan-right ""

    a = b = c = 5 d = a + b * c

    In a pure functional programming language like Haskell, the value of d might not be evaluated until it is actually used elsewhere. The idea of deferring computations in this way is commonly known as lazy evaluation. 

    Python, on the other hand, is a very strict (or eager) language. Nearly all of the time, computations and expressions are evaluated immediately. There are Python techniques, especially using iterators and generators, which can be used to achieve laziness.
