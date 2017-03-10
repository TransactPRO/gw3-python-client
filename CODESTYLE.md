# Code Style Guide

The code should generally follow [PEP8](https://www.python.org/dev/peps/pep-0008/)

Code documentation should be written using Google style, which can be extracted
using Sphinx:
* [Example Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)


## Line Length

PEP8 recommends a maximum line length of 80 characters.  While some lines
are easier to read if they're a bit longer than that, generally try to stay
within the 80 character limit.

Parameter lists can be wrapped and long strings can be split by enclosing them
in parentheses:

````python
long_string = ('First long line...'
    'Second long line')
````

## White Space

Indentation should be made using 4 space characters.

* Two blank lines between class definitions and top-level functions
* One blank line between methods (generally)

Follow [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)
for whitespace in expressions and statements.

## Imports

Import statements should be arranged in three blocks at the head of the file
(though after the module documentation).  Each block of imports should be in
alphabetical order.

1. The first block should be Python-provided packages (eg. sys)
2. The second block should be third-party packages (eg. numpy)
3. The final block should be local packages and module (eg. from . import response)

````python
import os
import sys

from . import operation
````

Wildcard imports (from module import *) should not be used outside of tests.

Additionally it is generally useful to avoid importing variables from modules
directly into the local namespace (from module import some_object) - Doing
so means you now have two references to to the same thing, which impedes
mocking during unit tests.

Better instead to import the module and reference a qualified name (import module
and module.some_object).

## Names

* Module level constants should be in CAPS
    ```
        OPTION_A = 0x01
        OPTION_B = 0x02
    ```
* Class names should be CamelCase
    ```
        class MyAwesomeClass:
    ```
* Variables, attributes, functions, methods and properties should be lowercase with underscores
    ```
        my_variable_of_response = MyAwesomeClass.get_response
    ```
* Variables, attributes, functions, methods and properties can be named with a
leading underscore to indicate that they're "private"
    ```
        __private_validate_response(response):
    ```

## Exceptions

Wherever practical, catch explicit exception classes rather than using
a bare try/except statement (or matching Exception).

To re-raise the original exception use raise by itself or
raise MyException() from exc
(rather than raise exc) to maintain the original stack trace.
