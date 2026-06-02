# Name: Samir Khatiwada
# Assignment: Day 1 Operator Precedence & Associativity
# Date: 01 June 2026

# Day 1: Operator Precedence & Associativity

# 1. Operator Precedence

# Operator precedence is the set of rules that determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. Parentheses () have the highest precedence and can be used to override the default order of evaluation.

# 2.Operator Associativity

# Operator associativity determines the order in which operators of the same precedence level are evaluated. Most arithmetic operators such as +, -, *, and / are evaluated from left to right (left-associative), while the exponentiation operator ** is evaluated from right to left (right-associative).

# Common Precedence Rules (Highest to Lowest)

# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary operators +x, -x
# 4. Multiplication, Division, Floor Division, Modulus *, /, //, %
# 5. Addition and Subtraction +, -
# 6. Comparison operators >, <, >=, <=, ==, !=
# 7. Logical not
# 8. Logical and
# 9. Logical or

# The following program demonstrates these precedence and associativity rules with practical examples and expected outputs.


# DAY 1 ASSIGNMENT: OPERATOR PRECEDENCE & ASSOCIATIVITY

print("=== 1. Arithmetic Operator Precedence ===")

print(2 + 3 * 4)
# Expected: 14
# Reason: Multiplication (*) has higher precedence than addition (+).

print((2 + 3) * 4)
# Expected: 20
# Reason: Parentheses force addition to happen before multiplication.

print(20 - 8 / 2)
# Expected: 16.0
# Reason: Division (/) is evaluated before subtraction (-).


print("\n=== 2. Exponentiation Associativity ===")

print(2 ** 3 ** 2)
# Expected: 512
# Reason: ** is right-associative, so 2 ** (3 ** 2) = 2 ** 9.

print((2 ** 3) ** 2)
# Expected: 64
# Reason: Parentheses change the evaluation order.

print(-3 ** 2)
# Expected: -9
# Reason: Exponentiation occurs before unary minus, so -(3 ** 2).

print((-3) ** 2)
# Expected: 9
# Reason: Parentheses make -3 the base before exponentiation.


print("\n=== 3. Left-to-Right Associativity ===")

print(100 / 5 * 2)
# Expected: 40.0
# Reason: / and * have the same precedence and are evaluated left to right.

print(10 - 5 - 2)
# Expected: 3
# Reason: - operators have the same precedence and are evaluated left to right.

print(20 + 5 - 3)
# Expected: 22
# Reason: + and - share precedence and are evaluated left to right.


print("\n=== 4. Arithmetic, Comparison and Logical Operators ===")

print(5 + 3 * 2 > 10 and not False)
# Expected: True
# Reason: * first, then +, then >, then not, then and.

print(10 > 5 or 3 > 8 and False)
# Expected: True
# Reason: and has higher precedence than or.

print(not 5 > 3 and 10 > 5)
# Expected: False
# Reason: Comparison occurs before not; not True becomes False.

print((5 + 3) * 2 > 20 or not (4 < 2))
# Expected: True
# Reason: Parentheses first, then comparison, then not, then or.


print("\n=== End of Demonstration ===")

