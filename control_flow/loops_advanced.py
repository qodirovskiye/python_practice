# Advanced loop control

# break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)                      #result: 1, 2, 3, 4

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)                       #result: 1, 2, 4, 5

# pass example
for i in range(3):
    pass  # placeholder, does nothing

# nested loops
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)              #result: (1,1), (1,2), (2,1), (2,2), (3,1), (3,2)

# ternary condition
age = 18
status = "adult" if age >= 18 else "minor"
print(status)                    #result: adult 
