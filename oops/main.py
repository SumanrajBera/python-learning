"""
Create a student registration system
Ask for
1) Name
2) Age
3) Gender
4) Number
5) Blood Group
"""

class Student:
    def __init__(self, name, gender, age, number, blood):
        self.name = name
        self.gender = gender
        self.age = age
        self.number = number
        self.blood = blood

    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Number: {self.number}")
        print(f"Blood Group: {self.blood}")
        print()

registeredStudent = [
    Student("Aarav Sharma", "Male", 20, "9876543210", "B+"),
    Student("Ananya Patel", "Female", 19, "9123456780", "O+"),
    Student("Rohan Mehta", "Male", 21, "9988776655", "A+"),
    Student("Priya Singh", "Female", 20, "9090909090", "AB+"),
    Student("Kabir Shah", "Male", 22, "9765432109", "O-"),
    Student("Isha Verma", "Female", 19, "9345678901", "B-"),
    Student("Aditya Joshi", "Male", 20, "9898989898", "A-"),
    Student("Sneha Rao", "Female", 21, "9234567890", "AB-"),
]

registeredStudent[0].printInfo()
registeredStudent[3].printInfo()
registeredStudent[1].printInfo()
registeredStudent[4].printInfo()