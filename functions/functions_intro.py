# A function is a reusable block of code
# defined using the keyword `def`

# syntax:
# def function_name(parameters):
#     code
#     return value


# parameter = variable inside function definition
# argument = value passed when calling the function

def add(a, b):          # a and b are parameters
    return a + b

result = add(3, 5)      # 3 and 5 are arguments


# return vs print
def show_sum(a, b):
    print(a + b)        # prints but returns nothing

def get_sum(a, b):
    return a + b        # returns a value


# default parameters
def greet(name="Guest"):
    return "Hello " + name
