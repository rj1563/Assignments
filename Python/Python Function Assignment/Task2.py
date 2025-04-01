# 2. Higher-Order Function
        # Write a function apply_discount that:
        # Takes two arguments: a price and a discount_function.
        # Applies the discount_function to the price and returns the discounted
        # value.
        # Define the following discount strategies as lambda functions:
        # A flat discount of $50.
        # A 20% percentage discount.
        # Test the apply_discount function with both strategies.

def apply_discount(price, discount_function):
    return discount_function(price) # Applies the discount_function to the price and returns the discounted

# Define the discount strategies as lambda functions:
flat_discount = lambda price: price - 50
percentage_discount = lambda price: price * 0.20

# function call
print("Flat Discount: ", apply_discount(500, flat_discount))
print("Percentage Discount: ", apply_discount(500, percentage_discount))