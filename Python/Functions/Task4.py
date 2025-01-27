# 4. Using map() and filter()
        # Create a list of dictionaries representing products in a store:
        # products = [
        # {"name": "Laptop", "price": 1200},
        # {"name": "Phone", "price": 800},
        # {"name": "Tablet", "price": 600},
        # {"name": "Monitor", "price": 300}]
        # Use map() with a lambda function to calculate the price after applying a 10% discount to all products.
        # Use filter() with a lambda function to retrieve only the products with a price above $500.

# Creating a list of dictionaries representing products in a store
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]

# Using map() with a lambda function to calculate the price after applying a 10% discount to all products.
discounted_product = list(map(lambda x: x["price"] - x["price"] * 0.10, products))
print(f"Products after applying 10% discount: ", discounted_product)

# Using filter() with a lambda function to retrieve only the products with a price above $500.
above_500 = list(filter(lambda x: x["price"] > 500, products))
print("Products with price > 500: ", above_500)