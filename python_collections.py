# ============================================
# Day 3 - Python Collections
# Summer Training 2026
# ============================================


# Lists

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[1])

fruits.append("Orange")
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.sort()
print(fruits)

print(len(fruits))


# Tuples

colors = ("Red", "Green", "Blue")

print(colors)
print(colors[0])
print(len(colors))


# Sets

numbers = {10, 20, 30, 40}

print(numbers)

numbers.add(50)
print(numbers)

numbers.remove(20)
print(numbers)


# Dictionary

student = {
    "Name": "Vanshika",
    "Age": 20,
    "Course": "Data Analysis"
}

print(student)

print(student["Name"])

student["College"] = "GNDEC"

print(student)

student.pop("Age")

print(student)

print(student.keys())

print(student.values())