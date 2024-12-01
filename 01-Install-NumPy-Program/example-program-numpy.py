import numpy as np    # import numpy and refer it with alias np

# Creating a NumPy array
numpy_array = np.array([12, 22, 34, 54, 65])

# Displaying the array
print("NumPy Array:", numpy_array)

# Performing mathematical operations
print("Array multiplied by 2:", numpy_array * 2)  # multiplication operation on numpy array elements
print("Sum of the Array:", np.sum(numpy_array))   # sum of all elements of numpy array

# Output
# NumPy Array: [12 22 34 54 65]
# Array multiplied by 2: [ 24  44  68 108 130]
# Sum of the Array: 187