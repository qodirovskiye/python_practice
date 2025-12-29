# Tuples in Python
# A tuple is an ordered collection that is immutable (cannot be changed)

# creating a tuple
numbers = (1, 2, 3, 4)

# accessing elements
print(numbers[0])        # 1
print(numbers[2])        # 3

# length of a tuple
print(len(numbers))      # 4

# tuples can store different data types
mixed = (1, "hello", 3.5, True)
print(mixed)             # (1, 'hello', 3.5, True)

# tuples are immutable (cannot be modified)
# numbers[0] = 10   # ERROR: tuples do not support item assignment

# looping through a tuple
for x in numbers:
    print(x)             # 1 2 3 4

# tuple slicing
print(numbers[1:3])      # (2, 3)

# checking if an element exists
print(2 in numbers)      # True
print(10 in numbers)     # False

# tuple unpacking
a, b, c, d = numbers
print(a)                 # 1
print(b)                 # 2
print(c)                 # 3
print(d)                 # 4

# swapping values using tuples
x = 5
y = 10
x, y = y, x
print(x, y)              # 10 5

# tuple with one element (comma is required)
single = (5,)
print(single)            # (5,)
print(type(single))      # <class 'tuple'>

# converting between list and tuple
lst = list(numbers)
print(lst)               # [1, 2, 3, 4]

tup = tuple(lst)
print(tup)               # (1, 2, 3, 4)
