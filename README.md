<p align="center">
    <a href="https://github.com/Intsights/flake8-intsights">
        <img src="https://raw.githubusercontent.com/Intsights/flake8-intsights/master/images/logo.png" alt="Logo">
    </a>
    <h3 align="center">
        Uncompromising and opinionated flake8 plugin which follows Intsights' practices
    </h3>
</p>

![license](https://img.shields.io/badge/MIT-License-blue)
![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%20pypy3-blue)
![Build](https://github.com/Intsights/flake8-intsights/workflows/Build/badge.svg)
[![PyPi](https://img.shields.io/pypi/v/flake8-intsights.svg)](https://pypi.org/project/flake8-intsights/)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
  - [Warnings](#warnings)
    - [Full List](#full-list)
    - [Backslashes](#backslashes)
    - [Blank Lines](#blank-lines)
    - [Builtins](#builtins)
    - [Comments](#comments)
    - [Debugging](#debugging)
    - [Declarations](#declarations)
      - [Lists/Sets/Tuples/Dicts](#listssetstuplesdicts)
      - [Functions/Classes Definitions](#functionsclasses-definitions)
      - [Try/Except/Exceptions](#tryexceptexceptions)
    - [Duplications](#duplications)
    - [Imports](#imports)
    - [Indents](#indents)
    - [Mutables](#mutables)
    - [Naming](#naming)
    - [Raise](#raise)
    - [Quotes](#quotes)
    - [Spacing](#spacing)
    - [String Formatting](#string-formatting)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)


## About The Project

flake8-intsights is a flake8 extension to lint for conventions that are being used in Intsights. This extensions is not configurable and highly opinionated. Each of the warnings was developed after a lot of thinking. We took into consideration many aspects such as bug reduction, clearability, code complexity, code editing and more.


### Built With

* [astroid](https://github.com/PyCQA/astroid)
* [flake8](https://github.com/PyCQA/flake8)


### Warnings

#### Full List

| Code     | Text                                                                                                                 |
| -------- | -------------------------------------------------------------------------------------------------------------------- |
| **I001** | at each python module, there should be a blank line at the end of the file                                           |
| **I002** | there should not be any blank lines at the top of a python module                                                    |
| **I003** | no tabs indentation, only spaces                                                                                     |
| **I004** | only 4 spaces indentation                                                                                            |
| **I005** | inline comments are not allowed                                                                                      |
| **I006** | indentation should be gradually added                                                                                |
| **I011** | only single quote is allowed in strings                                                                              |
| **I012** | duplicate definition                                                                                                 |
| **I021** | only one import module per line                                                                                      |
| **I022** | never import * from module                                                                                           |
| **I023** | never from import a module name, just relative from imports                                                          |
| **I024** | never relative import from a module, import the whole module instead                                                 |
| **I025** | never provide a module alias                                                                                         |
| **I026** | relative imports must be decleared after non-relative ones                                                           |
| **I027** | standard imports and relative imports should be seperated by one newline                                             |
| **I028** | last import must be spaced with two lines                                                                            |
| **I031** | control keywords right after special control definitions must not be spaced                                          |
| **I032** | control keywords must be divided by space all the time                                                               |
| **I033** | control keywords right after special neighbour control definitions must not be spaced                                |
| **I034** | except/finally/else, must not be spaced                                                                              |
| **I041** | an empty list/dict must be declared with []/()/{}                                                                    |
| **I042** | each list entry must be in its own line                                                                              |
| **I043** | each list entry must end with comma                                                                                  |
| **I044** | a tuple must be enclosed within () and be spaced with 1 new line                                                     |
| **I045** | each subentry opener must be in its own line                                                                         |
| **I046** | dict key and value must be on the same line                                                                          |
| **I047** | dict keys must not be on the same line                                                                               |
| **I048** | dict keys must be identically indented                                                                               |
| **I049** | dict key type must be on of the following: a const, a name, of a dict unpack                                         |
| **I051** | class definition without inheritance should be declared only by "class Name:"                                        |
| **I052** | main class definition should start with a  "class Name("                                                             |
| **I053** | each base class should be seperated by a new-line                                                                    |
| **I054** | each base class should be one indentation level above the main class                                                 |
| **I055** | each base class definition should be ended with a comma                                                              |
| **I056** | classes should never inherit from object                                                                             |
| **I061** | function definition with no arguments should be defined as: "def function_name():"                                   |
| **I062** | function definition with arguments should define the arguments starting by the next line"                            |
| **I063** | each function argument should be in a new line                                                                       |
| **I064** | each function argument should be in the same indentation level, 1 level above the function definition line           |
| **I065** | each function argument should be ended with a comma                                                                  |
| **I066** | there must not be any empty lines in the function definition                                                          |
| **I071** | exception handler parameter name should be "exception"                                                               |
| **I081** | function default parameter must not be mutable                                                                       |
| **I091** | never use a builtin name                                                                                             |
| **I092** | never leave a debug code                                                                                             |
| **I093** | do not break a line with backslashes                                                                                 |
| **I094** | functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly |
| **I095** | class name should start with upper case char and must not include underscore                                         |
| **I096** | unittest TestCase class name should start with the tested module name and end with TestCase                          |
| **I097** | function arguments should be lower case                                                                              |
| **I098** | use only fstring for string interpolation. format and % are forbidden                                                |
| **I099** | raising an exception should raise an object not a type                                                               |

#### Backslashes

Line ending with backslashes to escape \r are forbidden. We assume that escaping new lines characters is a result of bad code design and flow. We believe there is always a better way to organize your code to avoid this behavior. Most times, the use of this escaping technique is a result of avoiding long lines or organizing text in a viewable visual form. We encourage getting familiar with [textwrap](https://docs.python.org/3/library/textwrap.html) library.

```python
# bad - to avoid a long line
long_text = 'blabllablasdlasdflkasdf\
sdflkjasdflkjasdf'
# good - option 1
long_text = (
    'blabllablasdlasdflkasdf'
    'sdflkjasdflkjasdf'
)
# good - option 2
long_text = 'blabllablasdlasdflkasdf'
long_text += 'sdflkjasdflkjasdf'

# bad - viewable visual form
long_text = 'ssh user@host \
    -flag-one option \
    -flag-two option \
    -flag-three option \
    -flag-four option \
'
# good - option 1
long_text = (
    'ssh user@host'
    ' -flag-one option'
    ' -flag-two option'
    ' -flag-three option'
    ' -flag-four option'
)
# good - option 2
long_text = 'ssh user@host'
long_text += ' -flag-one option'
long_text += ' -flag-two option'
long_text += ' -flag-three option'
long_text += ' -flag-four option'
# good - option 3
flags = [
    '-flag-one option',
    '-flag-two option',
    '-flag-three option',
    '-flag-four option',
]
long_text = f'ssh user@host {" ".join(flags)}'
```

#### Blank Lines

Inside a code block (function def, if/for/while, etc...), there should not be any double blank lines. We see no reason for more than one blank line.

```python
# bad
def function():
    a = 10


    return a
# good
def function():
    a = 10

    return a
```

#### Builtins

Assigning variables, parameters, and other names to buildins is forbidden. This can end up with unexpected behaviour. Many times developers do not think about the consequences of this. As a general rule, developers must not touch any of these builtins.

```python
# bad - this modules can not recover the original functionality of int builtin function
def int(var):
    ...
# good
def custom_to_int():
    ...

# bad - this modules can not recover the original functionality of int builtin function
def some_function(type):
    # can't use the builtin type function
    # for instance:
    # if type() is ...
    # won't work
    ...
# good
def some_function(var_type):
    ...
```

#### Comments

We do not believe in comments. Function names, along with variable names, and good separation between actions, must end up with a readable and understandable code. If you found yourself commenting, your code was probably written with bad practices. Complex functions that should be explained, can be explained with good separation of functions, which eventually end up with a self explanatory code. It also helps the developer separate the code in a logical and reasonable way.

```python
# bad - bad usage of variable names

# five minutes
x = 60 * 5

# good
five_minutes_in_seconds = 60 * 5

# bad - describe a process

# validates if the input is longer than the maximum
if len(text) > 1000:
    return False

# good
max_accepted_text_length = 1000
input_is_too_long = len(text) > max_accepted_text_length
if input_is_too_long:
    return False
```

#### Debugging

Make sure no debugging leftovers are present. Keywords like `breakpoint`, `ipdb`, `pudb` and more are forbidden. This warning makes sure no debugging code is being executed on production environments.

#### Declarations

This section provides one of the most complex conventions at Intsights. This set of warnings is designed to assure declerations and assignments are properly nested, ended and formed. With this set of warnings we increase the readability, editing and manipulating actions at the cost of longer code.

##### Lists/Sets/Tuples/Dicts

Rules:
* Every container must start with its opening char on the same line as the assignment parameter
* The first element of the container must be on the next line, indented
* Each element in the container must have its own line
* At the end of each element, there must be a comma
* Same rules apply for nested containers
* Dict keys types must be of the following types: consts, names or dict unpack

Exceptions:
* A single element sequential container can be enclosed without a new line

Rational:
* When every element has its own line, actions such as: reordering, line deletion, line duplication, become convenient
* When each element has its own line, the potential of exploding out of the line is impossible
* A list of elements is easier to understand when you don't have to split the elements based on the presence of a comma
* Using a multiline selection is easier when all the elements start at the same visual line
* When an element is ommited or added, text diff algorithms highlight the difference much better. Git diff would show the added/ommited element better
* Finding duplicates is possible based on line comparison
* Alphabetical ordering becomes possible
* Dicts keys types that are not consts, names of dict unpacks, are harder to read and maintain. It is important to assign the expressions outside of the dict declaration, and use the parameter name inside as a key

|                  Intsights' Conventions                   |                          Single Line                          |
| :-------------------------------------------------------: | :-----------------------------------------------------------: |
| <img src="images/examples/declarations - lines diff.png"> | <img src="images/examples/declarations - same line diff.png"> |


<!-- # TODO: put a demonstration video -->

```python
# bad - elements ordering, commas
list_a = [1, 2, 3]
list_b = [1, 2, 3,
    4, 5, 6]
tuple_a = (1, 2)
tuple_a = (1, 2)
set_a = {1, 2}
dict_a = {'key': 'value'}
list_of_lists_a = [[1, 2], [3, 4]]

# good - elements ordering - one element every line - indented, comma at the end of each element, closing bracket dedented.
list_a = [
    1,
    2,
    3,
]
tuple_a = (
    1,
    2,
)
dict_a = {
    'key': 'value',
}
dict_b = {
    'key': 'value',
    'dict_key': {
        'subdict_key': 'value',
    },
}
list_of_lists_a = [
    [
        1,
        2,
    ],
    [
        3,
        4,
    ],
]
single_element_list = [1]
```

##### Functions/Classes Definitions

Rules:
* Functions must be declared with the same rules as the rules applied to containers and declarations
* Each function's parameter must be declared in its own line, indented
* Each function's parameter must end with a comma unless it is a `**kwargs`
* Each class' inherited classes must be declared in its own line, indented

```python
# bad
class TestClass(DerivedTestClass):
    pass

class TestClass(DerivedTestClassOne, DerivedTestClassTwo):
    pass

# good

class TestClass(
    DerivedTestClass,
):
    pass

class TestClass(
    DerivedTestClassOne,
    DerivedTestClassTwo,
):
    pass
```

```python
# bad
def test_function(param_one):
    pass

def test_function(param_one, param_two):
    pass

def test_function(param_one, param_two,
    param_three):
    pass

def test_function(param_one, param_two,
    param_three='default'):
    pass

# good
def test_function(
    param_one,
):
    pass

def test_function(
    param_one,
    param_two,
):
    pass

def test_function(
    param_one,
    param_two,
    param_three,
):
    pass

def test_function(
    param_one,
    param_two,
    param_three='default',
):
    pass
```

##### Try/Except/Exceptions

Rules:
* Try/Except block must not be on one line
* After each block, there must not be a blank line
* Exception types must be enclosed in parentheses as a tuple if there is more than one, according to the tuple conventions
* Exception object name must be `exception`
* `try` keyword must be spaced above. There should be a blank line above it if it is not the first keyword after a new block (first keyword in a function)
* There must not be a blank line above `except` keyword
* `except` keyword must always contain an Exception type, but not exception object

```python
# bad
try:
    pass
except:
    pass

# good
try:
    pass
except Exception:
    pass

# bad
try: pass
except Exception: pass

# good
try:
    pass
except Exception:
    pass

# bad
def function():

    try:
        pass
    except Exception:
        pass

# good
def function():
    try:
        pass
    except Exception:
        pass

# bad
def function():
    try:
        pass
    except Exception, ExceptionOther:
        pass

# good
def function():
    try:
        pass
    except (
        Exception,
        ExceptionOther,
    ):
        pass

# bad
def function():
    try:
        pass
    except (
        Exception,
        ExceptionOther,
    ) as e:
        pass

# good
def function():
    try:
        pass
    except (
        Exception,
        ExceptionOther,
    ) as exception:
        pass
```

#### Duplications

Rules:
* Never call a function with the same name as another function in the same scope - class methods, global scope
* Never call a dictionary key with the same name as another dictionary key in the same dictionary
* Never call a class with the same name as another class in the same module

#### Imports

Rules:
* Imports must be ordered in the following order:
  * Standard libraries & 3rd parties
  * Internal libraries
  * Relative internal package modules/packages
* Never import with aliases
* Never use `from .module import other_module`, always import the parent module itself `from . import module`
* Within a package, use only relative imports
* For every imports group, sort alphabetically unless ordering might has impact on the runtime behavior (on rare occasions, result of bad practices)
* At the end of the imports section, there must be two blank lines of separation

Rationale:
* When a developer observe module's imports, he/she must understand where those packages/modules come from. Whether they are part of the package itself, whether they are part of the project, or they are 3rd party libraries
* Using aliases, especially in big projects with multiple developers, might mask important keywords, and potentially end with an unexpected behaviour for the sake of "less text". Masking the origin of a keyword can cause a lot of problems in big projects. Same goes for relative imports from a specific module such as `from .module import sub_module`
* Relative imports inside a package helps navigating inside a package. IDEs support is much better at finding the modules. You should never care about your current working directory anymore
* Sorting helps finding imports visually, with your eyes easier. Think about the following use case, which happens a lot. You have multiple sub modules inside a package, and you want to make sure you imported each one of them. Let's say there are 20 sub modules. IDEs directory tree is ordering files alphabetically. Many times, you will look at your module's imports sections, and start comparing both lists. If one is missing, you will find it much faster when both lists would be sorted rather than only the directory tree
* Nontheless, detecting duplications and typos is much easier when imports are sorted

```python
# bad
import module_one as one

# good
import module_one

# bad
from .package import module_one

# good
from . import package

# bad
import module_one
def function():
    pass

# good
import module_one


def function():
    pass

# bad
from . import sub_module
import module_one
import std_library

# good
import std_library

import module_one

from . import sub_module
```

#### Indents

Rules:
* Indents must always be 4 spaces
* Indents must be gradually indented, 4 spaces for every indent level
* Containers types' entries must also be identically indented

Rationale:
* Mixing indet types is not allowed to avoid syntax errors
* Using these guidlines not only would make the code visually readable, but would help text editors to assure auto indentation functionality would work
* Containers entries must be identically indented to allow for code editing techniques such as multiline editing, reordering and more

```python
# bad
list_a = [
    1,
        2,
        3,
]

# good
list_a = [
    1,
    2,
    3,
]

# bad
if something:
        pass

# good
if something:
    pass
```

#### Mutables

Rules:
* Never set a function argument default to a mutable value

Rationale:
* Most time, the behaviour is counterintuitive. Most developers at first would think, that each time the function gets invoked, it would generate a new mutable value. This is wrong, and could end up causing problems

```python
# bad
def function(
    param={},
):
    pass

# good
def function(
    param=None,
):
    if param is None:
        param = {}
```

#### Naming

Rules:
* function/method names must always be lower-snake case
* function parameters must always be lower-snake case
* Class names must always be uppercase and must not contain underscores
* Class methods must start with a parameter called `self` and classmethod with parameter called `cls`
* Unittest.TestCase class name must end with TestCase

Rationale:
* Consistency! Consistency! Consistency!
* Using `self` and `cls` for methods and classmethods respectively increase readability and eliminate potential synatax and runtime erros. It also helps code navigation (lookups)

```python
# bad
class someclass:
    pass
class someClass:
    pass
class some_class:
    pass

# good
class SomeClass:
    pass

# bad
def function(
    Param,
):
    pass

# good
def function(
    param,
):
    pass

# bad
class SomeClass:
    def method_one(
        slf,
    ):
        pass

    @classmethod
    def classmethod_one(
        kls,
    ):
        pass

# good
class SomeClass:
    def method_one(
        self,
    ):
        pass

    @classmethod
    def classmethod_one(
        cls,
    ):
        pass

# bad
class SomeTest(
    unittest.TestCase,
):
    pass

# good
class SomeTestCase(
    unittest.TestCase,
):
    pass
```

#### Raise

Rules:
* `raise` must be followed by and object rather than a class when raising an `Exception` derived object
* `raise` can raise a variable/attribute that holds an exception object

Rationale:
* `There should be one-- and preferably only one --obvious way to do it.`

```python
# bad
def function():
    raise Exception

# good
def function():
    raise Exception()
```

#### Quotes

Rules:
* You must always use single quotes rather than double quotes for strings

Rationale:
* `There should be one-- and preferably only one --obvious way to do it.`

```python
# bad
str_object = "some text"

# good
str_object = 'some text'
```

#### Spacing

Spacing is considered one of the most important parts of our conventions. A good/bad spacing has a huge impact on code quality and readability. A good use of spacing can lead to better readability and can also raise logic questions that might enforce the developer to supply answers. Think about the requirement of separating coding blocks into different spaced paragraphs. Each paragraph should be somehow a part of the bigger block. A developer should understand that each paragraph is a part of the bigger block. Consider the following example (it was taken from the spacing.py checker):

```python
@classmethod
def check_right_after_else(
    cls,
    node,
    lines,
):
    if not isinstance(node, astroid.If):
        return

    if not node.orelse:
        return

    if lines[node.orelse[0].lineno - 1].strip().startswith('elif '):
        else_nodes = node.orelse[0].orelse
    else:
        else_nodes = node.orelse

    child_nodes = []
    for child_node in else_nodes:
        if not hasattr(child_node, 'lineno'):
            continue

        if isinstance(child_node, astroid.Expr):
            child_nodes.append(child_node.value)
        else:
            child_nodes.append(child_node)

    if child_nodes:
        number_of_blank_lines_above = cls.number_of_blank_lines_above(
            lines=lines,
            node=child_nodes[0],
        )
        if number_of_blank_lines_above != 0:
            yield from cls.error_yielder.yield_error(
                error_id='I031',
                line_number=child_nodes[0].lineno,
                column_offset=child_nodes[0].col_offset,
            )
```

It is very clear that there are sections in this code. Let's walkthrough them.

The first section is the input limitations section. The function filters any input that it does not take care of.
```python
if not isinstance(node, astroid.If):
    return

if not node.orelse:
    return

The second section is responsible to extract the else_nodes from the input node.
```python
if lines[node.orelse[0].lineno - 1].strip().startswith('elif '):
    else_nodes = node.orelse[0].orelse
else:
    else_nodes = node.orelse
```

The third section is responsible to extract the child_nodes out of the else_nodes that were extracted previously.
```python
child_nodes = []
for child_node in else_nodes:
    if not hasattr(child_node, 'lineno'):
        continue

    if isinstance(child_node, astroid.Expr):
        child_nodes.append(child_node.value)
    else:
        child_nodes.append(child_node)
```

The last section is responsible for the function's main output. If to this line of code, child_nodes exist, there is a check the might end up with a yielded value.
```python
if child_nodes:
    number_of_blank_lines_above = cls.number_of_blank_lines_above(
        lines=lines,
        node=child_nodes[0],
    )
    if number_of_blank_lines_above != 0:
        yield from cls.error_yielder.yield_error(
            error_id='I031',
            line_number=child_nodes[0].lineno,
            column_offset=child_nodes[0].col_offset,
        )
```

I remember nothing from writing this function yet I can fill the gap very fast thanks to good work of spacing and naming conventions.

Rules:
* A `return`/`yield` keyword would always contain a blank line above, unless it is the first line of a block - right after a function definition / after if/else statement
* After each block opener, there must be no blank line - function definitions, if/else, try/except etc.

Rationale:
* A `return`/`yield` keyword would always show some end of logic, as such, they should be put under a spotlight and get their own line
* If a block was opened, there is no reason to separate it from the next line, it has no sense

```python
# bad
str_object = "some text"

# good
str_object = 'some text'
```

#### String Formatting

Rules:
* String formatting would happen only with fstring(string interpolation). Using `format` method, of `%` is forbidden

Rationale:
* Readability: fstrings are much lighter (number of lines), very readable
* Performance: fstrings are much faster

## Installation

```sh
pip3 install flake8-intsights
```


## Usage

This extension is built as a flake8 plugin. As such, it is enabled by default after installation.


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Gal Ben David - gal@intsights.com

Project Link: [https://github.com/Intsights/flake8-intsights](https://github.com/Intsights/flake8-intsights)
