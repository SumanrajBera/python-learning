# Object Oriented Programming
- There are three types of programming paradigms:
  - Imperative: where we use variable based programming which are straight written in .py file
  - Functional: Where we make use of functions 
  - Object-oriented: In this programming we make of class and objects.

## Class
- A class is a `blueprint` which can be used to create multiple objects.
- To create a class we make use of `class` keyword.
```py
class Class_Name:
  a = 12 # this attribute will be shared by all instances/objects made from this class
  def hello(): # instance method
    print("How are you")

print(Class_Name.a)
Class_Name.hello()
```
- Class gets initialised only once at very start.
- Industry standard is to make sure class name starts with Capital letters.

## Objects
- We make use of class to make objects.
- We need to use atleast one parameter in methods inside class as when we call methods using the object that object is passed as an argument
```py 
class Class_Name:
  a = 12 
  def hello(): 
    print("How are you")

obj = Class_Name()
print(obj.a)
```

## Constructors
- Constructor is a method that runs automatically when we call a class. And it will target the location of an object.
```py
class NewClass:
  def __init__(self, material, zip):
    print("This runs when we call a class")
    self.material = material
    self.zip = zip
  
  # instance method
  def printMaterial(self):
    print(f"Material: {self.material}\nZips: {self.zip}")

obj = NewClass("leather", 4)
obj2 = NewClass("cotton", 2)
# Due to self every object refers to its assigned material
print(obj.material)
print(obj2.material)
```
- `self` here targets the location of the object.

*Note*: OOPs is majorly used in management system.
