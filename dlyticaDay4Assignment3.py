# Name: Samir Khatiwada

# Assignment: Day 3 – Mini Project: Personal Bio-Data Card

# Date: 03 June 2026

full_name = input("Enter your full name: ")
city = input("Enter your city: ")

age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

student_answer = input("Are you a student? (yes/no): ").lower()
is_student = student_answer == "yes"

day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

birth_date = (day, month, year)

hobby1 = input("Enter hobby 1: ")
hobby2 = input("Enter hobby 2: ")
hobby3 = input("Enter hobby 3: ")

hobbies = [hobby1, hobby2, hobby3]

language1 = input("Enter language 1: ")
language2 = input("Enter language 2: ")
language3 = input("Enter language 3: ")

languages = {language1, language2, language3}

profile = {
    "full_name": full_name,
    "city": city,
    "age": age,
    "height": height,
    "is_student": is_student,
    "birth_date": birth_date,
    "hobbies": hobbies,
    "languages": languages
}

print("\n" + "=" * 50)
print("          PERSONAL BIO-DATA CARD")
print("=" * 50)

print(f"Name              : {profile['full_name']}")
print(f"City              : {profile['city']}")
print(f"Age               : {profile['age']}")
print(f"Height            : {profile['height']} m")
print(f"Student           : {profile['is_student']}")
print(f"Birth Date        : {birth_date[0]}/{birth_date[1]}/{birth_date[2]}")
print(f"Hobbies           : {profile['hobbies']}")
print(f"Languages         : {profile['languages']}")

print("-" * 50)

print(f"First Letter      : {full_name[0]}")
print(f"Total Hobbies     : {len(hobbies)}")
print(f"Unique Languages  : {len(languages)}")

print("-" * 50)

print(f"Type of Name      : {type(full_name)}")
print(f"Type of Age       : {type(age)}")
print(f"Type of Height    : {type(height)}")
print(f"Type of Student   : {type(is_student)}")
print(f"Type of BirthDate : {type(birth_date)}")
print(f"Type of Hobbies   : {type(hobbies)}")
print(f"Type of Languages : {type(languages)}")

print("=" * 50)
