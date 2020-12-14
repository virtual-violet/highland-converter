## What is this?
This is a tool for converting `.highland` files to Markdown or HTML. I made it because while I love the [Highland 2](https://quoteunquoteapps.com/highland-2/) editor, it doesn't have a proper HTML export, and the Markdown export it has breaks images. Right now, it only supports Highland files that are a single document, it does not support Highland's `{{INCLUDE}}` function. It does, however, support Highland's `> centered text <` markup.

## How do I use it?
Download the Python script and run it, using `-i [filename]` to point it at the file to convert. Use the `--html` flag to generate an HTML file as well. This script also requires [markdown2](https://pypi.org/project/markdown2/), which can be installed with `pip`. 

Examples:

`python3 highland-converter.py -i my_file.highland` will generate a folder containing a Markdown file and the associated assets of your Highland project.

`python3 highland-converter.py -i my_file.highland --html` will do the same as the first command, but also include a `.html` file in the folder.

## I don't know how to use Python scripts/the command line!
Sorry! Maybe I'll get around to creating a graphical version of this tool, but don't hold your breath. This is just a small tool that I made with some free time, so I don't know if I'll get a chance to do that.

## I want to convert to [FORMAT]!
The beauty of plain Markdown and HTML is that they can be converted to basically anything, so there's already a tool out there for doing this. I recommend looking into [Pandoc](https://pandoc.org/) if you need to convert this Markdown or HTML into a format Highland 2 doesn't support. I *do* intend on adding EPUB support to this converter, though, to make it usable for self-publishing novelists.

## Do you work for Quote-Unquote Apps/John August?
No! I'm just an independent writer and coder who really enjoys Highland 2 but needed some features it doesn't have, and I figured other people may be in a similar situation. I am in no way, shape, or form affiliated with Quote-Unquote Apps or John August, and **this project is not endorsed or supported by them.** 