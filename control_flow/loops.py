# Loops in Python
# A loop is used to repeat a block of code multiple times.

# A "for" loop is usually used when we know how many times we want to repeat something.
# It often works with ranges or collections like lists.

# A "while" loop runs as long as a condition remains True.
# It is useful when we don’t know in advance how many times the loop should run.


# Example 1: for loop with range
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# Example 2: looping through a list
fruits = ["apple", "banana", "orange"]

print("\nFruits list:")
for fruit in fruits:
    print(fruit)


# Example 3: while loop
count = 1
print("\nWhile loop example:")
while count <= 5:
    print(count)
    count += 1


# Example 4: using break
# 'break' stops the loop immediately
print("\nBreak example:")
for number in range(1, 10):
    if number == 5:
        break
    print(number)


# Example 5: using continue
# 'continue' skips the current iteration and moves to the next one
print("\nContinue example:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
