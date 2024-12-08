import numpy as np  # Import numpy library alias name np
from tensorflow.python.keras.backend import dtype

# Create NumPy Array using np.zeros()

arr_1d_zeros = np.zeros((3,))  # 1-D array of zeros with 3 elements
print("arr_1d_zeros", arr_1d_zeros)

arr_2d_zeros = np.zeros((3, 4))  # 2-D array of zeros with 3 rows and 4 columns
print("arr_2d_zeros", arr_2d_zeros)

arr_3d_zeros = np.zeros((3, 4, 2))  # 3-D array of zeros with 3 rows, 4 columns, 2 layers
print("arr_3d_zeros", arr_3d_zeros)

# Output
# arr_1d_zeros [0. 0. 0.]
# arr_2d_zeros [[0. 0. 0. 0.][0. 0. 0. 0.][0. 0. 0. 0.]]
# arr_3d_zeros [[[0. 0.][0. 0.][0. 0.][0. 0.]]
# [[0. 0.][0. 0.][0. 0.][0. 0.]]
# [[0. 0.][0. 0.][0. 0.][0. 0.]]]

print("\n-----------------------------\n")
# Create NumPy Array using np.zeros() with specific data-type

arr_1d_zeros_str = np.zeros((3,), dtype=str)  # 1-D array of str with 3 elements
print("arr_1d_zeros_str", arr_1d_zeros_str)

arr_2d_zeros_bool = np.zeros((3, 4), dtype=bool)  # 2-D array of bool with 3 rows and 4 columns
print("arr_2d_zeros_bool", arr_2d_zeros_bool)

# Output
# arr_1d_zeros_str ['' '' '']
# arr_2d_zeros_bool [[False False False False]
#  [False False False False]
#  [False False False False]]

print("\n-----------------------------\n")
# Create NumPy Array using np.ones()

arr_1d_ones = np.ones((3,))  # 1-D array of ones with 3 elements
print("arr_1d_ones", arr_1d_ones)

arr_2d_ones = np.ones((3, 4))  # 2-D array of ones with 3 rows and 4 columns
print("arr_2d_ones", arr_2d_ones)

arr_3d_ones = np.ones((3, 4, 2))  # 3-D array of ones with 3 rows, 4 columns, 2 layers
print("arr_3d_ones", arr_3d_ones)

# Output
# arr_1d_ones [1. 1. 1.]
# arr_2d_ones [[1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.]]
# arr_3d_ones [[[1. 1.][1. 1.][1. 1.][1. 1.]]
# [[1. 1.][1. 1.][1. 1.][1. 1.]]
# [[1. 1.][1. 1.][1. 1.][1. 1.]]]

print("\n-----------------------------\n")
# Create NumPy Array using np.ones() with boolean data-type

arr_2d_bool = np.ones((3, 4), dtype=bool)  # 2-D array of 3 rows and 4 columns, with dtype=bool
print("arr_2d_bool", arr_2d_bool)

# Output
# arr_2d_bool [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True  True  True]]

print("\n-----------------------------\n")
# Create NumPy Array using np.ones() with complex data-type

arr_1d_complex = np.ones((3,), dtype=complex)  # 1-D array of 3 elements, with dtype=complex
print("arr_1d_complex", arr_1d_complex)

# Output
# arr_1d_complex [1.+0.j 1.+0.j 1.+0.j]

print("\n-----------------------------\n")

arr_1d_empty = np.empty((3,))  # 1-D empty array with 3 elements
print("arr_1d_empty", arr_1d_empty)

arr_2d_empty = np.empty((3, 4), dtype = int)  # 2-D empty array with 3 rows and 4 columns
print("arr_2d_empty", arr_2d_empty)

# Output
# arr_1d_empty [1.13521682e-311 1.13521682e-311 0.00000000e+000]
# arr_2d_empty [[0 1076232192 -858993459 1077300428]
#  [0 1077968896 0 1078231040]
#  [0 1078591488 0 1078951936]]

print("\n-----------------------------\n")
# Create NumPy Array using np.full()

arr_1d_full = np.full((3,), 8)  # 1-D array with 3 elements, fill value = 8
print("arr_1d_full", arr_1d_full)

arr_2d_full = np.full((3, 4), 6)  # 2-D array with 3 rows and 4 columns, fill value = 6
print("arr_2d_full", arr_2d_full)

arr_3d_full = np.full((3, 4, 2), 5)  # 3-D array with 3 rows, 4 columns, 2 layers, fill value = 5
print("arr_3d_full", arr_3d_full)

# Output
# arr_1d_full [8 8 8]
# arr_2d_full [[6 6 6 6][6 6 6 6][6 6 6 6]]
# arr_3d_full [[[5 5][5 5][5 5][5 5]]
# [[5 5][5 5][5 5][5 5]]
# [[5 5][5 5][5 5][5 5]]]

print("\n-----------------------------\n")
# Create NumPy Array using np.full() with different data-type

arr_1d_full = np.full((3,), 8, dtype=float)  # 1-D array with 3 elements, fill value = 8, data-type = float
print("arr_1d_full", arr_1d_full)

arr_2d_full = np.full((3, 4), 6.5, dtype=str)  # 2-D array with 3 rows and 4 columns, fill value = 6.5, data-type = string
print("arr_2d_full", arr_2d_full)

# Output
# arr_1d_full [8. 8. 8.]
# arr_2d_full [['6' '6' '6' '6']
#  ['6' '6' '6' '6']
#  ['6' '6' '6' '6']]

print("\n-----------------------------\n")
# Create NumPy Array using np.full() with Complex value and float data-type

arr_1d_full_complex = np.full((3,), 8+6j, dtype=float)  # 1-D, 3 elements, complex value, data-type = float
print("arr_1d_full_complex", arr_1d_full_complex)

# Output
# arr_1d_full_complex [8. 8. 8.]
# ComplexWarning: Casting complex values to real discards the imaginary part
#   multiarray.copyto(a, fill_value, casting='unsafe')


