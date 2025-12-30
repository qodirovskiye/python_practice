# Topic: Classes, objects, attributes, __init__, self

# A class is a blueprint for creating objects
class Student:
    # __init__ is the constructor (runs when an object is created)
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute

    # method inside a class
    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old.")


# creating objects (instances) of the class
student1 = Student("Ali", 20)
student2 = Student("Sara", 22)

# accessing attributes
print(student1.name)   # Ali
print(student2.age)    # 22

# calling a method
student1.introduce()   # My name is Ali and I am 20 years old.
student2.introduce()   # My name is Sara and I am 22 years old


# class with default values
class Car:
    def __init__(self, brand="Unknown", year=0):
        self.brand = brand
        self.year = year

    def info(self):
        print("Brand:", self.brand, "| Year:", self.year)


car1 = Car()
car2 = Car("Toyota", 2022)

car1.info()   # Brand: Unknown | Year: 0
car2.info()   # Brand: Toyota | Year: 2022
