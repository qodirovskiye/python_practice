# Strings in Python
# A string is a sequence of characters

text = "Hello World"

# accessing characters (indexing)
print(text[0])            # H
print(text[-1])           # d

# length of a string
print(len(text))          # 11

# string slicing
print(text[0:5])          # Hello
print(text[6:])           # World
print(text[:5])           # Hello

# changing case
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.title())       # Hello World

# removing spaces
text2 = "  hello  "
print(text2.strip())      # hello
print(text2.lstrip())     # hello  
print(text2.rstrip())     #   hello

# replacing text
print(text.replace("World", "Python"))  # Hello Python

# checking content
print(text.startswith("Hello"))         # True
print(text.endswith("World"))           # True
print(text.isalpha())                   # False (space exists)
print("Hello".isalpha())                # True
print("123".isdigit())                 # True

# splitting strings
sentence = "Python is easy to learn"
words = sentence.split(" ")
print(words)                            # ['Python', 'is', 'easy', 'to', 'learn']

# joining strings
joined = "-".join(words)
print(joined)                           # Python-is-easy-to-learn

# finding substrings
print(sentence.find("easy"))           # 10
print(sentence.find("hard"))           # -1

# counting occurrences
print(sentence.count("o"))             # 1

# string formatting
name = "Alex"
age = 20
print("My name is " + name)            # My name is Alex
print(f"My name is {name} and I am {age}")  # My name is Alex and I am 20

# escape characters
print("Line1\nLine2")                  # Line1 (new line) Line2
print("He said: \"Hello\"")            # He said: "Hello"
