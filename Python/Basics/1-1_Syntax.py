# Single line comments start with a hash symbol
"""
Multi-line comments 
start and end with
three quotes
"""

# Python is a dynamically typed language, so we don't need to specify the type of variable
# For example, we can assign an integer value to a variable, and later assign a string to the same variable:
x = 5
print(x)
x = "Hello"
print(x)


# Python is a strongly typed language, so we can't perform operations on variables of different types
# For example, we can't add an integer and a string (remove the comment below to see the error):
# print(x + 5)


# Python uses indentation (tab or 4 spaces) to denote blocks of code
# For example, the following code is indented to denote that it is part of the if statement:
if x == 5:
    print("x is 5")
else:
    print("x is not 5")


# To create a function in Python, we use the def keyword
# The function below takes in a string and returns the length of the string
def get_length(string):
    return len(string)


# To call a function, we simply use the function name followed by parentheses
print(get_length("Hello"))


# A typical convention in Python is to use snake_case for variable and function names, and PascalCase for class names
# For example (note the 'pass' keyword is used to denote an empty block):
my_variable = 5

def my_function():
    pass

class MyClass:
    pass


# Another convention is the if __name__ == "__main__": block to denote the entry point of the program
# For example:
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()


# Python is a high-level language, so we don't need to worry about low-level details like memory management
# Of course, this means that Python is slower than low-level languages like C


# Python is an interpreted language, so we don't need to compile the code
# Instead, the code is interpreted and executed line-by-line
