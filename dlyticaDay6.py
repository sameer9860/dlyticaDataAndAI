# Conditional statements
salary_amount = 7000000
tax_amount = 0
if salary_amount > 500000:
    tax_amount = salary_amount * 0.01
elif salary_amount > 500000:
    tax_amount = salary_amount * 0.1
   
print(tax_amount)

# Ternary operator
x = int(input("Enter a number: "))
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Looping statements
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    result.append(num ** 2)
print(result)

list_sqr = []
for item in range(1,4):
    inout_num = int(input("Enter a number: "))
    list_sqr.append(inout_num ** 2)
print(list_sqr)


#enumerate
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for index, fruit in enumerate(fruits,5):
    print(f"{index}: {fruit}")
    
    
# while loop    
num = 2
while num < 5:
    print(f"number: {num}")
    num += 1    
    
    
num = 2
while num < 5:
    print(f"number: {num}")
    num += 1
    if num == -5:
     break 
else:
    print("Loop ended without break")


#pass statement
x = 2
if x==2:
    pass  
else:    
    print("x is not 2")   
    
    
#nested loops
mark = 60

if mark >= 50:
    print("Passed")
    if mark >= 75:
        print("Distinction")
    else:
        print("No Distinction")
else:
    print("Failed")    
 
 
 # break statement
for num in range(1, 10):
    if num == 5:
        break
    print(num)   
    
#continue statement
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num)    
    
#    list
items = [1, 2, 3, 4, 5, "apple", "banana", "cherry", "date", "elderberry"]
print(items)
print(items[0])  # Accessing first element
print(items[5])  # Accessing sixth element
print(items[-1]) # Accessing last element
print(items[2:5]) # Accessing a slice of the list`
print(items[1:7:2]) # Accessing a slice of the list with a step of 2
items.append("fig")  # Adding an element to the end of the list
print(items)
items.insert(2, "grape")  # Inserting an element at index 2
print(items)

list = [2,8,3,4,1,5,7,6,9]
list.sort()  # Sorting the list in ascending order
print(list)

sorted_list = sorted(list)  # Sorting the list in descending order
print(sorted_list)

#list comprehension
squared_numbers = [x ** 2 for x in range(1, 11)]
print(squared_numbers)

math_marks = [85, 92, 78, 90, 88]
math_marks_rank = ["pass " if marks <80 else "distinction" for marks in math_marks]
print(math_marks_rank)


list = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
even_numbers = [num for num in list if num % 2 == 0]
print(even_numbers)


#tuples
nums = (1, 2, 3, 4, 5,3)
print(type(nums))
print(nums)
print(nums[0])

#sets
my_set = {1, 2, 3, 4, 5,3,2}
print(type(my_set))
print(my_set)

x={}
print(type(x))

#dictionary
person = {
    "name": "Ram",
    "age": 30, 
    "city": "Ktm"}
print(type(person))
print(person)

print(person["name"])
print(person.get("age"))