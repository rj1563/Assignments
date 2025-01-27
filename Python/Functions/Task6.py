# 6. Decorators
        # Write a decorator execution_time to calculate and display the time taken by a function to execute.
        # Use the decorator on a function that calculates the factorial of a large number (e.g., 1000).

from time import time

# Decorator function to calculate and display the time taken by a function to execute
def execution_time(func):

    def wrapper(*args,**kwargs):
        before_time = time()      #before the func time
        res=func(*args,*kwargs)   #execute function
        after_time = time()       #after the func runs
        print(f"Time of execution {after_time-before_time}")  #give time taken by func
        return res
    return wrapper

# Using the decorator on a function that calculates the factorial of a large number
@execution_time
def factorial(n):
    fact = 1
    for i in range(1, n + 1): 
        fact *= i  # Calculating the factorial for given range and storing result back to fact
    return fact

# Function call
print("Factorial of 5: ", factorial(1000))