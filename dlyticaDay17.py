# Name: Samir Khatiwada
# Assignment  Bank Money Management System
# Date: 16 June 2026

# Approach: Created a Money class with dunder methods for addition,
# comparison, printing, and sorting. Created a Wallet class to store
# Money objects and calculate the total amount.

# Task 1: Money Class
class Money:
    def __init__(self, amount, currency="Rs"):
        self.amount = amount
        self.currency = currency

    # Task 2: String representation for users
    def __str__(self):
        return f"{self.currency} {self.amount}"

    # Task 2: String representation for developers
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    # Task 3: Add two Money objects
    def __add__(self, other):
        return Money(
            self.amount + other.amount,
            self.currency
        )

    # Task 4: Equality comparison
    def __eq__(self, other):
        return self.amount == other.amount

    # Task 4: Less-than comparison
    def __lt__(self, other):
        return self.amount < other.amount


# Task 5: Wallet Class
class Wallet:
    def __init__(self, notes):
        self.notes = notes

    # Return number of Money objects
    def __len__(self):
        return len(self.notes)

    # Calculate total money in wallet
    def total(self):
        total_money = Money(0)

        for note in self.notes:
            total_money = total_money + note

        return total_money


# -------------------------
# Testing the Program
# -------------------------

print("=== Money Objects ===")

a = Money(int(input("Enter amount for Money One: ")))
b = Money(int(input("Enter amount for Money Two: ")))

print(a + b)                 # Rs 800
print(a == Money(500))       # True
print(b < a)                 # True

print("\n=== Sorting Money ===")

notes = [
    Money(100),
    Money(500),
    Money(50)
]

print(sorted(notes))
# [Money(50, 'Rs'), Money(100, 'Rs'), Money(500, 'Rs')]

print("\n=== Wallet ===")

wallet = Wallet(notes)

print(len(wallet))           # 3
print(wallet.total())        # Rs 650


#Output
# samir@Samir:~/Dlytica/Python$ python3 dlyticaDay17.py 
# === Money Objects ===
# Enter amount for Money One: 500
# Enter amount for Money Two: 300
# Rs 800
# True
# True
# 
# === Sorting Money ===
# [Money(50, 'Rs'), Money(100, 'Rs'), Money(500, 'Rs')]
# 
# === Wallet ===
# 3
# Rs 650

#Another

# samir@Samir:~/Dlytica/Python$ python3 dlyticaDay17.py 
# === Money Objects ===
# Enter amount for Money One: 500
# Enter amount for Money Two: 300
# Rs 800
# True
# True
# 
# === Sorting Money ===
# [Money(50, 'Rs'), Money(100, 'Rs'), Money(500, 'Rs')]
# 
# === Wallet ===
# 3
# Rs 650