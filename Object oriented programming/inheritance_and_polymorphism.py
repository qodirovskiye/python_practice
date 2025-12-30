# Topics: Inheritance + Polymorphism (method overriding)

# -----------------------------
# 3. Inheritance
# -----------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am a person.")


# Student inherits from Person
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)   # call parent constructor
        self.student_id = student_id

    def show_id(self):
        print("Student ID:", self.student_id)


s = Student("Ali", 101)
s.speak()          # inherited method
s.show_id()        # own method


# -----------------------------
# 4. Polymorphism (method overriding)
# -----------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Animal(), Dog(), Cat()]

for a in animals:
    a.sound()
    # Output:
    # Animal makes a sound
    # Dog barks
    # Cat meows
