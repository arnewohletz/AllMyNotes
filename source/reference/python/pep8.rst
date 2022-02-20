PEP-8
=====
`PEP-8 <https://www.python.org/dev/peps/pep-0008/>`__ is the official style guide
for Python code.

This is a summary of the document.

* 4 space indent
* 79 character max. line length (72 for docstrings)
* 2 blank lines around classes and top level functions
* 1 blank line around methods inside classes
* UTF-8 encoding
* only use ASCII characters in strings or use escape (\\) characters for non-ASCII
* comments must be full sentences
* comments must be up-to-date with the code
* comments start with number sign (#) + single space
* always write comments in English
* prefer block comments (docstrings) over inline comments
* docstrings are required for all public modules, functions, classes and methods
* never use 'l' (lowercase L), 'O' (uppercase O) or 'I' (uppercase I) as single
  character variable name
* each import in separate line
* import order:

    #. standard library
    #. related third party
    #. local application/library

* avoid wildcard imports (e.g. \*)
* module level "dunders" (e.g. __name__) must be declared before import
  statements (but after module docstring)
* no unnecessary whitespace
* use whitespace around binary operators (e.g. +, -, <, >, ==, ...)
* don't use whitespace around higher prioritized operators (e.g. \*) when
  combined: :python:`x = x*2 - 1`
* module naming: lowercase names, preferably no underscores
* class naming: CamelCase style (each word starts with uppercase, no spaces)
* exception naming: same as class
* global variable naming: same as functions
* constant naming: all uppercase, words separated by underscores
* function / method & (instance) variable naming: lowercase, words separated
  by underscores. Leading underscore for non-public methods.
