import numpy as np

# Create Lower Triangular Matrix in NumPy using np.tril()

# Create a 3x3 matrix
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extract the lower triangular part of the matrix (default k=0)
lower_triangle = np.tril(input_matrix)
print(lower_triangle)
# Output => [[1 0 0] [4 5 0] [7 8 9]]

# Extract the lower triangular part with k=1 (including the first diagonal above the main diagonal)
lower_triangle_k1 = np.tril(input_matrix, k=1)
print(lower_triangle_k1)
# Output => [[1 2 0] [4 5 6] [7 8 9]]

# Extract the lower triangular part with k=-1 (including the first diagonal below the main diagonal)
lower_triangle_k_minus_1 = np.tril(input_matrix, k=-1)
print(lower_triangle_k_minus_1)
# Output => [[0 0 0] [4 0 0] [7 8 0]]

# Create a 3x4 matrix (rectangular matrix)
input_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Extract the lower triangular part of the matrix
lower_triangle_rectangular = np.tril(input_matrix)
print(lower_triangle_rectangular)
# Output => [[ 1  0  0  0] [ 5  6  0  0] [ 9 10 11  0]]

print("\n-----------------------------\n")
# Create Upper Triangular Matrix in NumPy using np.triu()

# Create a 3x3 matrix
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extract the upper triangular part of the matrix (default k=0)
upper_triangle = np.triu(input_matrix)
print(upper_triangle)
# Output => [[1 2 3] [0 5 6] [0 0 9]]

# Extract the upper triangular part with k=1 (including the first diagonal above the main diagonal)
upper_triangle_k1 = np.triu(input_matrix, k=1)
print(upper_triangle_k1)
# Output => [[0 2 3] [0 0 6] [0 0 0]]

# Extract the upper triangular part with k=-1 (including the first diagonal below the main diagonal)
upper_triangle_k_minus_1 = np.triu(input_matrix, k=-1)
print(upper_triangle_k_minus_1)
# Output => [[1 2 3] [4 5 6] [0 8 9]]

# Create a 3x4 matrix (rectangular matrix)
input_matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Extract the upper triangular part of the matrix
upper_triangle_rectangular = np.triu(input_matrix)
print(upper_triangle_rectangular)
# Output => [[ 1  2  3  4] [ 0  6  7  8] [ 0  0 11 12]]