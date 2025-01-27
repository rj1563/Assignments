# 8. Functional Programming: Custom Aggregation
        # Write a function custom_aggregate that:
        # Takes a list of numbers and a function as arguments.
        # Applies the function to all numbers and returns their aggregated result (e.g., sum, product, etc.).

        # Test it with:
        # A lambda function that calculates the sum.
        # A lambda function that calculates the product.

from functools import reduce

# a function that takes a list of numbers and a function as arguments and applies the function to all numbers
def custom_aggregate(lst, func):
    return  reduce(func, lst)      # Applies the function to all numbers and returns their aggregated result 

# A lambda function that calculates the sum.
print("Function call to calculate the sum: ", custom_aggregate([1,2,3,4,5], lambda x, y: x+y))

# A lambda function that calculates the product.
print("Function call to calculate the product: ", custom_aggregate([1,2,3,4,5], lambda x, y: x*y))