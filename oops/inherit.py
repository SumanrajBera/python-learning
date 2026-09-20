class Animal:
    def __init__(self,name, legs):
        self.name = name
        self.legs = legs

    def printInfo(self):
        print(f"My name is {self.name} and I have {self.legs} legs")

class Human(Animal):
    def __init__(self, name, legs):
        super().__init__(name, legs)

hum = Human("Samuel", 2)
hum.printInfo()

class ParentA:
    def greet(self):
        print("Hello from A")
        super().greet() # calls parent B which is next in chain

class ParentB:
    def greet(self):
        print("Hello from B")

class Child(ParentA, ParentB):
    def test_super(self):
        # super() looks at the MRO chain: Child -> ParentA -> ParentB -> object
        super().greet() 

obj = Child()
obj.test_super()  # Outputs: "Hello from A"