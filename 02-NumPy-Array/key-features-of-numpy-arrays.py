# Homogeneous Data Type
import numpy as np

integer_array = np.array([14, 22, 35, 45])  # All integers
string_array = np.array(["shbytes.com", "NumPy", "Python", "Power BI"])  # All strings
boolean_array = np.array([False, True, True, True])  # All booleans

print(integer_array)  # [14 22 35 45]
print(string_array)   # ['shbytes.com' 'NumPy' 'Python' 'Power BI']
print(boolean_array)  # [False  True  True  True]

print("\n------------------------------\n")
# Multidimensional (N-dimensional) Structure

arr1d = np.array([14, 22, 35, 45])  # 1-D array
arr2d = np.array([[14, 22], [35, 45]])  # 2-D array (matrix)
arr3d = np.array([[[14, 22], [35, 45]], [[54, 64], [74, 68]]])  # 3-D array (tensor)

print("\n------------------------------\n")
# Shape and Size of Arrays

arr = np.array([[12, 22, 34], [46, 65, 86]])
print(arr.shape)  # Output: (2, 3) (2 rows and 3 columns)
print(arr.size)   # Output: 6 (2 * 3)

print("\n------------------------------\n")
# Array Indexing and Slicing

arr = np.array([14, 22, 35, 45])
print(arr[2])  # Access the third element (indexing starts at 0) => 35
print(arr[1:3])  # Slice elements from index 1 to 2 (not inclusive of 3) => [22 35]

print("\n------------------------------\n")
# Element-wise Operations

arr_1 = np.array([12, 22, 34])
arr_2 = np.array([46, 65, 86])
result = arr_1 + arr_2  # Element-wise addition
print(result)  # Output: [ 58  87 120]

print("\n------------------------------\n")
# Broadcasting

arr_1 = np.array([12, 22, 34]) # 1-D array with shape (3,) (3 elements)
arr_2 = np.array([[46], [65], [86]])  # 2-D array with shape (3, 1) (3 rows, 1 column)
result = arr_1 + arr_2  # Broadcasting: arr_1 is added to each column of arr_2
print(result)
# Output:
# [[ 58  68  80]
#  [ 77  87  99]
#  [ 98 108 120]]

print("\n------------------------------\n")
# Reshaping Arrays

arr = np.array([12, 22, 34, 46, 65, 86]) # 1-D array with shape (6,) (6 elements)
reshaped_arr = arr.reshape((2, 3))  # Reshape into 2 rows and 3 columns
print(reshaped_arr)
# Output:
# [[12 22 34]
#  [46 65 86]]

print("\n------------------------------\n")
# Universal Functions (ufuncs)

arr = np.array([41, 44, 29, 16])
sqrt_arr = np.sqrt(arr)  # Apply square root to each element
print(sqrt_arr)  # Output: [6.40312424 6.63324958 5.38516481 4.]

print("\n------------------------------\n")
# Concatenation

arr_1 = np.array([15, 52])
arr_2 = np.array([23, 44])
result = np.concatenate((arr_1, arr_2))  # Concatenate along the 0-axis (1-D arrays)
print(result)  # Output: [15 52 23 44]

print("\n------------------------------\n")
# Splitting

arr = np.array([41, 44, 29, 16, 15, 52])
result = np.split(arr, 3)  # Split into 3 sub-arrays
print(result)  # Output: [array([41, 44]), array([29, 16]), array([15, 52])]

print("\n------------------------------\n")
# Memory Efficiency

arr = np.array([41, 44, 29, 16, 15, 52], dtype=np.int32)
print(arr.nbytes)  # Output: 24 (6 integers * 4 bytes per int32)

print("\n------------------------------\n")
# Vectorization

arr = np.array([41, 44, 29, 16, 15, 52])
result = arr * 2  # Multiply each element by 2
print(result)  # Output: [82  88  58  32  30 104]

print("\n------------------------------\n")
# Random Number Generation

random_arr = np.random.rand(2, 3)  # Generate a 2x3 array of random floats in [0, 1)
print(random_arr)
# Output => Can be different on next run
# [[0.328437   0.31566905 0.36429999]
#  [0.03383582 0.72987953 0.33411073]]

print("\n------------------------------\n")
# Linear Algebra Functions

A = np.array([[6, 2], [3, 4]])
B = np.array([[5, 4], [7, 8]])
result = np.dot(A, B)  # Matrix multiplication
print(result)
# Output:
# [[44 40]
#  [43 44]]

print("\n------------------------------\n")
# Universal Mathematical Functions

arr = np.array([12, 22, 32])
log_arr = np.log(arr)  # Natural logarithm of each element
print(log_arr)  # Output: [2.48490665 3.09104245 3.4657359 ]

