# static_site_generator

A static site is what it sounds like... static. No matter who is interacting with the site, the content is always the same. You cannot log in, you can't leave comments, or upload files to a static site. You would need a dynamic site for that stuff, which is usually powered by a database and a custom web server.

Some popular production-ready static site generators include:

- Eleventy
- Gatsby
- Astro
- Jekyll
- Hugo

## MARKDOWN

Here's the deal: writing HTML by hand sucks. Even if you're a grubby front-end programmer, you probably don't want to write entire documents in raw HTML. It's just too much work.

Here's the other deal: writing Markdown is pure bliss. Markdown is a less-verbose markup language designed for ease of writing. The trouble is, web browsers don't understand Markdown. They only understand HTML and CSS. So, the #1 job of a static site generator is to convert Markdown into HTML.

Our static site generator will take a directory of Markdown files (one for each web page), and a simple HTML and CSS template, and output a browser-ready bundle of HTML and CSS files.

## CHEAT SHEET

Seeing as the primary objective of a static site generator is to convert Markdown into HTML, it's important to understand the basics of each. We're not going to cover every aspect of Markdown or HTML, but we will cover the basics.

HEADINGS
Typically there are 6 possible levels of headings in HTML. "Heading 1" is the heading for an entire document, then you can nest multiple "Heading 2"'s in the document, multiple "Heading 3"'s in each "Heading 2", and so on.

<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>

# Heading 1

## Heading 2

### Heading 3

PARAGRAPHS

<p>This is a paragraph of text.</p>

This is a paragraph of text.

BOLD

<p>This is a <b>bold</b> word.</p>

This is a **bold** word.

ITALICS

<p>This is an <i>italic</i> word.</p>

This is an _italic_ word.

LINKS
This is a paragraph with a <a href="https://www.google.com">link</a>.

This is a paragraph with a [link](https://www.google.com).

RENDERING IMAGES
<img src="url/of/image.jpg" alt="Description of image">

![alt text for image](url/of/image.jpg)

UNORDERED LISTS

<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

- Item 1
- Item 2
- Item 3

ORDERED LISTS

<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>

1. Item 1
2. Item 2
3. Item 3

QUOTES

<blockquote>
    This is a quote.
</blockquote>

> This is a quote.

CODE
<code>This is code</code>

`This is code`
