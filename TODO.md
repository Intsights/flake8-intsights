### general
+ No tabs at code, unless in strings.
+ all lines must start with 4-spaces tabs. make sure the number of spaces is a multiplication of 4 spaces.
+ never use inline comments.
+ no trailing spaces.
+ last line is a blank line in a file
+ no blank lines at the top of the file
+ if the same file has 2 same name functions/classes/dict_keys ....
+ no newline after class def
+ except, finally: no blank lines above
+ two blank lines after last import
+ indenteation must be +1 0 -1 from the previous line
+ use only f strings
+ raise must raise an object() not class
+ no mutable as default argument
+ remove set_trace
- vars cant be 1 char long
- functions names must be at least 3 chars.
- check if the file is in utf8 format.
- variables names must not be less than 3 chars.
- not string -> length > 100 -> error
- if comparison -> no more than 2 boolean operators
- no \r in code
- re.compile -> pattern, always r''
- try should be spaced above
- no strings without any assignment :
    ```python
        import test

        """
        some comment
        """
    ```
- test file must start with test_
- dict key name must be next to the bracket - dict['key'] and not dict[ 'key' ]
* write a formatter



### dict/list-comprehension
```python
[
    entry
    for entry in arr
    if condition
    .....
]
```

### std functions calls
- comma ',' at the end of each line

```python
range(
    0,
    10,
    2,
)
```

### non std functions calls
- comma ',' at the end of each line
- always call by parameters names

```python
requests.get(
    url='http:/....',
    headers={
        'key': 'value',
    },
)
```

### use more and better comprehensions
https://pypi.python.org/pypi/flake8-comprehensions/1.2.1

### no leftovers!
- check there are no 'print' calls in the code

### regex
- regex patterns must always be escaped string -> r''
