# Task 6: Method Overloading
    # 1. Add a method calculate_discount in the Vehicle class that:
    # Accepts a single argument (percentage) to calculate the discounted price.
    # Overloads to accept two arguments (percentage and additional discount) to
    # calculate the final discounted price.
    # 2. Write a program to demonstrate both versions of the method.

# Main class
class Vehicle:

    # Constructor to initialize to data members of the class 
    def __init__(self, brand, model, year, price): 
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    # Method to calculate discount and additional discount
    def calculate_discount(self, percentage, additional_discount = 0):
        discount = self.price * (percentage / 100)
        additional = self.price * (additional_discount / 100)
        final_price = self.price - discount - additional
        return final_price
    
# Create an instance of Vehicle
vehicle = Vehicle("Ford", "Innova Crysta", 2023, 500000)

print("Original Price: ", vehicle.price)

print(f"Price after 10% discount: ", vehicle.calculate_discount(10))

print(f"Price after 10% + 5% discount: ", vehicle.calculate_discount(10, 5))