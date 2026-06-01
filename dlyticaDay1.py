# 1. COMPILER vs INTERPRETER

# Compiler   : Converts ALL source code into machine code first, then runs it.
# Interpreter: Executes code LINE BY LINE (Python uses this approach).


# 2. INPUT AND OUTPUT

# input() always returns a string
# print() displays output to the console

persona = input("What is your name: ")
person_age = input("What is your age: ")
print(persona)
print(person_age)


# 3. F-STRINGS (Formatted String Literals)

# f-strings let you embed variables directly inside strings using {}
person_name = input("What is your name: ")
person_age = input("What is your age: ")
print(f"person_name is {person_name} and age is {person_age}")


# 4. VARIABLES

# A variable stores a value in memory and points to it
a = 5
print(a)

name = "honey bunny"    # string variable
age = 66                # integer variable
address = "kathmandu"   # string variable

# type() tells you the data type of a variable
print(type(age))        # Output: <class 'int'>


# --- Variable Naming Rules ---
# 1. Do NOT start with a digit       e.g. 1age is invalid
# 2. Do NOT use Python keywords      e.g. for, while, if
# 3. Do NOT use hyphens (-)          e.g. Age-ff is invalid
# 4. Can start with underscore (_)   e.g. _age = 66 is valid

_age = 66               # valid variable name with underscore

# This would cause a SyntaxError (hyphen in variable name):
# Age-ff = 66


# --- Python Keywords (reserved words, cannot be used as variable names) ---
import keyword
print(keyword.kwlist)


# --- Naming Conventions ---
# camelCase   : childParent     (common in JS, used sometimes in Python)
# snake_case  : child_parent    (recommended style in Python - PEP 8)


# 5. SWAPPING VARIABLES

a = 10
b = 6

# Swap values of a and b in one line (Pythonic way)
a, b = b, a
print(a)   # Output: 6
print(b)   # Output: 10


# 6. DELETING VARIABLES

a = 10
b = 6

print(a)   # Output: 10
del a      # Removes variable 'a' from memory

# print(a) here would raise NameError: name 'a' is not defined

# If another variable points to the same value, it remains unaffected
a = 10
b = a      # both a and b point to the same value (10)
print(b)   # Output: 10
del a      # only removes the label 'a', not the value
print(b)   # Output: 10 (b still works fine)


# 7. MULTIPLE ASSIGNMENT

# Assign the same value to multiple variables in one line
x = y = z = 10
print(x)   # 10
print(y)   # 10
print(z)   # 10


# 8. OPERATORS

# --- 8a. Arithmetic Operators ---
a = 0.1
b = 0.2

print(f"Addition        : {a + b:.2f}")    # + (use :.2f to round to 2 decimals)
print(f"Subtraction     : {a - b}")         # -
print(f"Multiplication  : {a * b}")         # *
print(f"Division        : {a / b}")         # / (always returns float)
print(f"Floor Division  : {a // b}")        # // (rounds down to nearest int)
print(f"Modulus         : {a % b}")         # % (remainder)
print(f"Exponent        : {a ** b}")        # ** (power)

# Note: Floating point numbers can have tiny precision errors in Python
# e.g. 0.1 + 0.2 might show 0.30000000000000004 without rounding


# --- 8b. Comparison Operators ---
# These return True or False (Boolean values)
a = 5
b = 5

print(f"a == b  : {a == b}")   # Equal to
print(f"a >  b  : {a > b}")    # Greater than
print(f"a >= b  : {a >= b}")   # Greater than or equal to
print(f"a <= b  : {a <= b}")   # Less than or equal to
print(f"a <  b  : {a < b}")    # Less than
print(f"a != b  : {a != b}")   # Not equal to


# --- 8c. Logical Operators: and, or, not ---
# and  -> True only if BOTH sides are True
# or   -> True if AT LEAST ONE side is True
# not  -> Reverses the boolean value

# Truth table for 'and':
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

# Truth table for 'or':
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False

# Truth table for 'not':
# not True  = False
# not False = True

a = True
b = False
print(a and b)   # False
print(a or b)    # True
print(not a)     # False
print(not b)     # True

