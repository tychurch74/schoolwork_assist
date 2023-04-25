"""
Lambda functions are small, anonymous functions defined using the lambda keyword.
They are anonymous because they don't have a name.
They can have multiple arguments but only one expression, which is evaluated and returned.
They are typically used as arguments to higher-order functions (functions that take in other functions as arguments).
Or when you just want to look cool...
"""

# Define a lambda function that takes one argument and returns its square.
# Use another lambda function with the map function to square each number in a list.

# Initialize the first lambda function
square = lambda x: x ** 2

# Call the lambda function with an argument of 5 and print the result
print(square(5))  # Output: 25

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map function with the lambda function to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the squared numbers list
print(squared_numbers)
