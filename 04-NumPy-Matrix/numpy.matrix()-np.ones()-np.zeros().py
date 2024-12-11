import numpy as np

matrix= np.matrix([[16, 26], [38, 42]]) # Create a 2x2 matrix
print(matrix)
# Output => [[16 26][38 42]]

print("\n-----------------------------\n")

array = np.array([[16, 26], [38, 42]]) # Create a 2x2 ndarray (which can be treated as a matrix)
print(array)
# Output => [[16 26][38 42]]

# Convert the array to a NumPy matrix
matrix = np.matrix(array)
# Output => [[16 26][38 42]]

print("\n-----------------------------\n")

zero_matrix = np.matrix(np.zeros((3, 3))) # Create a 3x3 matrix of zeros
print("Zero Matrix:", zero_matrix)
# Output => [[0. 0. 0.] [0. 0. 0.] [0. 0. 0.]]

one_matrix = np.matrix(np.ones((3, 3))) # Create a 3x3 matrix of ones
print("One Matrix:", one_matrix)
# Output => [[1. 1. 1.] [1. 1. 1.] [1. 1. 1.]]

print("\n-----------------------------\n")

# Create a 2x2 matrix of random values between 0 and 1
random_matrix = np.matrix(np.random.rand(2, 2))
print("Random Matrix:", random_matrix)
# Output => Random Matrix: [[0.6021748  0.08169072] [0.79366297 0.03931574]]

print("\n-----------------------------\n")
