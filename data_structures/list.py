# Lists in Python
# A list is a collection that can store multiple values in one variable

# creating a list
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]

# accessing elements (index starts from 0)
print(numbers[0])        # 1
print(fruits[1])         # banana

# changing elements
numbers[0] = 10
print(numbers)           # [10, 2, 3, 4, 5]

# length of a list
print(len(fruits))       # 3

# adding elements
fruits.append("mango")
print(fruits)            # ['apple', 'banana', 'orange', 'mango']

# removing elements
fruits.pop()
print(fruits)            # ['apple', 'banana', 'orange']

fruits.remove("banana")
print(fruits)            # ['apple', 'orange']

# checking if an item exists in a list
print("apple" in fruits) # True
print("pear" in fruits)  # False

# looping through a list
for fruit in fruits:
    print(fruit)         # apple, orange

# using range to create a list
numbers_range = list(range(1, 6))
print(numbers_range)     # [1, 2, 3, 4, 5]

# list slicing
print(numbers_range[1:4])  # [2, 3, 4]
print(numbers_range[:3])   # [1, 2, 3]
print(numbers_range[2:])   # [3, 4, 5]

# sorting a list
nums = [5, 2, 9, 1]
nums.sort()
print(nums)               # [1, 2, 5, 9]

# reversing a list
nums.reverse()
print(nums)               # [9, 5, 2, 1]

# list with mixed data types
mixed = [1, "hello", 3.5, True]
print(mixed)              # [1, 'hello', 3.5, True]

# nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0])          # [1, 2]
print(matrix[1][0])       # 3
