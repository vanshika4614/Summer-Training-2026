# Day 1 - Python Basics

# Print Statement
print("Hello, Python!")
print("Welcome to Summer Training")

# Variables
name = "Vanshika"
college = "GNDEC"
age = 20

print("Name:", name)
print("College:", college)
print("Age:", age)

# Data Types
number = 100
decimal = 12.5
text = "Python"
status = True

print(type(number))
print(type(decimal))
print(type(text))
print(type(status))

# Type Casting
marks = "95"
marks = int(marks)
print(marks)
print(type(marks))

# User Input
city = input("Enter your city: ")
print("City:", city)

# Swapping Variables
a = 10
b = 20

print("Before Swapping")
print(a, b)

a, b = b, a

print("After Swapping")
print(a, b)

# Variable Unpacking
fruit1, fruit2, fruit3 = ["Apple", "Banana", "Mango"]

print(fruit1)
print(fruit2)
print(fruit3)