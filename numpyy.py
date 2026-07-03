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