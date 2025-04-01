# Task 4: Polymorphism
    # 1. Create another subclass Bike that inherits from the Vehicle class.
    # 2. Override the display_info method in the Bike class to customize its output.
    # 3. Write a program to demonstrate polymorphism by calling the display_info method on
    # objects of Vehicle, Car, and Bike classes

# Main class
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

# Sub class inheriting main class
class Car(Vehicle):

    # Overriding the constructor and adding number_of_doors
    def __init__(self, brand, model, year, price, number_of_doors): 
        super().__init__(brand, model, year, price) 
        self.number_of_doors = number_of_doors

    # Method to display information about a Car
    def display_info(self):
        super().display_info()
        print("Number of doors: ", self.number_of_doors)

# Sub class inheriting main class
class Bike(Vehicle):

    # Overriding the constructor and adding bike_type
    def __init__(self, brand, model, year, price, bike_type): 
        super().__init__(brand, model, year, price) 
        self.bike_type = bike_type

    # Method to display information about a Bike
    def display_info(self):
        super().display_info()  # Calling the base class display_info
        print("Bike type:", self.bike_type)


# Create an instance of Vehicle
vehicle = Vehicle("Ford", "Innova Crysta", 2023, 500000)
print("Vehicle Info:")
vehicle.display_info()

print("\nCar Info:")
# Create an instance of Car
car = Car("Toyota", "Corolla", 2022, 22000, 4)
car.display_info()  # Calling overridden display_info for Car

print("\nBike Info:")
# Create an instance of Bike
bike = Bike("Yamaha", "FZ", 2021, 12000, "Sport")
bike.display_info()  # Calling overridden display_info for Bike