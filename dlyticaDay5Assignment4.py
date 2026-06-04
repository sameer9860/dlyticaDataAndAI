# Name: Samir Khatiwada

# Assignment: Day 4 – Cinema Ticket Pricing System

# Date: 04 June 2026

base_price = 1000

age = int(input("Enter your age: "))
day = input("Enter day of the week: ").lower()

member_answer = input("Are you a member? (yes/no): ").lower()
is_member = member_answer == "yes"

if age < 5:
    category = "Free Entry"
    final_price = 0
    discount = "100%"
elif age < 18:
    category = "Minor"
    final_price = base_price * 0.50
    discount = "50%"
elif age >= 60:
    category = "Senior Citizen"
    final_price = base_price * 0.70
    discount = "30%"
else:
    category = "Adult"
    final_price = base_price
    discount = "0%"

weekdays = {
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday"
            }

if is_member and day in weekdays:
    final_price *= 0.90
    discount += " + 10% Member Discount"

if final_price == 0:
    if is_member:
        popcorn = "Large Free Popcorn"
    else:
        popcorn = "Regular Free Popcorn"
else:
    if is_member:
        popcorn = "Free Small Popcorn"
    else:
        popcorn = "No Free Popcorn"

message = "Free Entry" if final_price == 0 else "Enjoy the Show!"

print("\n" + "=" * 50)
print("        CINEMA TICKET SUMMARY")
print("=" * 50)
print(f"Age             : {age}")
print(f"Day             : {day.title()}")
print(f"Member          : {is_member}")
print(f"Category        : {category}")
print(f"Discount        : {discount}")
print(f"Popcorn Offer   : {popcorn}")
print(f"Final Price     : Rs. {final_price:.2f}")
print(f"Message         : {message}")
print("=" * 50)
