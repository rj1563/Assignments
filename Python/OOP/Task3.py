# Task 3: Inheritance
    # 1. Create a subclass Car that inherits from the Vehicle class.
    # 2. Add an additional attribute to the Car class:number_of_doors (integer)
    # 3. Override the display_info method in the Car class to include the number of doors.
    # 4. Create an object of the Car class and call the display_info method.

# Main Class
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

    # Overriding the main class constructor and adding number_of_doors
    def __init__(self, brand, model, year, price, number_of_doors): 
        super().__init__(brand, model, year, price) 
        self.number_of_doors = number_of_doors

    # Method to display information about a Car
    def display_info(self):
        super().display_info()
        print("Number of doors: ", self.number_of_doors)

# Creating an object of Car class and storing it in the reference variable
car1 = Car("Ford", "Innova Crysta", 2022, 5000000, 4)
car1.display_info()