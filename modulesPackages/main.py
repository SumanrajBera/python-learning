# first way: To import via refering

# import modules.math_utils
# print(modules.math_utils.sum(10, 20))
# print(modules.math_utils.sub(10, 20))

# shorter way
from modules import math_utils
print(math_utils.sum(10, 20))
print(math_utils.sub(10, 20))

# second way: To import particular

# from modules.math_utils import sum
# print(sum(10, 20))

# third way: To import all

# from modules.math_utils import *
# print(sum(10, 20))

from my_package import math_utils, string_utils

print(string_utils.length("Hello World"))