# 5. Sorting with Lambda
        # Use the same products list from Task 4.
        # Sort the products by price in:
        # Ascending order.
        # Descending order.
        # Print the sorted lists.

# Using products list from task 4
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]

# Sorting products in ascending order based on the price of the products
asc_products = sorted(products, key = lambda x: x["price"])
print("Products in Ascending order: ", asc_products)

print()

# Sorting products in descending order based on the price of the products
desc_products = sorted(products, key=lambda x: x["price"], reverse=True)
print("Products in Descending order: ", desc_products)