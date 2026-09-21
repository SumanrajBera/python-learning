# Modules and Packages 
- `Module` - A file containing Python code. It allows reuse and organisation
- `Package` - A package is a directory of modules which has an `__init__.py` file for enabling hierarchy

## Creating and Using modules
- To `create` a module we just need to create a file with `.py` extension.
- Ways to import
```py
# first way: To import via refering
import modules.math_utils
print(modules.math_utils.sum(10, 20))

# shorter way for first
from modules import math_utils
print(math_utils.sum(10, 20))
print(math_utils.sub(10, 20))

# second way: To import particular
from modules.math_utils import sum
print(sum(10, 20))

# third way: To import all
from modules.math_utils import *
print(sum(10, 20))
```