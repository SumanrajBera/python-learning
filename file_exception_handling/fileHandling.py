# It refers the current working directory then we can refer to wherever our file is

file = open(r"./file_exception_handling/file.txt")

# To read from the file
print(file.read())

file.close()