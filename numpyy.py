# Create a NumPy array of numbers from 1 to 20.
import numpy as np
l1=np.arange(1,21)
print (l1);

# Generate a 3×3 NumPy array filled with zeros.
a=np.zeros((3, 3), dtype=int)
print (a)

# Create a 5×5 matrix with values from 1 to 25
matrix = np.arange(1, 26).reshape(5, 5)

print("Matrix:")
print(matrix)

# Extract the diagonal elements
diagonal = np.diag(matrix)

print("\nDiagonal Elements:")
print(diagonal)

# Create a 1D array of even numbers between 10 and 30.
arr=np.arange(10,31)
print(arr%2==0)
print (arr[(arr%2==0)])

# Reshape an array of 12 elements into a 3×4 matrix.
var=np.arange(12).reshape(3,4)
print (var)

# Find the maximum, minimum, and mean values of a NumPy array
arr1=np.array([4,5,8,7,9,10])
print(arr1.min())
print(arr1.max())
print(arr1.mean())


# Perform element-wise addition, subtraction, and multiplication of two arrays. 
arr3 = np.random.randint(1, 18, size=18)
arr4 = np.random.randint(1, 18, size=18)
print (arr3+arr4)
print (arr3-arr4)
print (arr3*arr4)

# Create a 2D array and extract the second row using slicing.
print(np.identity(4, dtype = int))
arr =([[1, 2],
                [4, 5]])
print(arr[1])

# import numpy as np

# arr = np.array([[2, 3],
#                 [8, 9]])

# print("Second Row:")
# print(arr[1])      # or arr[1, :]


# Generate an identity matrix of size 4×4.
import numpy as np

identity_matrix = np.eye(4)

print("Identity Matrix:")
print(identity_matrix)

# Use NumPy to generate 5 random integers between 1 and 100.
import numpy as np
random_numbers = np.random.randint(1, 101, 5)
print("Random Numbers:")
print(random_numbers)

# Find the square root and standard deviation of elements in an array.
arr = np.array([4, 9, 16, 25, 36])

print("Array:", arr)

print("Square Root:")
print(np.sqrt(arr))

print("Standard Deviation:")
print(np.std(arr))


# -------------------------------
# Day 9 - More NumPy Practice
# -------------------------------

import numpy as np

# Creating Arrays

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

print()


# Reshaping Array

numbers = np.arange(1, 13)

matrix = numbers.reshape(3, 4)

print("Reshaped Array:")
print(matrix)

print()


# Indexing

print("First Element:", arr[0])
print("Last Element:", arr[-1])

print()


# Sorting Array

values = np.array([12, 5, 8, 20, 3])

print("Before Sorting:")
print(values)

print("After Sorting:")
print(np.sort(values))

print()


# Slicing

print("Array Slice:")
print(arr[1:4])

print()


# Copying Array

copy_array = arr.copy()

copy_array[0] = 100

print("Original Array:")
print(arr)

print("Copied Array:")
print(copy_array)

print()


# Broadcasting

array = np.array([1, 2, 3, 4])

print("Broadcasting (+5):")
print(array + 5)

print()


# Conditional Statements

numbers = np.array([15, 8, 22, 4, 30])

print("Numbers Greater Than 10:")
print(numbers[numbers > 10])

print()


# Aggregate Functions

marks = np.array([70, 85, 90, 78, 88])

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))