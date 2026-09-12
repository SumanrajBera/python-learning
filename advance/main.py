li = [10,20,30]

# Add 10 to all in list
resli = []
for i in li:
    resli.append(i + 10)
print(resli)

# comprehension
resli2 = [i + 10 for i in li ]
print(resli2)


# Creating a diction where each number from li is squared
dt1 = {}
for i in li:
    dt1[i] = i**2
print(dt1)

# Comprehension
dt2 = {i: i**2 for i in li}
print(dt2)

def my_addDecorator(func):
    def wrapper():
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Addition of two numbers:")
        func(a,b)
        print("Bye Bye")
    return wrapper

@my_addDecorator
def add(a,b):
    print(a+b)

add()