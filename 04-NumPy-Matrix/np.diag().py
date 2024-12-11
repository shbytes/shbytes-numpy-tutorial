import numpy as np

# Create Diagonal Matrix inNumPy using np.diag()

# Create a diagonal matrix from a 1-D array
input_array = np.array([10, 20, 30])
diagonal_matrix = np.diag(input_array)
print(diagonal_matrix)
# Output => [[10  0  0] [ 0 20  0] [ 0  0 30]]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Create a 3x3 2D array (matrix)
# Extract the main diagonal
diagonal_elements = np.diag(matrix)
print(diagonal_elements)
# Output => [1 5 9]

# Extract the diagonal above the main diagonal (k=1)
diagonal_above = np.diag(matrix, k=1)
print(diagonal_above)
# Output => [2 6]

# Extract the diagonal below the main diagonal (k=-1)
diagonal_below = np.diag(matrix, k=-1)
print(diagonal_below)
# Output => [4 8]

# Create a 5x5 diagonal matrix with elements on the second diagonal above the main diagonal (k=1)
input_array = np.array([10, 20, 30, 40])
diagonal_matrix = np.diag(input_array, k=1)
print(diagonal_matrix)
# Output => [[ 0 10  0  0  0] [ 0  0 20  0  0] [ 0  0  0 30  0] [ 0  0  0  0 40] [ 0  0  0  0  0]]

# Create a 3x3 diagonal matrix with complex values
input_array = np.array([1+2j, 3+4j, 5+6j])
diagonal_matrix = np.diag(input_array)
print(diagonal_matrix)
# Output => [[1.+2.j 0.+0.j 0.+0.j] [0.+0.j 3.+4.j 0.+0.j] [0.+0.j 0.+0.j 5.+6.j]]