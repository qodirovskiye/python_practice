# Type conversion in Python

# input() always returns a string
age = input("Enter your age: ")

# convert string to integer
age_int = int(age)

print("Your age is:", age_int)
print("Next year you will be:", age_int + 1)

# converting between different data types
number = 10
number_str = str(number)   #number_str = "10"  (useful for concatination (str + str))

print("Number as string:", number_str)
print("Type of number:", type(number))
print("Type of number_str:", type(number_str))

# converting float to int
price = 19.99
price_int = int(price)      #price_int = 19

print("Original price:", price)
print("Converted to int:", price_int)
