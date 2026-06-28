# ============================================
# Day 1 - Python Basics
# Summer Training 2026
# Name: Vanshika Sharma
# Date: 22 June 2026
# ============================================


# -------------------------------
# 1. Introduction to Python
# -------------------------------

print("Hello, Python!")
print("Welcome to Summer Training 2026")


# -------------------------------
# 2. Python Syntax
# Python uses indentation instead of braces.
# -------------------------------

if 10 > 5:
    print("10 is greater than 5")


# -------------------------------
# 3. Print Statement
# -------------------------------

print("My name is Vanshika Sharma")
print("I am learning Python.")


# -------------------------------
# 4. Variables
# -------------------------------

name = "Vanshika"
age = 20
college = "Guru Nanak Dev Engineering College"

print(name)
print(age)
print(college)


# -------------------------------
# 5. Data Types
# -------------------------------

integer_number = 100
decimal_number = 25.5
text = "Python"
status = True

print(type(integer_number))
print(type(decimal_number))
print(type(text))
print(type(status))


# -------------------------------
# 6. Type Casting
# -------------------------------

num = "50"

converted_num = int(num)

print(converted_num)
print(type(converted_num))


# -------------------------------
# 7. Input Function
# -------------------------------

city = input("Enter your city: ")

print("City:", city)


# -------------------------------
# 8. Swapping Variables
# -------------------------------

a = 10
b = 20

print("Before Swapping")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)


# -------------------------------
# 9. Variable Unpacking
# -------------------------------

fruit1, fruit2, fruit3 = ["Apple", "Banana", "Mango"]

print(fruit1)
print(fruit2)
print(fruit3)