# Functions
- Functions are blocks of code that can be called for executing a set of instruction and without functions we may need to write repetitive code for executing the same set of instructions.
```py
# basic syntax
def Greet():
    pass
# to call
Greet()
```

## return statement
- This is used to return some value back wherever it was called. When this runs the function completes execution.

## Parameters and arguments
- `Parameters` - These are variables written during function declaration. *We can have default values which gets assigned if nothing is passed as arguments. Eg. (a, b = 10) - here b has default value of 10*
- `Arguments` - These are values passed when calling the function
**Note**: Always make `defaults` in the last
```py
# a, b are both parameters
def add(a,b):
    return a + b
add(10, 12)
# 10 and 12 are both agruments.
```

## Positional and keyword arguments.
- `positional arguments` - These are normal arguments that we pass. As they get assigned by position.
- `keyword arguments` - This is keyword argument which used to pass based on the value. Like suppose we have order `(a,b, c)` and now we can pass using `(12, c = 10, b = 9)` - Here we a will be 12 where as c is 10 and b is 9 and if we hadn't given the variable names here it would have been in  a is 12, b is 10 and c is 9. Also we have used a mix of args and kwargs so once kwargs is used you can't go back to args.

**Note**: A function returns `None` if we don't return anything