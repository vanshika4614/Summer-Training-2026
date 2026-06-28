# Day 2 - Python Operators

# Arithmetic Operators
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)

print()

# Assignment Operators
x = 10
x += 5
print("After += :", x)

x *= 2
print("After *= :", x)

x -= 4
print("After -= :", x)

print()

# Comparison Operators
num1 = 25
num2 = 18

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)

print()

# Logical Operators
age = 20
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)

print()

# Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)

print()

# Membership Operators
subjects = ["Python", "Java", "C++"]

print("Python" in subjects)
print("HTML" not in subjects)

print()

# Bitwise Operators
a = 8
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)