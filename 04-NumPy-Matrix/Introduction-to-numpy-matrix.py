import numpy as np

M = np.matrix([[16, 26], [38, 42]]) # Create a 2x2 matrix
print(M)
# Output => [[16 26][38 42]]

print("\n-----------------------------\n")

A = np.array([[16, 26], [38, 42]]) # Create a 2x2 ndarray (which can be treated as a matrix)
print(A)
# Output => [[16 26][38 42]]

print("\n-----------------------------\n")
# NumPy Array vs NumPy Matrix
# Dimensionality

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3-D shape array
print(arr_3d.shape)  # Output: (2, 2, 2)

mat_2d = np.matrix([[1, 2], [3, 4]]) # 2-D shape matrix
print(mat_2d.shape)  # Output: (2, 2)

print("\n-----------------------------\n")
# Operations (Element-wise vs Matrix-specific)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1 * arr2) # Array Element-wise multiplication
# Output: [[ 5 12] [21 32]]

multiplication_result = np.dot(arr1, arr2)  # Matrix multiplication using np.dot()
multiplication_result = arr1 @ arr2   # Or using the @ operator (Python 3.5+):

mat1 = np.matrix([[1, 2], [3, 4]])
mat2 = np.matrix([[5, 6], [7, 8]])
print(mat1 * mat2)  # Matrix multiplication (not element-wise)
# Output => [[19 22] [43 50]]

print("\n-----------------------------\n")
# Shape and Return Type

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
result = np.dot(arr1, arr2)
print(result.shape)  # Output: (2, 2)
print(type(result))  # <class 'numpy.ndarray'>

mat1 = np.matrix([[1, 2], [3, 4]])
mat2 = np.matrix([[5, 6], [7, 8]])
result = mat1 * mat2
print(result.shape)  # Output: (2, 2)
print(type(result))  # <class 'numpy.matrix'>

print("\n-----------------------------\n")
# Shape and Return Type
# Broadcasting

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([5, 6])
print(arr1 + arr2)  # Broadcasting: adds [5, 6] to each row of arr1
# Output =>  [[ 6  8] [ 8 10]]
