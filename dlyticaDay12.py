# Name: Samir Khatiwada
# Assignment 4  Shape Calculator
# Date: 11 June 2026

import math


# Task 1: Create Circle class
class Circle:
    shapes_created = 0

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        self.radius = radius

        # Increase circle count
        Circle.shapes_created += 1

    # Calculate area
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    # Calculate perimeter
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    # Static method for cm to inch conversion
    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 4)

    # Static method to validate dimension
    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    # Class method to show total circles created
    @classmethod
    def total_created(cls):
        return f"Circles created: {cls.shapes_created}"

    # String representation
    def __str__(self):
        return f"Circle(r={self.radius})"


# Task 2: Create Rectangle class
class Rectangle:
    shapes_created = 0

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive.")

        self.width = width
        self.height = height

        # Increase rectangle count
        Rectangle.shapes_created += 1

    # Calculate area
    def area(self):
        return round(self.width * self.height, 2)

    # Calculate perimeter
    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    # Check if rectangle is a square
    def is_square(self):
        return self.width == self.height

    # Task 3: Static methods
    @staticmethod
    def cm_to_inch(cm):
        return round(cm * 0.3937, 4)

    @staticmethod
    def is_valid_dimension(val):
        return val > 0

    # Task 4: Class method
    @classmethod
    def total_created(cls):
        return f"Rectangles created: {cls.shapes_created}"

    # String representation
    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


try:
    # Task 4: Create shapes
    c1 = Circle(int(input("Enter radius for Circle One: ")))
    c2 = Circle(int(input("Enter radius for Circle Two: ")))
    c3 = Circle(int(input("Enter radius for Circle Three: ")))

    r1 = Rectangle(int(input("Enter width for Rectangle One: ")), int(input("Enter height for Rectangle One: ")))
    r2 = Rectangle(int(input("Enter width for Rectangle Two: ")), int(input("Enter height for Rectangle Two: ")))


    print("\n" + "=" * 50)
    print("Shape Calculator:")
    print("=" * 50 + "\n")
    
    print(c1)
    print(f"Area: {c1.area()}")
    print(f"Perimeter: {c1.perimeter()}")
    
    print("\n" + "-" * 50)
    
    print(r2)
    print(f"Area: {r2.area()}")
    print(f"Perimeter: {r2.perimeter()}")
    print(f"Is Square: {r2.is_square()}")

    print("\n" + "-" * 50)

    # Task 3: Static methods
    print(f"10 cm = {Circle.cm_to_inch(10)} inches")
    print(f"Valid Dimension (-2): {Rectangle.is_valid_dimension(-2)}")

    print("\n" + "-" * 50)
    # Task 4: Class methods
    print(Circle.total_created())
    print(Rectangle.total_created())

except ValueError as e:
    print(f"Error: {e}")