# Practical example with 'and'
a = 7
if a > 6 and a < 10:
    print("a is greater than 6 and less than 10")


# --- 8d. Assignment Operators ---
# Shortcut operators that update a variable's value

a = 6
a += 2    # same as: a = a + 2  →  8
print(a)

b = 7
b -= 2    # same as: b = b - 2  →  5
print(b)

c = 8
c *= 2    # same as: c = c * 2  →  16
print(c)

d = 9
d /= 2    # same as: d = d / 2  →  4.5
print(d)

e = 16
e %= 2    # same as: e = e % 2  →  0 (16 is divisible by 2)
print(e)


# --- 8e. Identity Operators: is, is not ---
# Checks if two variables point to the SAME memory location (not just equal value)

a = 10
b = 20
print(a is b)       # False (different objects in memory)
print(a is not b)   # True

# Note: For large integers, Python creates separate memory objects
a = 1000
b = 1000
print(hex(id(a)))   # Memory address of a
print(hex(id(b)))   # Memory address of b (likely different from a)

# Common real-world use: check if a variable is None
print(a is None)    # False


# --- 8f. Membership Operators: in, not in ---
# Checks if a value exists inside a sequence (list, string, tuple, etc.)

a = [1, 2, 3, 4, 5, "honey bunny"]
print(1 in a)        # True
print(6 in a)        # False
print(6 not in a)    # True

# Also works on strings (checks for substrings)
name = "honey bunny"
print("honey" in name)    # True
print("hello" in name)    # False


# 9. PYTHON DATA TYPES

# Python has the following built-in data types:
# 1. Numeric    : int, float, complex
# 2. Boolean    : bool (True / False)
# 3. Dictionary : dict
# 4. Set        : set
# 5. Sequence   : str (string), list, tuple


# --- 9a. Numeric Types ---
a = 5        # int     (whole numbers)
b = 5.0      # float   (decimal numbers)
c = 5 + 0j   # complex (real + imaginary part)

print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>
print(type(c))   # <class 'complex'>


# --- 9b. Dictionary ---
# Key-value pairs, like a real dictionary (word: definition)
# Syntax: {key: value, key: value}
# Keys must be unique

personal_info = {"name": "honey bunny", "age": 66, "address": "kathmandu"}
print(personal_info)
print(type(personal_info))   # <class 'dict'>


# --- 9c. Boolean ---
a = True
print(type(a))   # <class 'bool'>


# --- 9d. Set ---
# Unordered collection of UNIQUE elements
# Automatically removes duplicates
# Mutable (can add/remove items) but NOT subscriptable (no indexing)

a = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4}
print(a)           # {1, 2, 3, 4, 5, 6} — duplicates removed
print(type(a))     # <class 'set'>

# This would raise a TypeError (sets have no index):
# print(a[0])  →  TypeError: 'set' object is not subscriptable


# --- 9e. String ---
# Ordered, immutable sequence of characters
# Supports indexing and slicing: [start:end]

a = "hello this is hari's book"
print(type(a))     # <class 'str'>
print(a[0:5])      # 'hello' (characters at index 0,1,2,3,4)


# --- 9f. List ---
# Ordered, MUTABLE collection (you can change elements)
# Uses square brackets []

a = [1, 2, 3, 4]
print(type(a))     # <class 'list'>
a[0] = 8           # Changing the first element
print(a)           # [8, 2, 3, 4]


# --- 9g. Tuple ---
# Ordered, IMMUTABLE collection (you CANNOT change elements after creation)
# Uses round brackets ()

a = (1, 2, 3, 4, 5)
print(type(a))     # <class 'tuple'>

# This would raise a TypeError (tuples are immutable):
# a[0] = 8  →  TypeError: 'tuple' object does not support item assignment


# 10. SIMPLE IF CONDITION (bonus from notebook)

a = 7
if a > 6:
    print("a is a number greater than 6")


# 11. FUNCTIONS (briefly introduced at the end of notebook)

# def keyword defines a function
# Triple quotes """ """ are used for docstrings (describing what the function does)

def intro():
    """
    This function returns a greeting string.
    Docstrings appear in help() and IDE tooltips.
    """
    return "hello there"

# Call the function and print its return value
print(intro())