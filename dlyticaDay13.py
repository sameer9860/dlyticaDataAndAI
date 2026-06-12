#encapsulation
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
        self.__bank_name = "Dlytica Bank"

acc = BankAccount("John Doe",1000)
print(acc.owner) # John Doe
# print(acc.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
# print(acc.__bank_name) # AttributeError: 'BankAccount' object has no attribute '__
# print(acc.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
# print(acc.__bank_name) # AttributeError: 'BankAccount' object has no attribute '__bank_name'  
print("\n" + "=" * 50)

#getters and setters  @property and @X.setter
class temperature:
    def __init__(self,celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        print("Getting temperature in Celsius...")
        return self.__celsius

    @celsius.setter
    def celsius(self,value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self.__celsius = value

object = temperature(25)
print(object.celsius) # Getting temperature in Celsius... 25
object.celsius = 30
print(object.celsius) # Getting temperature in Celsius... 30

print("\n" + "=" * 50)
#without getter and setter
class temperature:
    def __init__(self,celsius):
        self.celsius = celsius  
object = temperature(25)
print(object.celsius) # 25
object.celsius = -300
print(object.celsius) # -300 (which is not physically possible)
print("\n" + "=" * 50)

#inheritance
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"
    
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
class Dog(Animal):
    def fetch(self):
        return f"{self.name} is fetching the ball."
    
d = Dog("Buddy","Woof")
print(d.speak()) # Buddy says Woof
print(d.sleep()) # Buddy is sleeping.
print(d.fetch()) # Buddy is fetching the ball.
print(isinstance(d,Dog)) # True
print("\n" + "=" * 50)

#super
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year = year

    def car_info(self):
        return f"{self.year} {self.make} {self.model}"  
    
car = Car("Toyota","Camry",2020)
print(car.info()) # Toyota Camry
print(car.car_info()) # 2020 Toyota Camry   
print("\n" + "=" * 50)

#multiple inheritance
class Father:
    def __init__(self,name):
        self.name = name

    def father_info(self):
        return f"Father's name: {self.name}"

class Mother:
    def __init__(self,name):
        self.name = name

    def mother_info(self):
        return f"Mother's name: {self.name}"

class Child(Father,Mother):
    def __init__(self,father_name,mother_name,child_name):
        Father.__init__(self,father_name)
        Mother.__init__(self,mother_name)
        self.child_name = child_name

    def child_info(self):
        return f"Child's name: {self.child_name}"

c = Child("John","Jane","Jack")
print(c.father_info()) # Father's name: John
print(c.mother_info()) # Mother's name: Jane
print(c.child_info()) # Child's name: Jack  

print("\n" + "=" * 50)


#Diamond problem
class A:    
    def method(self):
        return "Method from class A"

class B(A):
    def method(self):
        return "Method from class B"

class C(A):
    def method(self):
        return "Method from class C"

class D(B,C):
    pass

d = D()
print(d.method()) # Method from class B (because of method resolution order)

print("\n" + "=" * 50)


#polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
shapes = [Rectangle(4,5),Circle(3)]
for shape in shapes:
    print(shape.area()) # 20 (area of rectangle) and 28.26 (area of circle)
print("\n" + "=" * 50)    
    
#method overriding
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):    
    def greet(self):
        return "Hello from Child"

parent = Parent()
child = Child()
print(parent.greet()) # Hello from Parent
print(child.greet()) # Hello from Child
print("\n" + "=" * 50)

#Operator overloading
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)

    def __str__(self):
        return f"Vector({self.x},{self.y})"

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2
print(v3) # Vector(4,6)
print("\n" + "=" * 50)

#Duck typing
class Bird:
    def fly(self):
        return "The bird is flying."

class Plane:
    def fly(self):
        return "The plane is flying."

bird = Bird()   
plane = Plane()
for obj in (bird, plane):
    print(obj.fly()) # The bird is flying. and The plane is flying.    
    
#mixins
class Nepal:
    def __init__(self):
        self.country = "Nepal"
    def info(self): 
        return f"This is {self.country}."

class India:
    def __init__(self):
        self.country = "India"
    def info(self):
        return f"This is {self.country}."   
class Person(Nepal,India):
    def __init__(self,name):
        self.name = name
        Nepal.__init__(self)
        India.__init__(self)    
    def person_info(self):
        return f"Name: {self.name}, Country: {self.country}"

person = Person("John")
print(person.info()) # This is Nepal. (because of method resolution order)
print(person.person_info()) # Name: John, Country: Nepal

print("\n" + "=" * 50)

#Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using Credit Card."

class CashPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} in Cash."
    
credit_payment = CreditCardPayment()
cash_payment = CashPayment()
print(credit_payment.pay(100)) # Paid 100 using Credit Card.
print(cash_payment.pay(50)) # Paid 50 in Cash.

print("\n" + "=" * 50)

#magic methods
class Circle:
    def __init__(self,radius):
        self.radius = radius

    # Calculate area
    def area(self):
        return round(3.14 * self.radius ** 2, 2)

    # Calculate circumference
    def circumference(self):
        return round(2 * 3.14 * self.radius, 2)

     # String representation
    def __str__(self):
        return f"Circle(r={self.radius})"
    
    # Official string representation for debugging
    def __repr__(self):
        
        return f"Circle(radius={self.radius})"
    
    
#iterator
class Fibonacci:
    def __init__(self,limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib  
    
fib = Fibonacci(10)
for num in fib:
    print(num) # 0, 1, 1, 2, 3, 5, 8 (Fibonacci numbers up to 10)  
print("\n" + "=" * 50)
    
#generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num) # 0, 1, 1, 2, 3, 5, 8 (Fibonacci numbers up to 10)
print("\n" + "=" * 50)

#decorator
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
        
    return wrapper

@decorator
def say_hello():
    print("Hello, world!")

say_hello()

#python packages and environments
# To create a virtual environment:
# python -m venv myenv
# To activate the virtual environment:
# source myenv/bin/activate (Linux/Mac)
# myenv\Scripts\activate (Windows)
# To install packages:
# pip install package_name  
# To uninstall packages:
# pip uninstall package_name    


#type hints
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))

print("\n" + "=" * 50)