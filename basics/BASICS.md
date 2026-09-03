# Basics of Python
- This directory consists of all the basics of python for beginner.

## Comments 
- `#`: This is a single line comment
- `""" """`: This is used for multi-line comment
```py
# This is a single-line comment
"""
This is a multi-line comment
"""
```

## Variables
- Variables are used for storing some value.
- It can be initialised when we assign a value to it in python.
```py
a = 10
b = 12
```
- There are only 3 naming conventions used in python:
  - Camel case: helloWorld
  - Pascal case: HelloWorld
  - Snake case: hello_world 

### Conditions for variable creation
- Cannot start a variable with number
- Cannot use space in variable
- Cannot use special character with the exception of `_`

## Data types
- There are 3 major types in python
  - **Number**: This consists of int , float (fractions and decimals) and complex number
  - **String**: We can store between `""` or `''`
  - **Boolean**: True and False 
- To check the type of a variable we can `type` keyword 
```py
a = 10
print(type(a))
```