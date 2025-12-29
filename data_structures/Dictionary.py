# Dictionaries in Python
# A dictionary stores data in key : value pairs

student = {
    "name": "Alex",
    "age": 20,
    "major": "Computer Science"
}

# accessing values
print(student["name"])           # Alex
print(student.get("age"))        # 20

# adding a new key-value pair
student["year"] = 2
print(student)                   # {'name': 'Alex', 'age': 20, 'major': 'Computer Science', 'year': 2}

# updating values
student["age"] = 21
print(student["age"])            # 21

# removing items
student.pop("major")
print(student)                   # {'name': 'Alex', 'age': 21, 'year': 2}

# removing last inserted item
student.popitem()
print(student)                   # {'name': 'Alex', 'age': 21}

# getting all keys
print(student.keys())            # dict_keys(['name', 'age'])

# getting all values
print(student.values())          # dict_values(['Alex', 21])

# getting all key-value pairs
print(student.items())           # dict_items([('name', 'Alex'), ('age', 21)])

# checking if key exists
print("name" in student)         # True
print("grade" in student)        # False

# looping through dictionary keys
for key in student:
    print(key)                   # name, age

# looping through values
for value in student.values():
    print(value)                 # Alex, 21

# looping through key-value pairs
for key, value in student.items():
    print(key, value)            # name Alex / age 21

# dictionary with mixed value types
info = {
    "id": 101,
    "scores": [90, 85, 88],
    "active": True
}

print(info["scores"])            # [90, 85, 88]

# nested dictionary
users = {
    "user1": {"name": "Ali", "age": 19},
    "user2": {"name": "Sara", "age": 22}
}

print(users["user1"]["name"])    # Ali

# clear dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)                      # {}


#------------Bonus part-------------------
# if the key exists → take its value
# if not → start from 0, then add 1

votes = ["A", "B", "A", "C", "B", "A"]

count = {}

for v in votes:
    count[v] = count.get(v, 0) + 1

print(count)   # {'A': 3, 'B': 2, 'C': 1}

