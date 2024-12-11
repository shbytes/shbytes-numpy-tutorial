import numpy as np
# Create Identity Matrix in NumPy using np.eye()

# Create a Square Identity Matrix
identity_matrix_3x3 = np.eye(3) # Creates a 3x3 Identity matrix
print(identity_matrix_3x3)
# Output => [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]

# Create a Non-Square Matrix
identity_matrix_3x4 = np.eye(3, 4) # Creates a 3x4 Identity matrix
print(identity_matrix_3x4)
# Output => [[1. 0. 0. 0.] [0. 1. 0. 0.] [0. 0. 1. 0.]]

# Create a 4x4 matrix with ones on the first diagonal above the main diagonal (k=1)
identity_matrix_4x4 = np.eye(4, k=1)
print(identity_matrix_4x4)
# Output => [[0. 1. 0. 0.] [0. 0. 1. 0.] [0. 0. 0. 1.] [0. 0. 0. 0.]]

# Create a 3x3 identity matrix with integer data type
identity_matrix_integer = np.eye(3, dtype=int)
print(identity_matrix_integer)
# Output => [[1 0 0] [0 1 0] [0 0 1]]

# Create a 2x3 identity matrix with complex numbers
identity_matrix_complex = np.eye(2, 3, dtype=complex)
print(identity_matrix_complex)
# Output => [[1.+0.j 0.+0.j 0.+0.j] [0.+0.j 1.+0.j 0.+0.j]]