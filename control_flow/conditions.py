# Conditional flow in Python               ----> if, elif and else 

# Example 1: simple if
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")


# Example 2: if / else
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Example 3: if / elif / else
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")


# Example 4: logical operators
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":    # "and" → both conditions must be True   # "or"  → at least one condition must be True
    print("Access granted")
else:
    print("Access denied")
