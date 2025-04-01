# Task 1: Create a Class
    # 1. Create a class named Vehicle with the following attributes:
    # brand (string)
    # model (string)
    # year (integer)
    # price (float)
    # 2. Add a method display_info that prints all the details of the vehicle.
    # 3. Create an object of the Vehicle class and call the display_info method

# Created a class named Vehicle
class Vehicle:

    # Constructor to initialize to data members of the class 
    def __init__(self, brand, model, year, price): 
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    # Method to display information about a vehicle
    def display_info(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("Price: ", self.price)

vehicle1 = Vehicle("Ford", "Innova Crysta", 2022, 5000000) # Creating object of Vehicle class and storing in reference variable
vehicle1.display_info() # calling display function using the reference