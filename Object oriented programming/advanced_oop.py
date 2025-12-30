# Topics: super() + dunder methods + polymorphism + isinstance()

# -----------------------------
# super() + method overriding
# -----------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Person(name={self.name})"

    def __str__(self):
        return self.info()


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)          # calls Person.__init__
        self.student_id = student_id

    def info(self):
        base = super().info()           # calls Person.info
        return f"{base}, Student(id={self.student_id})"


s = Student("Ali", 101)
print(s.info())   # Person(name=Ali), Student(id=101)
print(s)          # Person(name=Ali), Student(id=101)


# -----------------------------
# Dunder methods: __eq__ (custom equality)
# -----------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)

print(p1)         # Point(1, 2)
print(p1 == p2)   # True
print(p1 == p3)   # False
print(p1 == 5)    # False


# -----------------------------
# Polymorphism (dynamic binding)
# Same method name, different behavior depending on object type
# -----------------------------

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

animals = [Animal(), Dog(), Cat()]

for a in animals:
    print(a.speak())   # ..., woof, meow


# -----------------------------
# isinstance() checks object type
# -----------------------------

print(isinstance(s, Student))  # True
print(isinstance(s, Person))   # True
print(isinstance(s, Point))    # False
