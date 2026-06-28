# Day 4 - User Defined Functions

# Function without parameters
def greet():
    print("Welcome to Python Programming!")

greet()

print()


# Function with parameters
def add(a, b):
    return a + b

result = add(15, 20)
print("Sum =", result)

print()


# Function with default argument
def introduce(name="Student"):
    print("Hello,", name)

introduce()
introduce("Vanshika")

print()


# Function returning multiple values
def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(20, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)

print()


# Function using *args
def total_marks(*marks):
    print("Total Marks:", sum(marks))

total_marks(80, 75, 90, 85)

print()


# Function using **kwargs
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(
    Name="Vanshika",
    Course="Data Analysis",
    College="GNDEC"
)



print("\nFunctions with Lists\n")


# Passing a list to a function

def show_fruits(fruits):
    for fruit in fruits:
        print(fruit)

fruit_list = ["Apple", "Banana", "Mango"]

show_fruits(fruit_list)

print()


# Returning a new list

def square_numbers(numbers):

    squared = []

    for num in numbers:
        squared.append(num * num)

    return squared


numbers = [1, 2, 3, 4, 5]

print(square_numbers(numbers))

print()


# Built-in functions with lists

marks = [82, 65, 91, 78, 88]

print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Sorted:", sorted(marks))

print()


# Remove duplicate values

def unique_items(items):
    return list(set(items))


values = [1, 2, 2, 3, 4, 4, 5]

print(unique_items(values))

print()


# List Comprehension

numbers = [1, 2, 3, 4, 5]

square = [num ** 2 for num in numbers]

print(square)


even = [num for num in numbers if num % 2 == 0]

print(even)