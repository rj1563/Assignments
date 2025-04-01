# Task 7: File Handling with OOP
    # 1. Modify the Vehicle class to include a method save_to_file() that:
    # Saves the details of the vehicle to a file named <brand>_<model>.txt.
    # 2. Write a program to:
    # Create a Vehicle object.
    # Call the save_to_file() method to save its details.

# Main class
class Vehicle:

    # Constructor to initialize to data members of the class 
    def __init__(self, brand, model, year, price): 
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def save_to_file(self):
        with open(f"{self.brand}_{self.model}.txt", "w") as file:
            file.write(f"Brand: {self.brand}\n")
            file.write(f"Model: {self.model}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Price: {self.price}\n")

vehicle = Vehicle("Ford", "Innova Crysta", 2023, 500000)
vehicle.save_to_file()