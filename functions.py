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