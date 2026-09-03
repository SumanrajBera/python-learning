print("Hello")

# String indexing
str1 = "hello"
print(str1[0]) # Positive indexing
print(str1[-1]) # Negative indexing

# String slicing
sliceStr = "hello world"
print(sliceStr[0: 9: 2])

# Task
taskStr = "hello I am Data Scientist"
# Extract hello
print(taskStr[:5])
# Extract Data
print(taskStr[11:15])
# Extract Scientist
print(taskStr[-9:])

# Formatted string
age = 20
print(f"Age is {age}") # This is a formatted string

# Raw string
print(r"This is a raw\n string")

str2 = "hell hell hell"
print(str2.upper())
print(str2.lower())
print(str2.count("hell"))
print(str2.find("ell"))