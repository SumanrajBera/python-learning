# File and Exeception Handling

## Exception Handling
- Exception Handling is the process of responding to runtime errors (unexpected events that happen while the program is running) so that the program doesn't crash abruptly and can maintain a controlled flow.

### How to handle
- `try-except` - This is the most basic way of handling exception.
```py
a = int(input())
b = int(input())

# Even if there is zero division error it will catch it and continue with the flow.
try:
    print(a/b)
except Exception as err:
    print(f"An error occured {err}")

print(a + b)
```
- We have made use of `Exception` which is an universal catcher but we can go specific to handle situations according to them. Example: `ZeroDivisionError` for catching zero division.
- We can also use `else` which executes if `except` doesn't execute and vice versa.
- Next we have `finally` and this executes no matter what
- And lastly there's `raise` for raising a custom exception.
```py
try:
    age = int(input())

    if age < 18:
        raise Exception("You must be 18 or above")
except Exception as err:
    print("Error:",err)
else:
    print("Access Granted")
finally:
    print("Process Completed")
```
*Note*: We can have multiple `except` to handle multiple kinds of errors.

## File Handling
- File handling is the process of handling (performing CRUD operations) files.

### Basic method to refer to a file
- Here we make use of `open("path", "mode")` method and pass the path of which file you want to refer and by default it referes to current directory in which you are working.
```py
# Here I have used r to make it raw string to eliminate the possible trigger of escape sequences
file = open(r"./file_exception_handling/file.txt")
```
- Once you open a file you must close it with `close()`

### Different methods we can use
- read("") - It is used to read the contents of the file
- write("") - It is used to write contents to the file

### Using `with` to close file automatically
- We can `with` to avoid manual closing
```py
with open("filepath") as fs:
    print(fs.read())
```
  
### Different modes of file
- `r` - This is the default which means the file opened can only be read from.
- `a` - This is used for appending to a file and can be used to create one as well
- `w` - This is used overwrite to a file and also creates a file if doesn't exist
- `x` - This is used for creating a file and raises error if it already exists.