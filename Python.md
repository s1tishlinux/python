# Python Guide

This python guide is intended to those who already know python and want a mind refresh or looking for a specific syntax.  
*-as this guide doesn't elaborate in explaining thing that a programmer would already know -like: variable, function, csv, json-*

additionally, this guide is not intended to be a replacement for reading [official Python documentation](https://docs.python.org).

> guide version: **2.1.0**  |  python version: 3.10

| Part of Version | Explanation                                 |
| --------------- | ------------------------------------------- |
| **X**.x.x       | Add new content/section                     |
| x.**X**.x       | Edit a (section content/document structure) |
| x.x.**X**       | Fix content                                 |

- [Python Guide](#python-guide)
  - [Frameworks](#frameworks)
    - [Web Development](#web-development)
    - [desktop Development](#desktop-development)
      - [GUI](#gui)
      - [CUI](#cui)
  - [General Info](#general-info)
    - [Related Jargon](#related-jargon)
    - [coding conventions](#coding-conventions)
    - [Implementations](#implementations)
    - [Run Python Files](#run-python-files)
    - [File Extension](#file-extension)
  - [Snippets](#snippets)
    - [stack](#stack)
    - [queue](#queue)
    - [array](#array)
    - [unpack string](#unpack-string)
    - [sorted function](#sorted-function)
      - [sort list](#sort-list)
      - [sort dictionary](#sort-dictionary)
    - [counter character frequency](#counter-character-frequency)
    - [pretty print](#pretty-print)
    - [get size of object](#get-size-of-object)
    - [calculate runtime](#calculate-runtime)
      - [using timestamp](#using-timestamp)
      - [using datetime](#using-datetime)
    - [read file](#read-file)
      - [using Path module](#using-path-module)
      - [using open function](#using-open-function)
    - [copy file snippet](#copy-file-snippet)
    - [generate random password](#generate-random-password)
    - [execute only if python file executed directly](#execute-only-if-python-file-executed-directly)
  - [Python Standard Library](#python-standard-library)
    - [len function](#len-function)
    - [zip function](#zip-function)
    - [range function](#range-function)
    - [Random Number generator](#random-number-generator)
    - [open file](#open-file)
    - [open web browser](#open-web-browser)
    - [send email](#send-email)
    - [Command-line Arguments](#command-line-arguments)
    - [run a command in Command-line](#run-a-command-in-command-line)
    - [shutil](#shutil)
    - [Path](#path)
      - [Working With Directory](#working-with-directory)
        - [list directory content](#list-directory-content)
          - ["iterdir" function](#iterdir-function)
          - ["globe" function](#globe-function)
          - ["rglobe" function](#rglobe-function)
      - [Working With Files](#working-with-files)
        - [File Management](#file-management)
        - [File Stat](#file-stat)
        - [Read and Write File](#read-and-write-file)
        - [Copy File](#copy-file)
    - [working with zip files](#working-with-zip-files)
    - [working with csv files](#working-with-csv-files)
    - [working with JSON files](#working-with-json-files)
    - [working with SQLite database](#working-with-sqlite-database)
    - [timestamp](#timestamp)
    - [datetime](#datetime)
      - [Working with Time Deltas](#working-with-time-deltas)
  - [Core Syntax](#core-syntax)
    - [the walrus operator(`:=`)](#the-walrus-operator)
    - [del statement](#del-statement)
    - [pass statement](#pass-statement)
    - [scope](#scope)
    - [Print Statement](#print-statement)
      - [simple form](#simple-form)
      - [print Multiple Strings](#print-multiple-strings)
    - [User Input](#user-input)
    - [Numbers](#numbers)
      - [Numbering Systems](#numbering-systems)
      - [Arithmetic Operations](#arithmetic-operations)
      - [Augmented Assignment Operator](#augmented-assignment-operator)
      - [Math module](#math-module)
    - [Type Annotation/hinting](#type-annotationhinting)
    - [Data types](#data-types)
      - [truth values](#truth-values)
    - [Variables](#variables)
      - [variable declaration](#variable-declaration)
      - [unpack variables](#unpack-variables)
      - [swap variables](#swap-variables)
      - [assign one value to multiple variables](#assign-one-value-to-multiple-variables)
      - [Python is a **dynamic** language](#python-is-a-dynamic-language)
    - [Type Casting](#type-casting)
    - [String](#string)
      - [some string methods](#some-string-methods)
        - [string sets](#string-sets)
      - [template](#template)
      - [combine strings](#combine-strings)
      - [Access Parts of The String](#access-parts-of-the-string)
      - [Escape Character](#escape-character)
    - [lambda expression](#lambda-expression)
    - [If Condition](#if-condition)
      - [General Structure](#general-structure)
      - [Comparison](#comparison)
      - [Boolean Operations(`and`, `or`, `not`)](#boolean-operationsand-or-not)
      - [`not`, `in`, `is`](#not-in-is)
      - [Chaining Comparison Operator](#chaining-comparison-operator)
      - [Ternary Operator](#ternary-operator)
    - [For Loop](#for-loop)
      - [for](#for)
      - [for...else](#forelse)
      - [enumerate](#enumerate)
    - [Generator Expressions](#generator-expressions)
    - [Comprehensive List](#comprehensive-list)
      - [comprehensive is not limited to lists](#comprehensive-is-not-limited-to-lists)
    - [While Loop](#while-loop)
    - [Functions](#functions)
      - [Bare Minimum](#bare-minimum)
      - [parameters](#parameters)
        - [Positional-only parameters](#positional-only-parameters)
        - [pass an arbitrary number of arguments](#pass-an-arbitrary-number-of-arguments)
        - [pass an arbitrary number of **keyword** arguments](#pass-an-arbitrary-number-of-keyword-arguments)
      - [Return Multiple Values](#return-multiple-values)
      - [function as a variable](#function-as-a-variable)
    - [Data Structure](#data-structure)
      - [list](#list)
        - [map list](#map-list)
        - [sort list of tuples](#sort-list-of-tuples)
        - [filter list](#filter-list)
        - [merge lists](#merge-lists)
      - [tuple](#tuple)
      - [set](#set)
      - [dictionary](#dictionary)
        - [merge dictionaries](#merge-dictionaries)
    - [unpack operator](#unpack-operator)
      - [unpack list](#unpack-list)
      - [unpack dictionary](#unpack-dictionary)
    - [Exceptions](#exceptions)
      - [handling exceptions](#handling-exceptions)
        - [Single exception](#single-exception)
        - [Multiple exceptions](#multiple-exceptions)
        - [Only one except clause get handled, the other get ignored](#only-one-except-clause-get-handled-the-other-get-ignored)
        - [raise an exception](#raise-an-exception)
      - [create a custom exception](#create-a-custom-exception)
    - [release resource](#release-resource)
      - [`finally` clause](#finally-clause)
      - [`with` statement](#with-statement)
        - [open multiple resources at once](#open-multiple-resources-at-once)
    - [`match` statement](#match-statement)
      - [match to a literal](#match-to-a-literal)
      - [`as` statement in `case`](#as-statement-in-case)
      - [Patterns with a literal and variable](#patterns-with-a-literal-and-variable)
      - [match a class](#match-a-class)
      - [Patterns with positional parameters](#patterns-with-positional-parameters)
      - [Nested patterns](#nested-patterns)
      - [Complex patterns and the wildcard](#complex-patterns-and-the-wildcard)
      - [guard](#guard)
      - [Named constants in pattern](#named-constants-in-pattern)
    - [`assert` keyword](#assert-keyword)
    - [class](#class)
      - [general structure](#general-structure-1)
      - [data class](#data-class)
      - [public and private members](#public-and-private-members)
      - [class and instance methods](#class-and-instance-methods)
      - [class and instance attributes](#class-and-instance-attributes)
      - [_isinstance_, _issubclass_ functions](#isinstance-issubclass-functions)
      - [propriety](#propriety)
      - [inheritance](#inheritance)
        - [abstract base class](#abstract-base-class)
          - [polymorphism](#polymorphism)
        - [multilevel inheritance](#multilevel-inheritance)
        - [multiple inheritance](#multiple-inheritance)
        - [Extending Built-in Types](#extending-built-in-types)
      - [method overriding](#method-overriding)
      - [decorator](#decorator)
      - [magic method](#magic-method)
  - [doc string](#doc-string)
  - [pydoc](#pydoc)
  - [module](#module)
    - [import module](#import-module)
      - [import syntax](#import-syntax)
      - [dire function](#dire-function)
      - [module as a script](#module-as-a-script)
      - [compiled module](#compiled-module)
  - [package management](#package-management)
    - [PIP](#pip)
    - [Environment](#environment)
    - [publish a package in PyPI](#publish-a-package-in-pypi)

## Frameworks

### Web Development

- [Flask](https://flask.palletsprojects.com/)
- [Django](https://www.djangoproject.com/)
- [fastapi](https://fastapi.tiangolo.com/)

### desktop Development

#### GUI

- [tkinter](https://docs.python.org/3/library/tkinter.html) (part of Python Standard Library)
- [others](https://wiki.python.org/moin/GuiProgramming)

#### CUI

- [Typer](https://typer.tiangolo.com/)

## General Info

### Related Jargon

- linter : check your source code for programmatic and stylistic errors.
- interrupter : execute your source code.

### coding conventions

[pep8](https://www.python.org/dev/peps/pep-0008/) is a formatting standard guide.

> Use 4 spaces per indentation level

> Function and class should be surrounded by 2 line breaks

```python
PI = 3.14  # constant  | variable can but shouldn't be modified
my_counter = 10  # variable


def my_function(very_long_name_parameter, very_long_name_argument):
    return very_long_name_parameter + very_long_name_argument


my_function(1, 2)

# function call with multiple lines
characters_frequency = {"a": 2, "b": 1, "c": 8}
print(sorted(
    characters_frequency.items(),
    key=lambda frequency_dict: frequency_dict[1],
    reverse=True))


class MyClass:
    pass
```

module name example: "my_module.py"

> related section: [module](#module)

### Implementations

[official documentation](https://docs.python.org/3/reference/introduction.html)

> python code get converted into platform-independent code(byte code).

Python generates a bytecode which can be Implemented using several programming languages, -some but not all- are in the following table:

| name                           | programming languages |
| ------------------------------ | --------------------- |
| cPython(common Implementation) | C                     |
| Jython                         | java                  |
| IronPython                     | C#                    |
| PyPy                           | subset of python      |

### Run Python Files

how to run python files from command line:

- `python file.py` for Windows
- `python3 file.py` for mac / linux (because python 2 exist in them)

### File Extension

| type                                     | file extension | contains                                       | opened using                                                               |
| ---------------------------------------- | -------------- | ---------------------------------------------- | -------------------------------------------------------------------------- |
| python file                              | *py*           | pure python code                               | [pycharm(IDE)][pycharm], [visual studio code(editor)][vscode]              |
| [jupyter notebook](https://jupyter.org/) | *ipynb*        | cells of python codes with output and markdown | [anaconda][anaconda], [colab][colab], [visual studio code(editor)][vscode] |

[pycharm]: https://www.jetbrains.com/pycharm/
[vscode]: https://code.visualstudio.com/
[anaconda]: https://www.anaconda.com/
[colab]: https://colab.research.google.com/

## Snippets

### stack

[documentation](https://docs.python.org/3/tutorial/datastructures.html?highlight=stack#using-lists-as-stacks)

> first in, last out

```python
# declaration
stack = [-1, 0]

# add item at the end
stack.append(1)
# get & remove last item
last_item = stack.pop()
# get last item
last_item = stack[-1]

# check if empty
if not stack:
    print("Empty")
```

related section: [list](#list)

### queue

[documentation](https://docs.python.org/3/tutorial/datastructures.html?highlight=stack#using-lists-as-queues)

> first in, first out

It's possible to implement queue using a list, **but** it's not memory efficient. Therefore, _deque_ module from the package _collections_ is used instead.

```python
from collections import deque

# declaration
queue = deque([-1, 0])
# queue
queue.append(1)
queue.append(2)
# dequeue
queue.popleft()

# check if empty
if not queue:
    print("Empty")
```

related section: [import module](#import-module)

### array

[documentation](https://docs.python.org/3.9/library/array.html)

Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained.

```python
from array import array

type_code = 'i'  # type code for int
numbers = array(type_code, [1, 2, 3])
number = 4
numbers.append(number)  # array('i', [1, 2, 3, 4])
numbers.append(number)  # array('i', [1, 2, 3, 4, 4])
index = 2
numbers.insert(index, number)  # array('i', [1, 2, 4, 3, 4, 4])
x = numbers.pop()  # x = 4 | numbers = array('i', [1, 2, 4, 3, 4])
numbers.remove(4)  # numbers = array('i', [1, 2, 3, 4])
# numbers[1] = 1.0  # TypeError: integer argument expected, got float
```

related section: [import module](#import-module)

### unpack string

related section: [tuple](#tuple)

```python
characters = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

### sorted function

[documentation](https://docs.python.org/3.9/library/functions.html#sorted)

#### sort list

```python
numbers = [5, 1, 8, 9, 0, 6, 50, 20]
print(sorted(numbers, reverse=True))  # output: [50, 20, 9, 8, 6, 5, 1, 0]  |   numbers = [5, 1, 8, 9, 0, 6, 50, 20]
print(sorted(numbers))  # output: [0, 1, 5, 6, 8, 9, 20, 50]    |   numbers = [5, 1, 8, 9, 0, 6, 50, 20]
```

#### sort dictionary

related section: [lambda expression](#lambda-expression)

```python
characters_frequency = {"a": 2, "b": 1, "c": 8}
print(sorted(
    characters_frequency.items(),
    key=lambda frequency_dict: frequency_dict[1],
    reverse=True))
```

### counter character frequency

[documentation](https://docs.python.org/3.9/library/collections.html#collections.Counter)

```python
# using built-in function
from collections import Counter

counter = Counter("hello world")

# Counter = ({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

```python
# using a dictionary
sentence = "hello world"
counter = {}
for character in sentence:
    counter[character] = counter.get(character, 0) + 1

# counter = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### pretty print

[documentation](https://docs.python.org/3.9/library/pprint.html#pprint.pprint)

```python
from pprint import pprint

x = {'w': 2, 'e': 4, 'l': 1, 'c': 1, 'o': 4, 'm': 2, ' ': 4, 't': 1, 'u': 1, 'r': 1, 'n': 1, 'h': 1}
pprint(x, width=1)
```

### get size of object

[documentation](https://docs.python.org/3.9/library/sys.html#sys.getsizeof)

```python
from sys import getsizeof

print("'a' takes", getsizeof('a'), "bytes of memory")  # 'a' takes 50 bytes of memory
```

### calculate runtime

#### using timestamp

related section: [timestamp](#timestamp)

```python
# using timeit
from timeit import timeit

code1 = """def xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    xfactor(0)
except ValueError as error:
    pass
"""

code2 = """def xfactor(age):
    if age <= 0:
        return None
    return 10 / age


x = xfactor(0)
if x is None:
    pass
"""

print("code1:", timeit(code1, number=10000))  # code1: 0.003757399999999994
print("code2:", timeit(code2, number=10000))  # code2: 0.001474000000000003
```

#### using datetime

related sections: [datetime](#datetime), [time deltas](#working-with-time-deltas)

```python
# using Epoch time
import time


# calculate execution time
def send_email():
    time.sleep(2)
    for i in range(1000):
        pass


start = time.time()
send_email()
end = time.time()
duration = end - start
```

### read file

#### using Path module

related section: [working with file](#working-with-files)

```python
# path object
from pathlib import Path

path = Path("file.text")

path.read_text()  # read file as string
```

#### using open function

related section: [open file](#open-file)

```python
# with open
with open("file.text", 'r') as file:
    file.readlines()  # list of lines as a strings
```

### copy file snippet

related sections: [working with file](#copy-file), [shutil](#shutil)

```python
# copy file
from pathlib import Path
import shutil

source = Path("text.py")
target = Path("text.txt")

# copy using path object
target.write_text(source.read_text())

# copy using shutil
shutil.copy(source, target)
```

### generate random password

related section: [random number generator](#random-number-generator), [string](#string)

> Warning: The pseudo-random generators of this module should not be used for security purposes. 
> For security or cryptographic uses, see the [secrets](https://docs.python.org/3.9/library/secrets.html#module-secrets) module.

```python
# generate a password of 8 letters & numburs 
import string
import secrets

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
```

### execute only if python file executed directly

related section: [module as a script](#module-as-a-script)

```python
if __name__ == '__main__':
    print("this file has been executed directly")
else:
    print("this file has been imported directly")
```

## Python Standard Library

As this section doesn't cover all the Standard Library, you are encouraged to take a look at [Standard Library Documentation](https://docs.python.org/3/library/index.html) 

### len function

[documentation](https://docs.python.org/3.9/library/functions.html#len) 

> length of object

```python
# length of string
len("hello")
# length of list
len([1, 2])
# length of tuple
len(tuple([1, 2]))
# length of set
len({1, 2})
```

### zip function

[documentation](https://docs.python.org/3/library/functions.html#zip)

> join two lists into one

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# similar length
joined_list = list(zip("abc", list1, list2))  # joined_list = [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
# vary length
joined_list = list(zip("abcd", list1, list2))  # joined_list = [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
```

### range function

[documentation](https://docs.python.org/3.9/library/stdtypes.html#range)

> `range` function generate an iterable object that give a new value in every iteration instead of making a list values

related section: [unpack-variables](#unpack-variables)

```python
end = 6
numbers = list(range(end))  # numbers = [0, 1, 2, 3, 4, 5]
start, end, step = 5, 12, 2
numbers = list(range(start, end, step))  # numbers = [5, 7, 9, 11]
```

### Random Number generator

[documentation](https://docs.python.org/3.9/library/random.html)

related sections: [generate random password](#generate-random-password), [string](#string)

> Warning: The pseudo-random generators of this module should not be used for security purposes.  
> For security or cryptographic uses, see the [secrets](https://docs.python.org/3.9/library/secrets.html#module-secrets) module.

```python
import random
import string

random_0_to_1 = random.random()
random_interval_int = random.randint(1, 10)  # 10 included
random_odd_numbers = random.randrange(1, 10, 2)  # (start, stop, range)
random_choice = random.choice(["python", "c", "c++", "java"])
multiple_random_choices = random.choices(["python", "c", "c++", "java"], k=2)
random_password = "".join(random.choices(string.ascii_letters + string.digits, k=4))

# in-place shuffle
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
```

### open file

[documentation](https://docs.python.org/3/library/functions.html#open)

reading modes can be found in documentation

```python
# with open
with open("file.text") as file:
    # do something
    pass
```

### open web browser

[documentation](https://docs.python.org/3.9/library/webbrowser.html)

```python
import webbrowser

webbrowser.open("https://www.google.com")
```

### send email

[documentation](https://docs.python.org/3/library/email.html)

related section: [string](#string)

```python
# forge message module
from email.mime.multipart import MIMEMultipart
# attach message body modules
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
# send message module
import smtplib
# Path module to read image
from pathlib import Path


# forge message header
message = MIMEMultipart()
message["from"] = "name"
message["to"] = "example@gmail.com"
message["subject"] = "this is a test"


# forge message body

# plain text
message.attach(MIMEText("hello"))

# html page
template = Template(Path("template.html").read_text())
# template file contents
"""<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    hello $name
</body>
</html>"""
body = Template.substitute(name="ahmad")
message.attach(MIMEText(body, "html"))

# image
message.attach(MIMEImage(Path("example.png").read_bytes()))


# send email
# host and port depends on smtp provider
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("example@gmail.com", "password")
    smtp.send_message(message)
    print("sent..")
```

### Command-line Arguments

[documentation](https://docs.python.org/3.9/library/sys.html)

related section: [run Python files](#run-python-files)

> sys.argv attribute contains `[python file name, ...Command-line Arguments]`

```python
import sys

if len(sys.argv) == 1:
    print("USAGE: python main.py <password>")
else:
    password = sys.argv[1]
    print("Password:", password)
```

### run a command in Command-line

[documentation](https://docs.python.org/3.9/library/subprocess.html)

```python
import subprocess

# command: ls -l

# print output on cmd
# completed = subprocess.run(["ls", "-l"])
# capture output in stdout attribute
completed = subprocess.run(["ls", "-l"],
                           capture_output=True,
                           text=True)

arguments = completed.args
return_code = completed.returncode
std_error = completed.stderr
stdout = completed.stdout
```

### shutil

related section: [copy file snippet](#copy-file-snippet)

shutil provides a high-level operations for files.

```python
from pathlib import Path
import shutil

source = Path("text.py")
target = Path("text.txt")

shutil.copy(source, target)
```

### Path

related section: [string](#string)

[Documentation](https://docs.python.org/3/library/pathlib.html)

- path can be relative or absolute.
  - path for windows: `C:\Program Files\Microsoft`
  - path for mac and linux: `user/local/bin`

```python
from pathlib import Path

# for windows

# back slash is written twice to escape it
Path("C:\\Program Files\\Microsoft")
# by using literal string, you write back slash only once
Path(r"C:\Program Files\Microsoft")


# for mac\linux
Path("user/local/bin")


# current folder
Path()

# combine path objects and strings
Path() / "ecommerce" / Path("../ecommerce")

# home directory
Path().home()
```

path object has a useful collection of methods.

#### Working With Directory

```python
from pathlib import Path

path = Path("ecommerce")

path.exists()
path.mkdir("test")
path.is_dir()
path.rmdir()
```

##### list directory content

> WindowsPath stands for windows based file system  
> PosixPath stands for mac\linux based file system

```python
from pathlib import Path

path = Path("ecommerce")

paths = [p for p in path.iterdir() if p.is_dir()]
# paths = [WindowsPath('ecommerce/customers'), WindowsPath('ecommerce/shopping'), WindowsPath('ecommerce/__pycache__')]
```

| method    | search by pattern | recursive list |
| --------- | ----------------- | -------------- |
| iterdir() | No*               | No             |
| globe()   | Yes               | Yes**          |
| rglobe()  | Yes               | Yes            |

> Note 1: You can filter in **iterdir** function using an if statement in a comprehensive list.  
> `[p for p in path.iterdir() if CONDITION]`

> Note 2: globe method can be used to list recursively by prefixing the path with (**).  
> `globe("**/*.py")`

###### "iterdir" function

```python
from pathlib import Path

path = Path("ecommerce")

# list all files and directories in path
paths = [p for p in path.iterdir()]
# filter by file suffix
py_files = [p for p in path.iterdir() if p.suffix == ".py"]
```

###### "globe" function

```python
from pathlib import Path

path = Path("ecommerce")

# search by pattern
py_files = [p for p in path.glob("*.py")]
# search by pattern, recursively
py_files = [p for p in path.glob("**/*.py")]
```

###### "rglobe" function

```python
from pathlib import Path

path = Path("ecommerce")

# search by pattern, recursively
py_files = [p for p in path.rglob("*.py")]
```

#### Working With Files

##### File Management

```python
from pathlib import Path

path = Path("test.txt")

path.exists()
path.is_file()
path.rename("text.py")
# remove file
path.unlink()
new_path = path.with_suffix(".py")  # new_path = text.py
```

##### File Stat

```python
from pathlib import Path
from time import ctime

path = Path("text.txt")

print(path.stat().st_ctime)  # 1631987149.6533422 | system dependent
print(ctime(path.stat().st_ctime))  # Sat Sep 18 20:45:49 2021
```

##### Read and Write File

```python
from pathlib import Path

path = Path("text.py")

# read text
path.read_bytes()  # read file as binary
path.read_text()  # read file as string

# write text
path.write_text("text")
path.write_bytes(b'10')
```

##### Copy File

related section: [copy file snippet](#copy-file-snippet)

```python
from pathlib import Path

source = Path("text.py")
target = Path("text.txt")

# copy using path object
target.write_text(source.read_text())
```

### working with zip files

[documentation](https://docs.python.org/3/library/zipfile.html)

related sections: [path](#path), [open file](#open-file)

```python
from pathlib import Path
from zipfile import ZipFile

# write a zip file from a directory
with ZipFile("files.zip", "w") as zip_file:
    for path in Path("directory").rglob("*.*"):
        zip_file.write(path)

# read and extract a zip file
with ZipFile("files.zip") as zip_file:
    # list files
    files_list = zip_file.namelist()
    # get file info
    info = zip_file.getinfo("file.txt")
    file_size = info.file_size
    compress_size = info.compress_size
    # extract zip file
    zip_file.extractall("extract all")
    zip_file.extract("file.txt", "extract")
```

### working with csv files

[documentation](https://docs.python.org/3.9/library/csv.html)

related section: [open file](#open-file)

> **csv** stands for Coma Separated Value

Only [open file](#open-file) can be used to open csv files.

with csv reader; you can iterate over a csv file **only once**.

```python
import csv

# write to file
with open("resource.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

# read file
with open("resource.csv") as file:
    # you can only iterate over csv object once
    reader = csv.reader(file)

    # list of rows
    data = list(reader)
    # read row by row
    for row in reader:
        print(row)
```

### working with JSON files

[documentation](https://docs.python.org/3/library/json.html?highlight=json#module-json)

Either [open file](#open-file) or [working with files](#working-with-files) can be used to read and write JSON files.

> JSON stands for JavaScript Object Notation

`loads()`, `dumps()` produce and return a **string**.  
While `load()`, `dump()` produce and return **fp** object(a .write()-supporting file-like object).

If the json file contains a non-asci characters, you should set `ensure_asci` flag to `False`.

```python
import json
from pathlib import Path

languages = [
    {"id": 1, "name": "Python", "type": "interrupted"},
    {"id": 2, "name": "c", "type": "compiled"}
]

# generate json string
data = json.dumps(languages, indent=4)
# write json file
Path("data.json").write_text(data)

# read json file
data = Path("data.json").read_text()
# load json string into python object
language = json.loads(data)
```

### working with SQLite database

[documentation](https://docs.python.org/3.9/library/sqlite3.html)

> To download SQLite database engine, head into [their official website](https://sqlitebrowser.org/)

> It's recommended to use an **ORM** _-stands for Object Relational Mapper-_ to manage a SQLite database,
> which maps a relational database system to python objects.
> 
> [SqlAlchemy](https://pythonspot.com/orm-with-sqlalchemy/) is one of the best ORMs for python.

```python
import sqlite3

languages = [
    {"id": 1, "name": "Python", "type": "interrupted"},
    {"id": 2, "name": "c", "type": "compiled"}
]

# insert resource
with sqlite3.connect("db.sqlite3") as connection:
    command = "INSERT INTO languages VALUES (?, ?, ?)"
    for language in languages:
        # execute command
        connection.execute(command, tuple(language.values()))
    # commit changes
    connection.commit()

# retrieve resource
with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM languages"
    # execute command
    cursor = connection.execute(command)
    # cursor can be iterated over only once
    # iterate over cursor
    for row in cursor:
        print(row)
    # fetch all rows
    languages = cursor.fetchall()
```

### timestamp

[documentation](https://docs.python.org/3/library/time.html)

> The epoch is the point where the time starts, and is platform dependent.

```python
import time

timestamp = time.time()  # timestamp = 1632115484.41066

# calculate execution time
def send_email():
    # sleep for 2 seconds
    time.sleep(2)
    for i in range(1000):
        pass


start = time.time()
send_email()
end = time.time()
duration = end - start
```

[convert timestamp into regular datetime](#datetime)

### datetime

[documentation](https://docs.python.org/3/library/datetime.html)

DateTime object represent a point of time.

```python
from datetime import datetime
from time import time

# datetime from parameters
past = datetime(2020, 1, 1, 11, 59, 59)
# datetime now
present = datetime.now()
# datetime string into object
dt = datetime.strptime("2020/01/01", "%Y/%m/%d")
# timestamp to datetime
dt = datetime.fromtimestamp(time())

print(f"{dt.year}/{dt.month}/{dt.day}")
print(dt.strftime("%Y/%m/%d"))

# comparison
print(past < present)
```

#### Working with Time Deltas

Time Deltas object represent a duration of time.

```python
from datetime import datetime, timedelta

# increase datetime by 2 days
past = datetime(2020, 1, 1, 11, 59, 59) + timedelta(days=2)
# datetime now
present = datetime.now()

duration = present - past  # type(duration) = datetime.timedelta
print(duration)  # 626 days, 1:41:55.764459
print(duration.days, "days")  # 626 days
print(duration.seconds, "seconds")  # 6115 seconds | represent time part of duration
print(duration.total_seconds(), "total seconds")  # 54092515.764459 total seconds
```

## Core Syntax

[general documentation](https://docs.python.org/3/tutorial/index.html)

### the walrus operator(`:=`)

[documentation](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions)

walrus operator`:=` assigns values to variables as part of a larger expression.

> Try to limit use of the walrus operator to clean cases that reduce complexity and improve readability.

```python
a: list = list(range(11))

# regular method
if len(a) > 10:
    print(f"List is too long ({len(a)} elements, expected <= 10)")
# the walrus operator
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

```python
from unicodedata import normalize

names = ["Mackintosh", "windows", "linux", "MacDonald's", "NFC"]
allowed_names = ["Mackintosh", "NFC"]

[clean_name.title() for name in names if (clean_name := normalize('NFC', name)) in allowed_names]
```

### del statement

[documentation](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)

```python
del object
```

### pass statement

[documentation](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)

`pass` statement is used to fill empty blocks.

```python
if True:
    pass
```

### scope

[documentation](https://docs.python.org/3/tutorial/classes.html?highlight=scope#scopes-and-namespaces-example)

related section: [coding-conventions](#coding-conventions)

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)  # After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam)  # After global assignment: nonlocal spam

scope_test()
print("In global scope:", spam)  # In global scope: global spam
```

### Print Statement

[documentation](https://docs.python.org/3/library/functions.html#print),

> [pretty print](#pretty-print) is an alternative for print which **pretty** print it's input

#### simple form

```python
print("hello world")
print('*' * 8)  # print * 8 times
```

#### print Multiple Strings

```python
first = "ali"
last = "ahmad"

# print full name
print(first + " " + last)  # concatenation
print(f"{first} {last}")  # both 'F' and 'f' are valid
print(first, last)

# expressions
# print(len(first) + " " + 2 + 2) # error | concatenation only accept string
print(f"{len(first)} {2 + 2}")
print(len(first), 2 + 2)
 ```

### User Input

[documentation](https://docs.python.org/3.9/library/functions.html#input)

```python
x = input("input: ")  # return a string type
print(x)
```

### Numbers

#### Numbering Systems

[bin documentation](https://docs.python.org/3.9/library/functions.html#bin)
[hex documentation](https://docs.python.org/3.9/library/functions.html#hex)

```python
d = 10  # decimal
b = 0b10  # binary
h = 0x12c  # hex

print(1)  # decimal is the default numbering system
print(bin(1))  # print number as a binary number
print(hex(1))  # print number as a hex number

# a + bi  | imaginary number
x = 1 + 2j  # x = 1 + 2J
# output: (1+2j)
 ```

#### Arithmetic Operations

[documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

```python
add = 5 + 2
subtract = 5 - 2
multiply = 5 * 2
divide_with_fraction = 5 / 2  # 2.5
divide_without_fraction = 5 // 2  # 2

reminder = 5 % 2  # 1
power = 5 ** 2  # 25

minus_five = -5
plus_five = +5
```

#### Augmented Assignment Operator

```python
x = 1
# apply to all arithmetic operations
x = x + 2
# same as
x += 2

# no increment(x++) or decrement(x--) in python
```

#### Math module

[math documents](https://docs.python.org/3/library/math.html)

```python
import math

PI = -3.14
print(round(PI))
print(abs(PI))  # absolute

print(math.floor(PI))
print(math.sqrt(PI))
```

### Type Annotation/hinting

[official documentation](https://docs.python.org/3/library/typing.html), [fastapi documentation](https://fastapi.tiangolo.com/python-types/)

> Note: The Python runtime does not enforce type annotations.  
> Instead, they can be used by third party tools such as type checkers, IDEs, linters, etc.

```python
# Variable
age: int = 10
age: int
score: float = 4.5
score: float
active: bool = False
active: bool
name: str = "john"
name: str
empty: None = None
x: any

my_list: list[str] = ['a', 'b']
my_tuple: tuple
my_dict: dict
my_set: set


# function
def increment(number: int, by: float, extra: list[str]) -> tuple:
    return number, number + by


values: tuple = increment(1, 1.5, ["a", "b"])
```

### Data types

[documentation](https://docs.python.org/3.9/library/stdtypes.html)

related section: [function as a variable](#function-as-a-variable)

```python
int_type = 1
float_type = 1.5
boolean_type = False  # True\False
empty = None

# string type
multiple_lines = """first line
second line"""
multiple_lines = '''first line
second line'''
single_line_string = "john"
single_line_character = 'j'
single_line_character = 'john'

# byte type
byte_type = b"10"
 ```

#### truth values

[documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

Any object can be tested for truth value.

False values are(Anything else is True):

- constants defined to be false: `False`, `None`
- zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

### Variables

[documents](https://docs.python.org/3/library/stdtypes.html)

#### variable declaration

```python
# There's no constant variable in python. Therefore, all capital words are used by convenient to inform programmer to not edit value.
PI = 3.14

count = 1  # value only
count: int  # type only
count: int = 1  # type and value
# the same can be done with any type of resource
```

#### unpack variables

related section: [tuple](#tuple)

```python
x = 1
y = 2
# same as
x, y = 1, 2
```

```python
numbers = (1, 2, 3, 4)
first, second, third, forth = numbers
```

> it's possible to use `match` statement to unpack a variable. go to [Patterns with a literal and variable](#patterns-with-a-literal-and-variable) section for more information

#### swap variables

related section: [tuple](#tuple)

```python
x = 1
y = 2

x, y = y, x  # equivalent to: x, y = (y, x)
```

#### assign one value to multiple variables

```python
a = b = 1
```

#### Python is a **dynamic** language

```python
a = 1
print(type(a))  # int

a = 3.14
print(type(a))  # float

a = True
print(type(a))  # bool
```

### Type Casting

```python
int(True)
float("1.5")
bool(None)
str(1)
```

### String

[documentation](https://docs.python.org/3.9/library/stdtypes.html#text-sequence-type-str)

related section: [print statement](#print-statement)

```python
x_eight_times = "x" * 8
byte_string = b"10"
first = "ali"
last = "ahmad"

# Literal String Interpolation
full = f"{first} {last}"
# raw string
path = r"C:\Program File\Microsoft"


single_line_character = 'j' + 'john'  # same as: "j" + "john"
multiple_lines = """first line
second line"""
multiple_lines = '''first line
second line'''
```

> `f"{varible=}"` can be used for [self-documenting expressions and debugging](https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging)

#### some string methods

```python
course = "python programming"

# change letter case
course.upper()
course.lower()
course.title()

# strip white spaces
course.strip()  # from both sides
course.lstrip()  # from left side
course.rstrip()  # from right side

# find substring
course.find("pro")  # case sensitive

# replace text
course.replace("p", "-")

# Split String
course.split(' ')

# join a list of strings separated by ','
','.join(["ab", "cd", "ef"])

# check if sequence of characters exist
print("python" in course)  # case sensitive
```

##### string sets

```python
import string

ascii_letters = string.ascii_letters
digits = string.digits
```

#### template

```python
import string

template = string.Template("hello $name")
message = template.substitute({"name": "ahmad"})  # or
message = template.substitute(name="ahmad")
```

#### combine strings

```python
first = "ali"
last = "ahmad"

# no expressions
full = " ".join([first, last])  # join method
full = first + " " + last  # concatenation
# or
full = f"{first} {last}"
# or
full = F"{first} {last}"

# with expressions
full = len(first) + " " + 2 + 2  # error
full = f"{len(first)} {2 + 2}"
```

#### Access Parts of The String

```python
course = "python programming"
len(course)  # length of string

# access parts of the string

## access individual character  | course[index]
first_element = course[0]  # 'p'
second_element = course[1]  # 'y'
last_element = course[-1]  # 'g'
third_element_from_the_end = course[-3]  # 'i'

## access range of characters(slice string)  
## course[start index:exclusive end index]
course[0:3]  # "pyt" | character in index 3 is excluded
course[:3]  # "pyt" | start = 0
course[0:]  # "python programming"  | end = length of string
course[:]  # "python programming"  | whole string
```

#### Escape Character

```python
# the strings below will cause an error
## message = "python "programming"
## message = 'python 'programming'
```

```python
# in order to deal with that, you can use one of the two methods below:
message = 'python "programming'  # 1st method
message = "python \"programming"  # 2nd method  | escape character

"There are 4 escape Sequences in python: \" \' \n \\"
```

### lambda expression

```python
# sort a list of tuples
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)  # items = [('Product2', 9), ('Product1', 10), ('Product3', 12)]
# -------------same as(lambda expression)------------
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
# items.sort(key=lambda parameter: expression)
items.sort(key=lambda item: item[1])  # items = [('Product2', 9), ('Product1', 10), ('Product3', 12)]
```

### If Condition

[if-statements documentation](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

related section: [truth values](#truth-values)

#### General Structure

```
if conditions:
    pass
elif conditions:
    pass
else:
    pass
```

#### Comparison

[documentation](https://docs.python.org/3/library/stdtypes.html#comparisons)

```python
if 6 == 5:
    pass
elif 6 >= 5:
    pass
elif 6 > 5:
    pass
elif 6 <= 5:
    pass
elif 6 < 5:
    pass
elif 6 != 5:
    pass
```

#### Boolean Operations(`and`, `or`, `not`)

[documentation](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

```python
if not (1 == 2) or (1 != 2):
    pass

if 2 == 2 and 1 != 2:
    pass

# complex expression
x = 5
y = x

if ((x is y) and (x > 4)) or ((x < 4) and (not y == x)):
    print("hello")
```

#### `not`, `in`, `is`

```python
name = "world"
x = 5
y = x

# in
if x in range(5):
    pass
elif x in [1, 2, 4, 6]:
    pass
elif name in "hello":
    pass

# not
if not name:
    print("name is empty")

# not in
elif name not in "hello world":
    pass

# is
if x is y:
    pass
a = 0
b = 0

# is not
if a is not b:
    pass
```

#### Chaining Comparison Operator

```python
age = 25

if age >= 18 and age < 65:
    print("Eligible")
# same as   (chaining comparison operator)
if 18 <= age < 65:
    print("Eligible")
```

#### Ternary Operator

```python
age = 25

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
# same as (Ternary Operator)
message = "Eligible" if age >= 18 else "Not eligible"

print(message)
```

### For Loop

[documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

#### for

```python
for character in "python":
    print(character)

for character in ['p', 'y', 't', 'h', 'o', 'n']:
    print(character)

for number in range(10):
    print(number)
```

#### for...else

[documentation](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

> `else` block will only be executed if the loop is computed successfully without a **break**

```python
names = ["ahmad", "samir"]

for name in names:
    if name.startswith('a'):
        print("Found")
        break
    else:
        continue
else:
    print("Not found")
```

#### enumerate

[documentation](https://docs.python.org/3/library/functions.html#enumerate)

```python
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
```

### Generator Expressions

[documentation](https://docs.python.org/3/tutorial/classes.html?#generator-expressions)

> [Difference between Yield and Return](https://www.pythonforbeginners.com/basics/difference-between-yield-and-return-in-python)

> **generator** generates a value in each iteration -unlike _lists_ which stores the values in memory-
> but has no length because of its nature.  
> generator has a fixed size regardless of the number of generated values

```python
# declaration
generator = (number * 2 for number in range(5))  # <generator object <genexpr> at 0x00000279738FE900>

for value in generator:
    print(value)

# generator size
from sys import getsizeof

generator1 = (number * 2 for number in range(5))
print("a generator of 5 items takes", getsizeof(generator1), "bytes of memory")
# generator of 5 items takes 112 bytes of memory
generator2 = (number * 2 for number in range(100000000))
print("a generator of 100000000 items takes", getsizeof(generator2), "bytes of memory")
# a generator of 100000000 items takes 112 bytes of memory

print("as you can see, generator size is the same no matter how many values can be generated")

print("a list of 100000000 items takes", getsizeof([number * 2 for number in range(100000000)]), "bytes of memory")
# a list of 100000000 items takes 835128600 bytes of memory
```

### Comprehensive List

[documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

> **comprehensive list** is the best practice to map and filter lists

> it's recommended to use [comprehensive list](#comprehensive-list) instead of [for loop](#for-loop) whenever possible

```python
# for loop
values = []
for number in range(5):
    values.append(number * 3)

# comprehensive list
values = [number * 3 for number in range(5)]
```

```python
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# primitive way
prices = []  # prices = [10, 9, 12]
for item in items:
    prices.append(item[1])
# map function
prices = list(map(lambda item: item[1], items))  # prices = [10, 9, 12]
# Comprehensive List
prices = [item[1] for item in items]  # prices = [10, 9, 12]
```

related section: [map list](#map-list)

```python
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# primitive way
filtered = []  # filtered = [('Product1', 10), ('Product3', 12)]
for item in items:
    if item[1] >= 10:
        filtered.append(item)
# filter function
filtered = list(filter(lambda item: item[1] >= 10, items))  # filtered = [('Product1', 10), ('Product3', 12)]
# comprehensive list
filtered = [item for item in items if item[1] >= 10]  # filtered = [('Product1', 10), ('Product3', 12)]
```

related section: [filter list](#filter-list)

#### comprehensive is not limited to lists

```python
# list
values = [number * 2 for number in range(5)]
# set
values = {number * 2 for number in range(5)}
# dictionary
values = {number: number * 2 for number in range(5)}
# generator
generator = (number * 2 for number in range(5))
```

> head to [generator expression](#generator-expressions) section for more info about generator

### While Loop

> `else` block will only be executed if the loop is computed successfully without a **break**

related section: [for loop](#for-loop)
```python
guess = 0
answer = 5
while guess != answer:
    guess = input("guess: ")
else:
    print("correct guess")
```

### Functions

[documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

related section: [documentation string](#doc-string)

> [Difference between Yield and Return](https://www.pythonforbeginners.com/basics/difference-between-yield-and-return-in-python)

#### Bare Minimum

```python
def my_function():
    pass


# function call
my_function()
```

#### parameters

There are two type of arguments:

- positional: `function(1)`
- keyword: `function(number=5)`

```python
# define function
def my_functions(a, b: str, c: str = "default", d="default") -> int:
    return 10


# call function
my_functions(1, 'a', c='c')
# my_functions(positional, positional, keyword)
```

##### Positional-only parameters

- `/` indicates that function parameters **before** it must be **specified positionally** and cannot be used as keyword arguments. 
- `*` indicates that function parameters **after** it must be **specified** as **keyword** arguments and cannot be used positionally.

In the following example : 
- parameters a and b are positional-only
- while c or d can be positional or keyword, 
- and e or f are required to be keywords:

```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# valid call
f(10, 20, 30, d=40, e=50, f=60)

# invalid call
f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument
```

##### pass an arbitrary number of arguments

By prefixing a parameter with `*`, python will **package** the passed arguments into a *tuple*

```python
def multiply(*numbers):
    total: int = 1
    for number in numbers:
        total *= number
    return total


multiply(1, 2, 3, 4, 5, 6, 7)
```

##### pass an arbitrary number of **keyword** arguments

By prefixing a parameter with `**`, python will **package** the passed keyword arguments into a *dictionary*

```python
def save_user(**user):
    print(user)  # {'id': 1, 'username': 'admin'}


save_user(id=1, username="admin")
```

#### Return Multiple Values

related section: [tuple](#tuple)

```python
def increment(a: int, b: int):
    return a, a + b  # return a tuple


print(increment(5, 2))  # (5, 7)
```

#### function as a variable

```python
def addition(x: int):
    return x + 3


add = addition
for number in range(6):
    print(add(number), end=" ")

# output:
# 3 4 5 6 7 8 
```

### Data Structure

| name       | structure          | features                                                 |
| ---------- | ------------------ | -------------------------------------------------------- |
| list       | `[1, 'a']`         | read and write list                                      |
| tuple      | `(1, 'a')`         | read **only** list                                       |
| set        | `{1, 2, 3}`        | read and write unordered collection of **unique** values |
| dictionary | `{"x": 1, "y": 2}` | key-value pairs with no repeated keys                    |

related sections: [named tuple](#data-class), [stack](#stack), [queue](#queue), [array](#array)

#### list

[documentation](https://docs.python.org/3.9/library/stdtypes.html#lists),
[documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

related section: [unack list](#unpack-list)

```python
# declaration
letters = ['a', 'b', 'c', 'd']
matrix = [[1, 2], [3, 4]]
zeros = [0] * 5  # [0, 0, 0, 0, 0]
combined = letters + zeros  # concatenation
numbers = list(range(8))  # [1, 2, 3, 4, 5, 6, 7]
characters = list("hello world")  # extract characters from a string
```

```python
# access list items
letters = ['a', 'b', 'c', 'd']
first_item = letters[0]
second_item = letters[1]
last_item = letters[-1]
second_last_item = letters[-2]
```

```python
# slice list    |   create a new sliced list
letters = ['a', 'b', 'c', 'd']
print(letters[0:3])  # ['a', 'b', 'c']
print(letters[:3])  # ['a', 'b', 'c']
print(letters[0:])  # ['a', 'b', 'c', 'd']
print(letters[:])  # ['a', 'b', 'c', 'd']
```

```python
# slice while skipping some items
numbers = list(range(20))
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::-2])  # [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
```

```python
# modify a list item
letters = ['a', 'b', 'c', 'd']
letters[0] = "A"  # ['A', 'b', 'c', 'd']
letters[1:3] = "B", "C"  # ['A', 'B', 'C', 'd'] | packing
```

```python
# list unpacking
numbers = [1, 2, 3, 4]

first = numbers[0]
second = numbers[1]
third = numbers[2]
# ---------same as-------------
first, second, third, forth = numbers  # first = 1  |   second = 2  |   third = 3   |   forth = 4

# -----------------------------

first, second, *other = numbers  # first = 1    |   second = 2  |   other = [3, 4]
first, *other, last = numbers  # first = 1      |   other = [2, 3]  |   last = 4
```

```python
# loop over a list
letters = ['a', 'b', 'c']

for letter in letters:
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)
```

```python
# list operations/methods
letters = ['a', 'b', 'd', 'b', 'c', 'e']

# add
letters.append('d')  # ['a', 'b', 'd', 'b', 'c', 'e', 'd']
letters.insert(0, '-')  # ['-', 'a', 'b', 'd', 'b', 'c', 'e', 'd']

# remove
letters.pop()  # ['-', 'a', 'b', 'd', 'b', 'c', 'e']
letters.pop(0)  # ['a', 'b', 'd', 'b', 'c', 'e']
letters.remove('b')  # ['a', 'd', 'b', 'c', 'e']
del letters[0:3]  # ['c', 'e']
letters.clear()  # []   | remove all elements of a list

# count occurrence of elements in a list
letters = ['a', 'b', 'b', 'c']
letters.count('b')  # 2

# find element index
if 'b' in letters:  # index method raise an error if element doesn't exist
    letters.index('b')

# sort
# in-place
numbers = [5, 1, 8, 9, 0, 6, 50, 20]
numbers.sort()  # numbers = [0, 1, 5, 6, 8, 9, 20, 50]
numbers.sort(reverse=True)  # numbers = [50, 20, 9, 8, 6, 5, 1, 0]
# create a new sorted list
numbers = [5, 1, 8, 9, 0, 6, 50, 20]
print(sorted(numbers, reverse=True))  # output: [50, 20, 9, 8, 6, 5, 1, 0]  |   numbers = [5, 1, 8, 9, 0, 6, 50, 20]
print(sorted(numbers))  # output: [0, 1, 5, 6, 8, 9, 20, 50]    |   numbers = [5, 1, 8, 9, 0, 6, 50, 20]
```

##### map list

related section: [comprehensive list](#comprehensive-list)

```python
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

prices = [item[1] for item in items]  # prices = [10, 9, 12]
```

##### sort list of tuples

related section: [lambda expression](#lambda-expression)

```python
# sort a list of tuples
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

items.sort(key=lambda item: item[1])  # items = [('Product2', 9), ('Product1', 10), ('Product3', 12)]
```

##### filter list

related section: [comprehensive list](#comprehensive-list)

```python
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

filtered = [item for item in items if item[1] >= 10]  # filtered = [('Product1', 10), ('Product3', 12)]
```

##### merge lists

related section: [unpack list](#unpack-list)

```python
numbers = [*range(1, 4)]  # [1, 2, 3]
characters = [*"hello"]  # ['h', 'e', 'l', 'l', 'o']
mixture = [*numbers, ':', *characters, 2]  # [1, 2, 3, ':', 'h', 'e', 'l', 'l', 'o', 2]
```

#### tuple

[documentation](https://docs.python.org/3.9/library/stdtypes.html#tuples),
[documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

> read only list

```python
# declaration
my_tuple = (1, 2)  # (1, 2)
my_tuple = 1, 2  # (1, 2)
my_tuple = (1,)  # (1)
my_tuple = 1,  # (1)
empty_tuple = ()  # ()

# concatenation
my_tuple = (1, 2) + (3, 4)  # (1, 2, 3, 4)

# repeat a tuple
my_tuple = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

characters = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

related section: [unpack string](#unpack-string)

```python
# access tuple items
letters = ('a', 'b', 'c', 'd')
first_item = letters[0]
second_item = letters[1]
last_item = letters[-1]
second_last_item = letters[-2]

# slice tuple    |   create a new sliced tuple
print(letters[0:3])  # ('a', 'b', 'c')
print(letters[:3])  # ('a', 'b', 'c')
print(letters[0:])  # ('a', 'b', 'c', 'd')
print(letters[:])  # ('a', 'b', 'c', 'd')

# slice and skip some items
numbers = tuple(range(20))
print(numbers[::2])  # (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
print(numbers[::-2])  # (19, 17, 15, 13, 11, 9, 7, 5, 3, 1)

# check if item exist
numbers = (1, 2, 3, 4)
if 1 in numbers:
    print("exist")

# tuples can't be edited
my_tuple = (1, 2)
my_tuple[0] = 2  # error: tuple doesn't support item assignment
```

```python
# tuple unpacking
numbers = (1, 2, 3, 4)

first = numbers[0]
second = numbers[1]
third = numbers[2]
forth = numbers[3]
# ---------same as-------------
first, second, third, forth = numbers  # first = 1  |   second = 2  |   third = 3   |   forth = 4

# swap variables
x = 1
y = 2
x, y = y, x

# pack and unpack
first, second, *other = numbers  # first = 1    |   second = 2  |   other = [3, 4]
first, *other, last = numbers  # first = 1      |   other = [2, 3]  |   last = 4
```

related section: [swap variables](#swap-variables), [unpack variable](#unpack-variables)

#### set

[documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)

> **unordered** **unique** collection of objects

```python
# declaration
numbers = {1, 2, 2, 3, 4}  # numbers = {1, 2, 3, 4}
numbers = set([1, 2, 2, 3, 4])  # numbers = {1, 2, 3, 4}

# add item
numbers.add(1)  # numbers = {1, 2, 3, 4}
numbers.add(5)  # numbers = {1, 2, 3, 4, 5}

# numbers.remove(10)  # error: element doesn't exist
numbers.remove(5)  # # numbers = {1, 2, 3, 4}

# as sets are unordered collections, you can't access them by index
numbers[0]  # error

# --------operations--------------
first = set([1, 2, 2, 3, 4])  # first = {1, 2, 3, 4}
second = {1, 5}

# union
print("union:", first | second)  # {1, 2, 3, 4, 5}
# intersection
print("intersection:", first & second)  # {1}
# difference
print("difference:", first - second)  # {2, 3, 4}
# semantic difference   | in one set or the another, but not both
print("semantic difference:", first ^ second)

# check if exist
if 1 in numbers:
    print("exist")
```

#### dictionary

[documentation](https://docs.python.org/3.9/library/stdtypes.html#mapping-types-dict),
[documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

> key can be only immutable type

```python
# declaration
point = {'x': 1, 'y': 2}
point = dict(x=1, y=2)

# access dictionary
print(point['x'])  # 1
# if key doesn't exist, an error get raised, to deal with that:
# 1. check if key exist
if 'a' in point:
    point['a']
# 2. use get method
print(point.get('a'))  # if key doesn't exist, 'get' return None
default = 0
print(point.get('a', default))  # if key doesn't exist, 'get' return 0

# assignment
point['z'] = 3  # point = {'x': 1, 'y': 2, 'z': 3}
point['z'] = 2  # point = {'x': 1, 'y': 2, 'z': 2}

# delete item
del point['z']
print(point)
```

```python
# loop over a dictionary
person = dict(id=1, score=5)

for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

> it's recommended to use [comprehensive list](#comprehensive-list) instead of [for loop](#for-loop) whenever possible

##### merge dictionaries

related section: [unpack dictionary](#unpack-dictionary)

There are two ways to merge dictionaries:

- `**` [unpack operator](#unpack-dictionary)
- `d | other` operator
  - Create a **new** dictionary with the merged keys and values of d and other
  - which **must both be dictionaries**
  - The values of **other** take **priority** when d and other share keys.
- `d |= other` operator
  - Update the dictionary d with keys and values from other
  - which may be either a [mapping](https://docs.python.org/3/glossary.html#term-mapping) or an [iterable](https://docs.python.org/3/glossary.html#term-iterable) of key/value pairs.
  - The values of **other** take **priority** when d and other share keys.
- `update(other)` function

```shell
>>> x = {"key1": "value1 from x", "key2": "value2 from x"}
>>> y = {"key2": "value2 from y", "key3": "value3 from y"}
>>> x | y
{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
>>> y | x
{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}
```

### unpack operator

#### unpack list

related section: [list](#list)

`*` is used to unpack a list.

```python
numbers = [*range(1, 4)]  # [1, 2, 3]
characters = [*"hello"]  # ['h', 'e', 'l', 'l', 'o']
mixture = [*numbers, ':', *characters, 2]  # [1, 2, 3, ':', 'h', 'e', 'l', 'l', 'o', 2]
```

#### unpack dictionary

related section: [merge dictionaries](#merge-dictionaries)

`**` is used to unpack a dictionary.

```python
first = {'x': 1, 'y': 2}
second = {'x': 10}
combined = {**first, **second, 'z': 3}  # {'x': 10, 'y': 2, 'z': 3}
```

### Exceptions

[documentation](https://docs.python.org/3/tutorial/errors.html)

[built-in exception documentations](https://python.readthedocs.io/en/stable/library/exceptions.html)

#### handling exceptions

related section: [release resource](#finally-clause)

```python
try:
    file = open("app.py")
    age = int(input("age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:  # this block is used to release resources
    file.close()
```

##### Single exception

```python
try:
    age = int(input("age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)  # invalid literal for int() with base 10: 'a'
    print(type(ex))  # <class 'ValueError'>
else:
    print("No exceptions were thrown.")
```

##### Multiple exceptions

```python
try:
    age = int(input("age: "))
    x = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# same as
try:
    age = int(input("age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

##### Only one except clause get handled, the other get ignored

```python
try:
    age = int(input("age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except ZeroDivisionError:  # this except clause doesn't get executed
    print("You didn't enter a valid age.")

else:
    print("No exceptions were thrown.")

# output
# age: 0
# You didn't enter a valid age.
```

##### raise an exception

> only raise an exception if you **really have to** as they _complicate_ the code and are _more costly_ execution-wise.

> You can raise your own exception instead of using the built-in exceptions.

```python
# raise an exception
def xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    xfactor(0)
except ValueError as error:
    print(error)


# return None value
def xfactor(age):
    if age <= 0:
        return None
    return 10 / age


x = xfactor(0)
if x is None:
    print("Age cannot be 0 or less")
```

check [calculate runtime](#calculate-runtime) for more information about the cost

#### create a custom exception

related section: [class](#class)

```python
# create a custom exception
class CustomError(Exception):
    pass


# raise the exception
raise CustomError
```

### release resource

You should release resource after using them.

#### `finally` clause

```python
try:
    file = open("app.py")
    age = int(input("age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:  # this block is used to release resources
    file.close()
```

#### `with` statement

[documentation](https://docs.python.org/3.9/library/stdtypes.html#context-manager-types)

`with` statement can only be used if the object support _context management protocol_ by having the
methods(`file.__enter__()`, `file.__exit__()`)

```python
try:
    with open("app.py") as file:  # file get closed after this block get executed
        print("file opened.")
    age = int(input("age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
```

##### open multiple resources at once

```python
with open("app.py") as file, open("readme.md") as target:
    print("file opened.")
```

> Change in python 3.10: Enclosing parentheses for continuation across multiple lines.

[documentation](https://docs.python.org/3/whatsnew/3.10.html#parenthesized-context-managers)

```python
with (CtxManager() as example):
    pass

with (
    CtxManager1(),
    CtxManager2()
):
    pass

with (CtxManager1() as example,
      CtxManager2()):
    pass

with (CtxManager1(),
      CtxManager2() as example):
    pass

with (
    CtxManager1() as example1,
    CtxManager2() as example2
):
    pass
```

```python
with (
    CtxManager1() as example1,
    CtxManager2() as example2,
    CtxManager3() as example3,
):
    pass
```

### `match` statement

[Documentation](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching)

> `match` statement is an equivalent to using multiple if conditions to match a single variable against multiple cases

```python
# generic syntax
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case <pattern_4> | <pattern_5> | <pattern_6>:
        <action_4>
    case _:
        <action_wildcard>
```

| Part                                              | Info                                                               |
| ------------------------------------------------- | ------------------------------------------------------------------ |
| `case <pattern>:`                                 | the first matching pattern get executed                            |
| `case <pattern_4> \| <pattern_5> \| <pattern_6>:` | if any of the patterns match, the case block get executed          |
| `case _:`                                         | (optional) executed if no case match -similar to `default` clause- |

> patterns don’t match iterators

#### match to a literal

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

#### `as` statement in `case`

```python
def http_error(status=400):
    match status:
        case 400 as error_code:
            print(f"{error_code}: Bad request")
```

#### Patterns with a literal and variable

related section: [unpack variable](#unpack-variables)

Patterns may be used to bind variables.

```python
point = (1, 0)

match point:
    # unpack and match a tuple
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

print(f"x={x}")
```

```python
point = {"x": 1, "y": 2}

match point:
    case {"x": a, "y": b}:
        print(f"X={a}, Y={b}")
```

```python
    point = (1, 0)

    match point:
        case (x, y):
            print(f"X={x}, Y={y}")
    # similar to 
    x, y = point
```

#### match a class

Patterns may be used to capture class attributes into variables.

```python
class Point:
    x: int
    y: int

def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")
```

```python
class Point2D:
    x: int
    y: int


class Point3D:
    x: int
    y: int
    z: int


def location(point):
    match point:
        case Point2D(x=x, y=y):
            print(f"2D point: x={x}, y={y}")
        case Point3D(x=x, y=y, z=z):
            print(f"3D point: x={x}, y={y}, z={z}")
        case _:
            print("Not a point")
```

#### Patterns with positional parameters

[documentation](https://docs.python.org/3/whatsnew/3.10.html#patterns-with-positional-parameters)

by setting `__match_args__` attribute to `("x", "y")`, we can use positional arguments in `match` cases. As a result, `y` attribute bind to `var` variable in all these cases.

```python
class Point:
    x: int
    y: int
    __match_args__ = ("x", "y")


def location(point):
    match point:
        case Point(1, var):
            print(f"var={var}")
        case Point(1, y=var):
            print(f"var={var}")
        case Point(x=1, y=var):
            print(f"var={var}")
        case Point(y=var, x=1):
            print(f"var={var}")
```

#### Nested patterns

```python
match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point {x}, {y} is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
    case _:
        print("Something else is found in the list.")
```

#### Complex patterns and the wildcard

```python
match test_variable:
    case ('warning', code, 40):
        print("A warning has been received.")
    case ('error', code, _):
        print(f"An error {code} occurred.")
```

```python
match [1, 2, 3, 4 , 5]:
    # extract first, second, last items
    case [x, y, *_, last]:
        print(x, y, last)  # 1, 2, 5
    # extract first, second, rest items
    case [x, y, *rest]:
        print(rest)  # [3, 4, 5]
```

#### guard

> Value capture happens before the guard is evaluated.

```python
match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")
```

#### Named constants in pattern

```python
from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```

### `assert` keyword

> The `assert` keyword is used when debugging code

`assert` keyword:

- do nothing if condition is true
- raise **AssertionError** if condition is false

```python
message = "hello"

# if condition return true, no thing happen
assert message == "hello"

# if condition return false, AssertionError is raised
assert message == "good bye"  # AssertionError
assert message == "goodbye", "message should be hello"  # AssertionError: message should be hello
```

### class

[documentation](https://docs.python.org/3/tutorial/classes.html?#a-first-look-at-classes)

related section: [function](#functions)

> A method is a function that belongs to a class

#### general structure

```python
class Point:
    # declare class attribute
    number_of_points = 0

    def __init__(self, x: str = "variable of a method"):
        # access attribute
        self.number_of_points += 1

        # declare instance attribute
        self.x = x

        x  # parameter
        self.x  # instance attribute

    def instance_method(self):
        pass


# make class instance
point = Point()

# access an attribute
point.x

# call instance method
point.instance_method()

# reassign an attribute
point.x = 1
```

#### data class

`named tuple` -which is an immutable object- can be used for a class of only data.
```python
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
point1 = Point(x=1, y=2)
point2 = Point(x=1, y=2)
print(point1 == point2)  # True
# point1.x = 2  # named tuples are immutable
point1 = Point(2, point1.y)
```

#### public and private members

[documentation](https://docs.python.org/3/tutorial/classes.html?#private-variables)

> public members are accessible from outside the class

> private members are prefixed with `__` which makes them hard to access, but not impossible.

```python
class MyClass:
    __private_class_attribute = "private class attribute"
    public_class_attribute = "public class attribute"

    def __init__(self):
        self.__private_instance_attribute = "private instance attribute"
        self.public_instance_attribute = "public instance attribute"

        # call a private method inside the class
        self.__private_method()
        
        # call a public method inside the class
        self.public_method()

        # access a private attribute inside the class
        self.__private_instance_attribute
        self.__private_class_attribute
        
        # access a public attribute inside the class
        self.public_instance_attribute
        self.public_class_attribute

        
    def __private_method(self):
        print("private method")

        
    def public_method(self):
        print("public method")


my_class = MyClass()

# call/access a public member

# call a public method outside of the class
my_class.public_method()

# access public attributes outside of the class
public_instance_attribute = my_class.public_instance_attribute
public_class_attribute = my_class.public_class_attribute

# assign public attributes outside of the class
my_class.public_class_attribute = "new public class attribute"
my_class.public_instance_attribute = "new public instance attribute"


# call/access a private member!

# call a private method outside of the class
# my_class.__private_method()  # raise an error
my_class._MyClass__private_method()

# access a private attributes outside of the class
# my_class.__private_instance_attribute  # raise an error
# my_class.__private_class_attribute  # raise an error
private_instance_member = my_class._MyClass__private_instance_attribute
private_class_member = my_class._MyClass__private_class_attribute

# assign a private attributes outside of the class
my_class._MyClass__private_instance_attribute = "new private instance attribute"
my_class._MyClass__private_class_attribute = "new private class attribute"

# get list of private and public instance attribute
print(my_class.__dict__)
# {'_MyClass__private_instance_attribute': 'private instance attribute',
# 'public_instance_attribute': 'public instance attribute'}
```

#### class and instance methods

There are two types of methods:

| method type     | corresponding parameter | parameter reference to | used to access                            |
| --------------- | ----------------------- | ---------------------- | ----------------------------------------- |
| instance method | `self`                  | the instance           | instance's **methods** and **attributes** |
| class method    | `cls`                   | the class itself       | the class itself                          |

> Note 1: class method should be decorated with `@classmethod`.  
> Note 2: _corresponding parameter_ -the first parameter in the method- can be named anything, it gets its name by **convention**.

```python
class MyClass:

    # instance method(magic method -> constructor)
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # instance method
    def instance_method(self):
        pass

    # class method
    @classmethod
    def class_method(cls):
        return cls(1, 2)


# create class instance
my_class_obj = MyClass(1, 2)  # internally call __intit__ method
my_class_obj = MyClass.class_method()  # by calling class_method

# call instance method
my_class_obj.instance_method()
```

related section: [magic method](#magic-method)

#### class and instance attributes

[documentation](https://docs.python.org/3/tutorial/classes.html?#class-and-instance-variables)

There are two types of attributes:

| attribute type         | accessible from     | change reflect on   |
| ---------------------- | ------------------- | ------------------- |
| **class** attribute    | **all** instances   | **all** instances   |
| **instance** attribute | instance **itself** | instance **itself** |

```python
class TagCloud:
    # class attribute
    tags = []

    def __init__(self, hashes):
        # instance attribute
        self.hashes = hashes


# create instance and assign instance attribute
cloud1 = TagCloud(1)
cloud2 = TagCloud(2)
# assign class attribute
cloud1.tags.append(3)
cloud2.tags.append(4)
# result
print(f"cloud1: tags = {cloud1.tags}, hashes = {cloud1.hashes}")  # cloud1: tags = [3, 4], hashes = 1
print(f"cloud2: tags = {cloud2.tags}, hashes = {cloud2.hashes}")  # cloud2: tags = [3, 4], hashes = 2
```

#### _isinstance_, _issubclass_ functions

> related section: [inheritance](#inheritance)

```python
class InheritedClass:
    pass


class ClassName(InheritedClass):
    pass


class_name = ClassName()

isinstance(class_name, ClassName)  # True
isinstance(class_name, InheritedClass)  # True

issubclass(ClassName, InheritedClass)  # True
```

#### propriety

related section: [magic method](#magic-method)
Propriety is used to set, get, delete an attribute.

It's possible to make a property read only.

```python
# without property
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative.")
        self.__price = value


# set price
product = Product(10)
# get price
product_price = product.get_price()
# reassign price
product.set_price(20)
```

```python
# with property
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative.")
        self.__price = value


# set price
product = Product(10)
# get price
product_price = product.price
# reassign price
product.price = 20
```

```python
# read-only property
class Product:
    def __init__(self, price):
        if price < 0:
            raise ValueError("Price can't be negative.")
        self.__price = price

    @property
    def price(self):
        return self.__price


# set price
product = Product(10)
# get price
product_price = product.price
```

#### inheritance

[documentation](https://docs.python.org/3/tutorial/classes.html?#inheritance)

related section: [isinstance and issubclass functions](#_isinstance_-_issubclass_-functions)

```python
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        pass


# Animal: parent, base
# Mammal: child, sub
class Mammal(Animal):
    def walk(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


mammal = Mammal()
mammal.eat()
mammal.walk()
mammal.age

fish = Fish()
fish.swim()
fish.age
```

##### abstract base class

```python
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError
        else:
            self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError
        else:
            self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading resource from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading resource from a network")


class MemoryStream(Stream):
    def read(self):
        print("reading resource from a memory")


memory_stream = MemoryStream()

# TypeError: Can't instantiate abstract class MemoryStream with abstract method read
# --------------------------
# class MemoryStream(Stream):
#     pass
#
# memory_stream = MemoryStream()

# TypeError: Can't instantiate abstract class Stream with abstract method read
# --------------------------
# stream = Stream()
```

###### polymorphism

> polymorphism means "many forms"

```python
from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("text box")


class DropDownList(UIControl):
    def draw(self):
        print("drop down list")


def draw(controls):
    for control in controls:
        control.draw()


text_box = TextBox()
drop_down_list = DropDownList()

draw([text_box, drop_down_list])

# output:
# text box
# drop down list
```

> Duck Typing: the type or the class of an object is less important than the method it defines.  
Using Duck Typing, we only check for the **presence** of a given method or attribute.  
The name Duck Typing comes from the phrase:  
“If it looks like a duck and quacks like a duck, it’s a duck”

##### multilevel inheritance

multilevel inheritance can be problematic

```python
class Animal:
    def eat(self):
        pass


class Bird(Animal):
    def fly(self):
        pass


class Chicken(Bird):
    pass


chicken = Chicken()
chicken.fly()  # a chicken can't fly!
```

##### multiple inheritance

[documentation](https://docs.python.org/3/tutorial/classes.html?#multiple-inheritance)

multiple inheritance can be problematic

```python
# a bad example
class Employee:
    def greet(self):
        print("Employee great")


class Person:
    def greet(self):
        print("Person great")


# python interrupter look for the called method in the class itself.
# If not found, look for it in the next inherited class(Employee in this case)
# If not found, look for it in the next one and so on
class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()  # Employee great


# a good example
class Flayer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flayer, Swimmer):
    pass
```

##### Extending Built-in Types

```python
# extend str
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())  # output: PythonPython
```

```python
# extend list
class TrackableList(list):
    def append(self, __object):
        print("Append called")
        super().append(__object)


trackable_list = TrackableList()
trackable_list.append("a")

# output:
# Append called
```

#### method overriding

> `super` function is used to access a parent class

```python
class Animal:
    def __init__(self):
        self.age = 1


class Mammal(Animal):
    def __init__(self):
        # overridden method won't be executed unless we explicitly call it
        super(Animal).__init__()
        self.weight = 100


mammal = Mammal()
mammal.age
mammal.weight
```

#### decorator

A decorator a way to extend the behavior of a method or a function.

```python
# function
@decorator
def function():
    pass
```

```python
# method
class MyClass:
    @classmethod
    def class_method(cls):
        pass
    @staticmethod
    def get_value(self):
        pass
```

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    

point = Point(1)
```
#### magic method

related section: [inheritance](#inheritance)

[documentation](https://rszalski.github.io/magicmethods/)

magic methods get called by python automatically depending on how we use the class. You can change there behavior by **
overriding** them.

> magic methods are inherited from a base class for all classes called "object"

```python
class Point:
    tags: dict = {"a": 1}

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines behavior for the equality operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Defines behavior for greater than operator
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __getitem__(self, item):
        return self.tags[item]

    def __setitem__(self, key, value):
        self.tags[key] = value

    # destructor
    def __del__(self):
        pass


point = Point(10, 20)  # __init__
other = Point(1, 2)
print(point == other)  # __eq__
print(point > other)  # __gt__
print(point < other)  # this magic method got figured out by itself
print(point["a"])  # __getitem__
point["b"] = 2  # __setitem__
```

```python
class Cloud:

    def __init__(self):
        self.tags: dict = {}

    def add(self, key):
        self.tags[key.lower()] = self.tags.get(key.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag, 0)

    # def __setitem__(self, tag, count):
    #     self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

    def __len__(self):
        return len(self.tags)


cloud = Cloud()  # __init__

cloud.add("Python")
cloud.add("python")
cloud.add("python")

print(cloud["python"])  # __getitem__
# Cloud["b"] = 10  # __setitem__
print(len(cloud))  # __len__
for tag in cloud:  # __iter__
    print(tag)
```

## doc string

```python
# module docstring
"""This module provides a function to convert a PDF to text."""


class Convertor:
    # class docstring
    """this class is a simple converter to convert a PDF into a text"""
    
    def convert(self, path: str) -> str:
        # function docstring
        """
        convert the given PDF into text.

        this function takes the given path to read the PDF,
        then parse the PDF to extract the text.

        :param
        path: path to PDF file.

        :return:
        str: extracted text from the PDF.
        """
        return "pdf2text"
```

## pydoc

open a module documentation in terminal:

- `pydoc module_name` (windows)
- `pydoc3 module_name` (mac / linux)

export a module documentation into an html file:

- `pydoc -w module_name` (windows)
- `pydoc3 -w module_name` (mac / linux)

explore documentations in a local server:

- `pydoc -p port_number` (windows)
- `pydoc3 -p port_number` (mac / linux)

## module

[documentation](https://docs.python.org/3/tutorial/modules.html)

- package: a directory that contains:
  - modules: a python file `.py`
  - `__init__.py` file, which gets executed once the corresponding module/package get loaded/compiled
  - sub-package: a package inside a package
    - modules
    - `__init__.py` file
    - and so on...

---

by convention, modules names are:

- lower case
- word separated by `_`

> modules name **shouldn't** include space

example: "my_module.py"

### import module

> import statement look for module name in a list of directories found in `sys.path` one after the other until it finds the module

```python
import sys

print(sys.path)
```

#### import syntax

> the codes below are run from an external python file in the same directory as the package

```python
# import multiple objects from a module
from sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# sales.py
# │
# ├── calc_shipping function
# └── calc_tax function
```

```python
# import all objects from a module, bad practice
from sales import *

calc_shipping()
calc_tax()

# sales.py
# │
# ├── calc_shipping function
# └── calc_tax function
```

```python
# import entire module as an object
import sales

sales.calc_tax()
sales.calc_shipping()

# sales.py
# │
# ├── calc_shipping function
# └── calc_tax function
```

---

```python
# "as" expression
import sales as s

s.calc_tax()
s.calc_shipping()

# sales.py
# │
# ├── calc_shipping function
# └── calc_tax function
```

---

module in a package

```python
from ecommerce.shopping.sales import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# └────── calc_tax function
```

```python
from ecommerce.shopping import sales

sales.calc_shipping()
sales.calc_tax()

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# └────── calc_tax function
```

---

module in a sub-package

---

```python
import ecommerce.shopping.sales as s

s.calc_shipping()
s.calc_tax()

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# └────── calc_tax function
```

```python
from ecommerce.shopping.sales import calc_tax, calc_shipping

calc_tax()
calc_shipping()

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# └────── calc_tax function
```

> the codes below are run from sales module

```python
# absolute path(best practice)
from ecommerce.customers.contacts import contact
contact()

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# ├────── calc_tax function
# │
# ├── customers/
# ├──── contacts.py
# └────── contact function
```

```python
# relative path
from ..customers.contacts import contact

contact()

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# ├────── calc_tax function
# │
# ├── customers/
# ├──── contacts.py
# └────── contact function
```

#### dire function

```python
from ecommerce.shopping import sales

print(dir(sales))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'calc_shipping', '']
print(sales.__name__)  # ecommerce.shopping.sales
print(sales.__package__)  # ecommerce.shopping
print(sales.__file__)  # file's path

# ecommerce/
# │
# ├── shopping/
# ├──── sales.py
# ├────── calc_shipping function
# └────── calc_tax function
```

#### module as a script

to make a chunk of module only execute if the module is executed directly(not imported),
you can use `__name__ == '__main__'` condition.

```python
if __name__ == '__main__':
    print("this file has been executed")
else:
    print("this file has been imported")
```

#### compiled module

related section: [python implementations](#implementations)

Python generates a compiled version of the imported module with the extension `pyc` -in case of **cpython** implementation- to
speed up the process. And ensure that the compiled version is up-to-date by comparing the dates of making the two files.

> Notice: file extension may differ depends on implementation used

## package management

[documentation](https://packaging.python.org/tutorials/installing-packages/)

The Python Package Index ([PyPI](https://pypi.org/)) is a repository of software for the Python programming language.

PIP is used to install packages from PyPI using cmd.

### PIP

> Note: mac and linux users write **pip3** instead of **pip**

> packages in PyPI use [Semantic Versioning](https://semver.org/)  
> ![Different components of version numbering](https://media.geeksforgeeks.org/wp-content/uploads/semver.png)
> ![Semantic Versioning](https://media.geeksforgeeks.org/wp-content/uploads/20201021010157/SemanticVersioning.png)

| name                                      | command                                                              |
| ----------------------------------------- | -------------------------------------------------------------------- |
| install latest version of a package       | `pip install package_name`                                           |
| install certain version of a package      | `pip install package_name==2.5.3`                                    |
| install latest minor version of a package | `pip install package_name==2.5.*`, `pip install package_name~=2.5.0` |
| uninstall a package                       | `unistall package_name`                                              |
| list installed packages                   | `pip list`                                                           |

### Environment

virtual environment is an isolated container for python packages.

There are two types of environments:

| type of environment | packages location         | get packages location | create operation                                                                   | activate operation                                                                  | deactivate operation |
| ------------------- | ------------------------- | --------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------- |
| venv                | included in environment   | -                     | `py -m venv env_name`                                                              | `venv/Script/activate.bat` (windows), `source venv/Script/activate.bat` (mac/linux) | `deactivate`         |
| virtualenv          | excluded from environment | `pipenv -venv`        | `pipenv install package_name` (windows), `pipenv3 install package_name`(mac/linux) | `pipenv -shell`                                                                     | `exit`               |

> Note 1: virtualenv use "venv" and PIP under the hood.  
> Note 2: You might need to install virtualenv, by running the command `pip install pipenv` for windows and `pip3 install pipenv` for mac / linux.  
> Note 3: "package_name" in creating pipenv command is optional.  
> Note 4: To create virtualenv from the dependency in "pipfile.lock" instead of "pipfile" run the command `pipenv install --ignore-pipfile`.  

**virtualenv** make a file called "pipfile", which consists of 3 sections:

- source: the **source** of the packages
- packages: list of packages used in **production**
- dev-packages: list of packages used in **development** only
- requires: specify python **version**

"pipfile" content:

```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"

[dev-packages]

[requires]
python_version = "3.9"
```

virtualenv dependency operations:

| operation                          | command                      |
| ---------------------------------- | ---------------------------- |
| list dependencies                  | `pipenv graph`               |
| update outdated packages           | `pipenv update --outdated`   |
| update a specific outdated package | `pipenv update package_name` |

### publish a package in PyPI

[official documentation](https://docs.python.org/3/distributing/index.html)

pre-requirements:

- Create an account in [PyPI](https://pypi.org/).
- install 3 tools globally, by running this command globally `pipenv install setuptools wheel twine`.

Create a package:

```
directory tree

packege/
│
├── packege/
│   ├── __init__.py
│   ├── module.py
│   └── another_module.py
│
├── tests/
│   ├── test.py
│   └── another_test.py
├── data/
│
├── setup.py
├── LICENSE
└── README.md
```

"setup.py" content:

```python
import setuptools
from pathlib import Path

setuptools.setup(
    name="unique_name",
    version="1.2.0",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "resource"])
)
```

"LICENSE" content:

pick a suitable license from [choosealicense](https://choosealicense.com/)

create a source distribution and build distribution:

execute the command `python setup.py sdist bdist_wheel` for windows or `python3 setup.py sdist bdist_wheel` for mac / linux

upload to PyPI by executing the command `twine upload dist/*`
