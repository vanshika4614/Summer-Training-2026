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

# -------------------------------
# Day 6 - Function Practice
# -------------------------------

# Palindrome

def palindrome(value):
    value = str(value)

    if value == value[::-1]:
        return "Palindrome"

    return "Not Palindrome"


print("Palindrome Check")
print(palindrome(121))
print(palindrome("aba"))
print()


# Fibonacci Series

def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

print("Fibonacci Series")
fibonacci(10)
print("\n")


# Largest and Second Largest Number

def largest_numbers(numbers):

    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    print("Largest Number:", unique_numbers[-1])
    print("Second Largest Number:", unique_numbers[-2])


marks = [45, 87, 65, 99, 76, 99]

largest_numbers(marks)

print()


# Factorial (Without Recursion)

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print("Factorial of 5:", factorial(5))

print()


# Vowel, Consonant, Digit or Special Character

def check_character(ch):

    if ch.isalpha():

        if ch.lower() in "aeiou":
            print(ch, "is a Vowel")

        else:
            print(ch, "is a Consonant")

    elif ch.isdigit():
        print(ch, "is a Digit")

    else:
        print(ch, "is a Special Character")


check_character("A")
check_character("8")
check_character("@")

print()


# Sum of Elements in a List

def list_sum(numbers):

    return sum(numbers)


values = [10, 20, 30, 40]

print("Sum =", list_sum(values))

print()


# Count Occurrence of an Element

def count_element(items, value):

    return items.count(value)


numbers = [1, 2, 3, 2, 4, 2, 5]

print("Count =", count_element(numbers, 2))

print()


# Sum of N Natural Numbers Using Recursion

def natural_sum(n):

    if n == 1:
        return 1

    return n + natural_sum(n - 1)


print("Sum =", natural_sum(10))
