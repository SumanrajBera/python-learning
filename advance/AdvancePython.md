# Advanced Things in Python

## Lambda Expression
- It is one line expression of function and is used for simpler functions.
```py
square = lambda x : print(x**2)
square(10) # Will print 10's square
```

## Map function
- This is used to apply some function over all the elements of the list. It returns an iterator
- Syntax: `map(fn, list)`

## Filter Function
- This is used to filter out elements based on the condition. It returns an iterator
- Synatx: `filter(fn, list)`

## Zip function
- This is used to combine multiple iterables into pairs of elements
```py
li1 = ["Ash","Hase"]
li2 = [20, 40]
newLi = list(zip(li1, l2)) # Will create [("Ash", 20), ("Hase", 40)]
```

## List, Dictionary and Set comprehension
- List
```py
li = [10,20,30]

# Add 10 to all in list
resli = []
for i in li:
    resli.append(i + 10)
print(resli)

# comprehension
resli2 = [i + 10 for i in li ]
print(resli2)
```
- Set comprehension is done the same way we do list but with curly braces
- Dictionary
```py
li = [10,20,30]

# Creating a diction where each number from li is squared
dt1 = {}
for i in li:
    dt1[i] = i**2
print(dt1)

# Comprehension
dt2 = {i: i**2 for i in li}
print(dt2)
```

## Generators
- Generators are special kind of iterators that don't store the sequence in memory rather generate one at a time.
```py
def generator_func():
    for i in range(5):
        yeild 1
print(next(generator_func())) # will print 0
print(next(generator_func())) # will print 1
print(list(generator_func())) # will print all the remaining in the list
```
- Its used for lazy evaluation like when we don't require it to run fully just when called to generate the next segment.

## Decorators
- This is like icing on the cake just to make sure that we add some extra before or after
```py
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
```