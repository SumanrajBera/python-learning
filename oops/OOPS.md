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

## In-depth attribute and method

### Attrubute
- `Instance attribute`: An attribute that is created using the `self` keyword. Eg. self.zip or self.brand
- `Class attribute`: An attribute that is created without the self keyword.

### Methods
- `Instance method`: A method created using self keyword as first parameter.
- `Class method`: A method created with `@classmethod` as decorator and do not rely on instance specific data. Here we use `cls` to target the class.
```py
class Factory:
  # class attribute
  age = 20

  # cls targets the class
  @classmethod
  def myMethod(cls):
    print(cls.age)
```
- `Static method`: It is created using `@staticmethod` and we don't pass anything.

## Inheritance
- Inheritance is a mechanism by which a `child` class can use the properties and methods of its `parent` class.
```py
class Animal:
    def __init__(self,name, legs):
        self.name = name
        self.legs = legs

    def printInfo(self):
        print(f"My name is {self.name} and I have {self.legs} legs")

class Human(Animal):
    def __init__(self, name, legs, canTalk):
        super().__init__(name, legs)
        self.canTalk = canTalk
```
- Here we call the super() method which is used to initialise the init of parent.

### Types of inheritance
- Single level: In this one class inherits from another class
- Multilevel : In this a class inherits from another class that also inherits from another class.
- Multiple inheritance: Here we inherit from two or more classes. Here when we call the method or attribute which exists in two or more classes it will call the first in chain that contains it and if we call it in the next one using super it will call the next in chain.
```py
class ParentA:
    def greet(self):
        print("Hello from A")

class ParentB:
    def greet(self):
        print("Hello from B")

class Child(ParentA, ParentB):
    def test_super(self):
        # super() looks at the MRO chain: Child -> ParentA -> ParentB -> object
        super().greet() 

obj = Child()
obj.test_super()  # Outputs: "Hello from A"
``` 
- Hierrarchical: Its where multiple class inherit from the same class.