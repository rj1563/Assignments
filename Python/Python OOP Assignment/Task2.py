# Task 2: Encapsulation
    # 1. Modify the Vehicle class:
    # Make the price attribute private.
    # Add getter and setter methods for price to access and modify it.
    # 2. Write a program to:
    # Create a Vehicle object.
    # Use the setter method to set the price.
    # Use the getter method to retrieve and display the price.

class Vehicle:

    # Constructor to initialize to data members of the class 
    def __init__(self, brand, model, year, price): 
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
    
    # Setter Method to set the price
    def set_price(self, price):
        self.__price = price

    # Getter method to retrieve and display the price
    def get_price(self):
        return self.__price

# Creating object of Vehicle class and storing in reference variable
vehicle1 = Vehicle("Ford", "Innova Crysta", 2022, 5000000)
vehicle1.set_price(6000000) # Setting the new price of a vehicle
print("Updated price is: ", vehicle1.get_price()) 