# Name: Samir Khatiwada
# Assignment  Bank Account Management System
# Date: 15 June 2026
# Approach: Created a BankAccount base class with private balance,
# then inherited SavingsAccount and CurrentAccount to add extra features.

# Task 1: Base Class
class BankAccount:
    def __init__(self, owner, opening_balance=0):
        self.owner = owner
        self.__balance = opening_balance

    # Task 2: Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}")
        else:
            print("Deposit amount must be positive!")

    # Task 3: Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print("Not enough balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount}")

    # Task 4: Getter Method
    def get_balance(self):
        return self.__balance

    # Helper method for child classes
    def _update_balance(self, amount):
        self.__balance += amount


# Task 5: Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, owner, opening_balance=0):
        super().__init__(owner, opening_balance)

    def add_interest(self, rate):
        interest = self.get_balance() * rate / 100
        self._update_balance(interest)
        print(f"Interest added: Rs.{interest}")


# Task 6: Current Account
class CurrentAccount(BankAccount):
    def __init__(self, owner, opening_balance=0, overdraft_limit=0):
        super().__init__(owner, opening_balance)
        self.overdraft_limit = overdraft_limit

    # Method Overriding
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif self.get_balance() - amount < -self.overdraft_limit:
            print("Overdraft limit reached!")
        else:
            self._update_balance(-amount)
            print(f"Withdrawn Rs.{amount}")


# -------------------------------
# Testing the Program
# -------------------------------

print("=== Savings Account ===")
s = SavingsAccount("Asha", 1000)

s.deposit(500)
s.add_interest(10)

print("Current Balance:", s.get_balance())  # 1650

s.withdraw(5000)  # Not enough balance


print("\n=== Current Account ===")
c = CurrentAccount("Bibek", 200, overdraft_limit=500)

c.withdraw(600)  # Allowed
print("Current Balance:", c.get_balance())  # -400

c.withdraw(200)  # Overdraft limit reached



#Output
# samir@Samir:~/Dlytica/Python$ python3 dlyticaDay16.py 
# === Savings Account ===
# Deposited Rs.500
# Interest added: Rs.150.0
# Current Balance: 1650.0
# Not enough balance!

# === Current Account ===
# Withdrawn Rs.600
# Current Balance: -400
# Overdraft limit reached!