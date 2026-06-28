# Day 3 - Python Collections

# List

students = ["Aman", "Vanshika", "Rahul"]

print(students)
print(students[1])

students.append("Priya")
print(students)

students.remove("Rahul")
print(students)

print()

# Tuple

months = ("January", "February", "March")

print(months)
print(months[0])
print(len(months))

print()

# Set

colors = {"Red", "Blue", "Green"}

colors.add("Yellow")
colors.remove("Blue")

print(colors)

print()

# Dictionary

student = {
    "Name": "Vanshika",
    "Age": 20,
    "Course": "Data Analysis"
}

print(student)

print(student["Name"])

student["City"] = "Ludhiana"

print(student)

student.pop("Age")

print(student)

print(student.keys())
print(student.values())