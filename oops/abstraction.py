from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    # If we don't implement sound(), it will throw an error
    # when we try to create a Dog object.
    def sound(self):
        print("I bark.")
