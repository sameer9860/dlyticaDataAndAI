# Name: Samir Khatiwada
# Assignment   Employee Payroll System
# Date: 17 June 2026
# Approach: Used an abstract Employee class as a contract.
# Each employee type implements its own calculate_pay() method.
# The parent class provides a common payslip() method, demonstrating
# abstraction, inheritance, and polymorphism.

from abc import ABC, abstractmethod


# Task 1: Abstract Employee Class
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    # Task 2: Common Payslip Method
    def payslip(self):
        print(f"{self.name} | Pay: Rs {self.calculate_pay()}")


# Task 3: Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

    # Task 4: String Representation
    def __str__(self):
        return f"FullTimeEmployee({self.name})"


# Task 3: Part-Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    # Task 4: String Representation
    def __str__(self):
        return f"PartTimeEmployee({self.name})"


# Task 3: Contractor
class Contractor(Employee):
    def __init__(self, name, project_fee, projects):
        super().__init__(name)
        self.project_fee = project_fee
        self.projects = projects

    def calculate_pay(self):
        return self.project_fee * self.projects

    # Task 4: String Representation
    def __str__(self):
        return f"Contractor({self.name})"


# -----------------------------------
# Task 5: Testing the Program
# -----------------------------------

staff = [
    FullTimeEmployee("Asha", monthly_salary=60000),
    PartTimeEmployee("Bibek", hourly_rate=500, hours_worked=80),
    Contractor("Rahul", project_fee=15000, projects=3),
]

print("=== Employee Details ===")

for emp in staff:
    print(emp)

print("\n=== Payslips ===")

# Polymorphism:
# No if-statements are needed because every employee
# object knows how to calculate its own pay.
for emp in staff:
    emp.payslip()

# Calculate Total Payroll
total_payroll = sum(emp.calculate_pay() for emp in staff)

print("\nTotal Payroll:", total_payroll)


# -----------------------------------
# Extra Test: Abstract Class Check
# -----------------------------------

print("\n=== Abstract Class Test ===")

try:
    test = Employee("Test")
except TypeError as e:
    print("Error:", e)
    
#Output:
# samir@Samir:~/Dlytica/Python$ python3 dlyticaDay18.py 
# === Employee Details ===
# FullTimeEmployee(Asha)
# PartTimeEmployee(Bibek)
# Contractor(Rahul)

# === Payslips ===
# Asha | Pay: Rs 60000
# Bibek | Pay: Rs 40000
# Rahul | Pay: Rs 45000    

# Total Payroll: 145000

# === Abstract Class Test ===
# Error: can't instantiate abstract class Employee with abstract methods calculate_pay    