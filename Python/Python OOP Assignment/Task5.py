# Task 5: Abstraction
    # 1. Create an abstract class Shape with an abstract method calculate_area().
    # 2. Create subclasses Rectangle and Circle that inherit from Shape.
    # For the Rectangle class, use attributes length and width.
    # For the Circle class, use attribute radius.
    # 3. Implement the calculate_area method in both subclasses.
    # 4. Write a program to:
    # Create objects of Rectangle and Circle.
    # Call the calculate_area method for each object and display the result

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
    
rectangle = Rectangle(3, 4)
circle = Circle(5)

print("Rectangle Area: ", rectangle.calculate_area())
print("Circle Area: ", circle.calculate_area())