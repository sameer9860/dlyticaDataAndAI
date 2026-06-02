# Name: Samir Khatiwada

# Assignment: Day 2  Mini Project: Student Report Card Generator

# Date: 02 June 2026


name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subject1 = float(input("Enter marks in Subject 1: "))
subject2 = float(input("Enter marks in Subject 2: "))
subject3 = float(input("Enter marks in Subject 3: "))

student = { # Dictionary to store student information and marks
    "name": name,
    "roll_no": roll_no,
    "subject1": subject1,
    "subject2": subject2,
    "subject3": subject3
}


total = subject1 + subject2 + subject3

percentage = total / 3

passed = subject1 >= 40 and subject2 >= 40 and subject3 >= 40

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"
    
    

remark = "Needs Improvement"

if passed:
    if grade in {"A+", "A"}:
        remark = "Distinction"
    elif grade == "B":
        remark = "First Division"
    elif grade == "C":
        remark = "Second Division"
    elif grade == "D":
        remark = "Third Division"

    
    
status = "PASS" if passed else "FAIL"

print("\n" + "=" * 40)
print("      STUDENT REPORT CARD")
print("=" * 40)

print(f"Name       : {student['name']}")
print(f"Roll No    : {student['roll_no']}")

print("-" * 40)

print(f"Subject 1  : {subject1}")
print(f"Subject 2  : {subject2}")
print(f"Subject 3  : {subject3}")

print("-" * 40)

print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Remark     : {remark}")
print(f"Status     : {status}")

print("=" * 40)
