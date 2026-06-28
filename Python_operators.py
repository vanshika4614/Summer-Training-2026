# ============================================
# Day 2 - Python Operators
# Summer Training 2026
# Name: Vanshika Sharma
# Date: 23 June 2026
# ============================================


# -------------------------------
# 1. Arithmetic Operators
# -------------------------------

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# -------------------------------
# 2. Assignment Operators
# -------------------------------

x = 10

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

x /= 4
print("After /= :", x)


# -------------------------------
# 3. Comparison Operators
# -------------------------------

num1 = 15
num2 = 20

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)


# -------------------------------
# 4. Logical Operators
# -------------------------------

a = True
b = False

print("AND :", a and b)
print("OR  :", a or b)
print("NOT :", not a)


# -------------------------------
# 5. Identity Operators
# -------------------------------

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)


# -------------------------------
# 6. Membership Operators
# -------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)


# -------------------------------
# 7. Bitwise Operators
# -------------------------------

a = 10
b = 4

print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("NOT :", ~a)
print("Left Shift :", a << 1)
print("Right Shift:", a >> 1)