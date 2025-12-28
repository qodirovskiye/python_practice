# Variable scope in Python
# Scope defines where a variable can be accessed

# -----------------------------------
# Local vs Global variables
# -----------------------------------

x = 10  # global variable

def show_local():
    x = 5  # local variable (exists only inside this function)
    print("Inside function:", x)

show_local()
print("Outside function:", x)  # still 10


# -----------------------------------
# Changing a variable inside a function does NOT affect outside
# unless returned or declared global
# -----------------------------------

def change_value():
    y = 20
    y = y + 5
    print("Inside function:", y)

change_value()
# print(y)  # ERROR: y is not defined outside the function


# -----------------------------------
# Using return to send a value back
# -----------------------------------

def add_one(n):
    return n + 1

result = add_one(10)
print("Returned value:", result)      #Returned value: 11


# -----------------------------------
# Using global keyword
# -----------------------------------

count = 0

def increase():
    global count
    count += 1

increase()
increase()
print("Global count:", count)             #Global count: 2


# -----------------------------------
# Scope inside loops
# -----------------------------------

for i in range(3):
    temp = i * 2

print("Loop variable i still exists:", i)
print("Temp also exists:", temp)


# -----------------------------------
# Function parameter scope
# -----------------------------------

def square(x):
    return x * x

value = 4
print("Square:", square(value))             #return: Square: 16


# -----------------------------------
# Shadowing variable names
# -----------------------------------

name = "Alice"

def change_name():
    name = "Bob"   # shadows the global variable
    print("Inside:", name)

change_name()
print("Outside:", name)            # Inside: Bob, Outside: Alice

