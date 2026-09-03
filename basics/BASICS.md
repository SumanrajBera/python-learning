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

### Strings (In depth)
- Strings has both positive and negative indexing
```py
str = "hello"
print(str[0]) # Positive indexing
print(str[-1]) # Negative indexing
```
- **String slicing**: We can slice our strings using `a[start: stop : steps]`
  - start: From where to start *(default is 0)*
  - stop: Where to stop *(stop_value - 1)*
  - steps *(optional)*: In how many steps should we move and if we set it to -1 its reversed (The sliced part)

*Note*: Strings are immutable by nature

## Print statement ways
- How to combine string with variables in print: We can use `,`
```py
age = 20
print("Age is", age) # Space is added automatically
```
- TO format string we can use `print(f"")`
```py
age = 20
print(f"Age is {age}") # This is a formatted string
```

### Escape sequences
- `\n` - For next line
- `\t` - For tab
- `\b` - For backspace

### Raw string
- Its similar to format string but we use `r` and we cannot use escape sequences in this.
```py
print(r"This is a raw\n string")
```

### Useful functions
- lower() - `str_var.lower()` can be used for lowercasing
- upper() - `str_var.upper()` can be used for uppercasing
- count("string") - Can be use for counting particular instances of the mentioned string in the string.
- find("string") - Can be used to find the index where the string mentioned starts *(First instance)*
- len(string) - Can be used to find the length of the string
- isdigit() - Can be used to check if the string has only numerics return `True` or `False`

*Note*: We can use `+` operator to join strings which is called concatenation.

## Type conversion
- We use this to convert one data type to another. Following are ways to convert
  - int() 
  - float()
  - str()
  - bool()
  - Truthy values - Everything is truthy except for 0, 0.0, False, "", [], (), {}
  - Falsy values - 0, 0.0, False, "", [], (), {}

## How to take input from user?
- To take input we can make use of built-in `input` function  
```py
name = input("What's your name?") # Always takes in string format so we need type conversion here
print(name)
```