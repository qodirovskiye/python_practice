# Functions in Python
# A function is a reusable block of code that performs a specific task.

# -------------------------------
# Basic function definition
def greet():
    print("Hello! Welcome to Python.")

greet()


# -------------------------------
# Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Alice")
greet_user("Bob")


# -------------------------------
# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


# -------------------------------
# Function with default parameter
def greet_with_default(name="Guest"):
    print("Hello,", name)

greet_with_default()
greet_with_default("John")


# -------------------------------
# Function that calculates area
def rectangle_area(length, width):
    return length * width

area = rectangle_area(4, 6)
print("Area:", area)


# -------------------------------
# Difference between print and return
def multiply(a, b):
    print("Multiplying numbers...")
    return a * b

value = multiply(3, 4)
print("Result:", value)

# Example of a common mistake (missing return)
def multiply_wrong(a, b):
    print(a * b)   # prints the result but does NOT return it

value = multiply_wrong(3, 4)
print(value)  # None, because the function did not return anything
