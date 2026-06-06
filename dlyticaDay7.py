# 1. *args (Variable Positional Arguments)

# *args allows a function to accept any number of
# positional arguments.
# Python stores them as a tuple.

def total(*numbers):
    print("Numbers received:", numbers)
    return sum(numbers)

print("Sum:", total(10, 20))
print("Sum:", total(10, 20, 30, 40))

print("\n" + "=" * 50)


# Example: Display multiple student names

def show_students(*students):
    print("Students List:")

    for student in students:
        print(student)

show_students("Samir", "Ram", "Hari", "Sita")

print("\n" + "=" * 50)


# 2. **kwargs (Variable Keyword Arguments)

# **kwargs allows a function to accept any number
# of keyword arguments.
# Python stores them as a dictionary.

def profile(**info):

    print("Profile Information:")

    for key, value in info.items():
        print(f"{key}: {value}")

profile(
    name="Samir",
    age=22,
    city="Kathmandu",
    profession="Developer"
)

print("\n" + "=" * 50)


# 3. Combining *args and **kwargs

# A function can receive:
# Required arguments
# *args
# **kwargs

def student_details(name, age, *skills, **extra):

    print("Name:", name)
    print("Age:", age)

    print("\nSkills:")

    for skill in skills:
        print("-", skill)

    print("\nExtra Information:")

    for key, value in extra.items():
        print(f"{key}: {value}")


student_details(
    "Samir",
    22,
    "Python",
    "Django",
    "React",
    city="Kathmandu",
    country="Nepal"
)

print("\n" + "=" * 50)


# 
# 4. map()

# map() applies a function to every element
# in a collection.

numbers = [1, 2, 3, 4, 5]

# Square every number

squares = list(map(lambda x: x ** 2, numbers))

print("Original Numbers:", numbers)
print("Squared Numbers:", squares)

print("\n" + "=" * 50)


# Another map() example

names = ["samir", "ram", "sita"]

# Convert first letter to uppercase

formatted_names = list(map(str.title, names))

print("Original Names:", names)
print("Formatted Names:", formatted_names)

print("\n" + "=" * 50)


# 5. filter()

# filter() selects elements that satisfy a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep only even numbers

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)

print("\n" + "=" * 50)


# Another filter() example

students = ["Samir", "", "Ram", "", "Sita"]

# Remove empty strings

valid_students = list(filter(None, students))

print("Original List:", students)
print("After Removing Empty Values:", valid_students)

print("\n" + "=" * 50)


# 6. zip()

# zip() combines multiple collections
# element by element.

names = ["Samir", "Ram", "Sita"]
scores = [85, 90, 95]

combined = list(zip(names, scores))

print("Combined Data:")
print(combined)

print("\n" + "=" * 50)


# Real-life zip() example

names = ["Samir", "Ram", "Sita"]
scores = [85, 90, 95]

print("Student Results:")

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

print("\n" + "=" * 50)



# BONUS PRACTICE

# Using map(), filter(), and zip() together

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Step 2: Square even numbers
squares = list(map(lambda x: x ** 2, evens))

# Step 3: Pair original even numbers with squares
result = list(zip(evens, squares))

print("Original Numbers:", numbers)
print("Even Numbers:", evens)
print("Squared Evens:", squares)
print("Paired Result:", result)

print("\n" + "=" * 50)


