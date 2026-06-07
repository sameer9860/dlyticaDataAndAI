#function
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

#lamda function
square = lambda x: x * x
print(square(5))

print("\n" + "=" * 50)

#global variable
price = 1000
def apply_discount(discount):
    global price
    price -= price * discount
    return price
discount = 0.20
final_price = apply_discount(discount)

print(f"Final price after {discount*100}% discount: {final_price}")

print("\n" + "=" * 50)

#local variable
def local_example():
    x = 5
    print(x)
local_example()

print("\n" + "=" * 50)


#1built in modules
import math
from datetime import datetime

print("Current date and time:", datetime.now())
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("Factorial of 5:", math.factorial(5))
print("Power of 2 raised to 3:", math.pow(2, 3))

print("\n" + "=" * 50)


#file handling

#file reading
with open("test/student_collection.txt", "r") as file:
    content = file.read()
    print(content)

print("\n" + "=" * 50)

#file writing

with open("test/new_file.txt", "w") as file:
    file.write("This is a new file created using Python.\n")
    file.write("It demonstrates file writing capabilities.")    

print("\n" + "=" * 50)


#file appending
with open("test/new_file.txt", "a") as file:
    file.write("\n\nThis is a new line appended to the file.")
    
    
    
#Error handling
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
finally: 
    print("Execution completed.")

print("\n" + "=" * 50)

#raise an exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("Age must be at least 18.")
    else:
        print("Age is valid.")
try:    
  validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
finally:
    print("Age validation completed.")       
    
print("\n" + "=" * 50)    
    #oops
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
    
    
student1 = Student("Alice", 20, "New York")
student2 = Student("Bob", 22, "Los Angeles")

student1.display_info()
print("\n" + "-" * 50)
student2.display_info()
print("\n" + "=" * 50)    


#@class methods
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    @classmethod
    def from_string(cls, student_str):
        name, age, city = student_str.split(",")
        return cls(name.strip(), int(age.strip()), city.strip())

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")