# 10. Real-World Use Case: Dynamic Function Application
        # Write a function dynamic_function that:
        # Takes a list of numbers and a string indicating the operation ("add",
        # "subtract", "multiply", "divide").
        # Dynamically applies the operation using lambda functions.
        # Returns the result of applying the operation to all numbers in the list.
        # Test it with various lists and operations

from functools import reduce

# function that takes list of numbers and string of operation
def dynamic_function(numbers, operation):

    # Indicating all the operation
    if operation == "add":
        func = lambda x, y: x + y
    elif operation == "subtract":
        func = lambda x, y: x - y
    elif operation == "multiply":
        func = lambda x, y: x * y
    elif operation == "divide":
        func = lambda x, y: x / y
    else:
        raise ValueError("Invalid Operation")

    return reduce(func, numbers)

# Function call
print("Addition of numbers in list: ", dynamic_function([1, 2, 3, 4], "add"))
print("Subtraction of numbers in list: ", dynamic_function([5, 6, 7, 8], "subtract"))
print("Multiplication of numbers in list: ", dynamic_function([1, 2, 4, 6], "multiply"))
print("Division of numbers in list: ", dynamic_function([1, 3, 5, 7], "divide"))