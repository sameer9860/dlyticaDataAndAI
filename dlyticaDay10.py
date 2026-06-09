# Name: Samir Khatiwada
# Assignment 2  Personal Expense Tracker
# Date: 09 June 2026

# Function to load expenses from a file
def load_expenses(filename):
    try:
        expenses = []
        with open(filename, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append((category, float(amount)))
        return expenses
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    
# Function to add a new expense to the file
def add_expense(filename, category, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    with open(filename, "a") as file:
        file.write(f"{category},{amount}\n")
        
# Function to calculate totals by category and overall total
def category_totals(expenses):
    totals = {}
    for category, amount in expenses:
        totals[category] = totals.get(category, 0) + amount
    grand_total = sum(totals.values())
    print("\nCategory         Total")
    print("-" * 25)
    for category, total in totals.items():
        print(f"{category:<15}: ${total:.2f}")
    print("-" * 25)
    print(f"Grand Total     : ${grand_total:.2f}")

# Function to filter expenses above a certain threshold
def above_threshold(expenses, limit):
    return [(c, a) for c, a in expenses if a > limit]

try:
    filename = "txt_files/expenses.txt"
    expenses = load_expenses(filename)
    category_totals(expenses)
    print("\nExpenses above $100:")
    for category, amount in above_threshold(expenses, 100):
        print(f"  {category:<14} → ${amount:.2f}")
except ValueError as e:
    print(f"Error: {e}")