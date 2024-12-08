import numpy as np

# np.linspace() - Create Array with Default Parameters
linspace_array_1 = np.linspace(0, 20)  # Generate 50 points between 0 and 20
print(linspace_array_1)

# Output
# [ 0.          0.40816327  0.81632653  1.2244898   1.63265306  2.04081633
#   2.44897959  2.85714286  3.26530612  3.67346939  4.08163265  4.48979592
#   4.89795918  5.30612245  5.71428571  6.12244898  6.53061224  6.93877551
#   7.34693878  7.75510204  8.16326531  8.57142857  8.97959184  9.3877551
#   9.79591837 10.20408163 10.6122449  11.02040816 11.42857143 11.83673469
#  12.24489796 12.65306122 13.06122449 13.46938776 13.87755102 14.28571429
#  14.69387755 15.10204082 15.51020408 15.91836735 16.32653061 16.73469388
#  17.14285714 17.55102041 17.95918367 18.36734694 18.7755102  19.18367347
#  19.59183673 20.        ]
print("\n-----------------------------\n")

# np.linspace() - Create Array with Specified Number of Points (num)
linspace_array_2 = np.linspace(0, 18, num=10)  # Generate 10 points between 0 and 18
print(linspace_array_2)
# Output => [ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18.]

# linspace_array_3 = np.linspace(0, 18, num=-10)  # Negative value for num
# print(linspace_array_3)
# Output => ValueError: Number of samples, -10, must be non-negative.

print("\n-----------------------------\n")
# np.linspace() - Create Array Excluding the Endpoint (endpoint=False)
linspace_array_4 = np.linspace(0, 18, num=10, endpoint=False)  # Exclude the stop value
print(linspace_array_4)
# Output => [ 0.   1.8  3.6  5.4  7.2  9.  10.8 12.6 14.4 16.2]

print("\n-----------------------------\n")
# np.linspace() - Return the Step Size (retstep=True)

linspace_array_5, step_size = np.linspace(0, 12, num=6, endpoint=True, retstep=True)  # Return both the array and step size
print("Array:", linspace_array_5)
print("Step size:", step_size)
# Output => Array: [ 0.   2.4  4.8  7.2  9.6 12. ]
# Step size: 2.4

linspace_array_6, step_size = np.linspace(0, 12, num=6, endpoint=False, retstep=True)  # Return both the array and step size
print("Array:", linspace_array_6)
print("Step size:", step_size)
# Output => Array: [ 0.  2.  4.  6.  8. 10.]
# Step size: 2.0

print("\n-----------------------------\n")
# np.linspace() - Specify a Different Data Type (dtype)

linspace_array_7 = np.linspace(0, 12, num=6, dtype=str)  # Array with string data-type
print("String Array:", linspace_array_7)
# Output => String Array: ['0.0' '2.4' '4.8' '7.199999999999999' '9.6' '12.0']

linspace_array_8 = np.linspace(0, 12, num=6, dtype=bool)  # Array with boolean data-type
print("Boolean Array:", linspace_array_8)
# Output => Boolean Array: [False  True  True  True  True  True]

linspace_array_9 = np.linspace(0, 12, num=6, dtype=complex)  # Array with complex data-type
print("Complex Array:", linspace_array_9)
# Output => Complex Array: [ 0. +0.j  2.4+0.j  4.8+0.j  7.2+0.j  9.6+0.j 12. +0.j]

linspace_array_10 = np.linspace(0, 12, num=6, dtype=int)  # Array with integer data-type
print("Integer Array:", linspace_array_10)
# Output => Integer Array: [ 0  2  4  7  9 12]

print("\n-----------------------------\n")
# np.linspace() - Work with Negative Numbers Sequence

linspace_array_11 = np.linspace(-8, 9, num=6)  # Array start with -8 (negative) and stop at 9 (positive)
print("Array:", linspace_array_11)
# Output => Array: [-8.  -4.6 -1.2  2.2  5.6  9. ] (elements in ascending order)

linspace_array_12 = np.linspace(-8, -1, num=6)  # Array start with -8 (negative) and stop at -1 (negative)
print("Array:", linspace_array_12)
# Output => Array: [-8.  -6.6 -5.2 -3.8 -2.4 -1. ] (elements in ascending order)

linspace_array_13 = np.linspace(8, -1, num=6)  # Array start with 8 (positive) and stop at -1 (negative)
print("Array:", linspace_array_13)
# Output => Array: [ 8.   6.2  4.4  2.6  0.8 -1. ] (elements in descending order)

linspace_array_14 = np.linspace(8, 8, num=6)  # Array start = stop
print("Array:", linspace_array_14)
# Output => Array: [8. 8. 8. 8. 8. 8.]

print("\n-----------------------------\n")

import numpy as np

# Create a 1-D array with 5 evenly spaced numbers between 0 and 80
linspace_array_15 = np.linspace(0, 80, num=5)  # 5 values spaced along the interval 0 to 80

# Now we create a 2-D 3x5 array where each row has these values spaced along axis=1
linspace_array_2d = np.tile(linspace_array_15, (3, 1))  # Repeat the array 3 times along axis 0 (rows)
print(linspace_array_2d)
# Output
# [[ 0. 20. 40. 60. 80.]
#  [ 0. 20. 40. 60. 80.]
#  [ 0. 20. 40. 60. 80.]]

# Now we create a 3-D 3x5*2 array
linspace_array_3d = np.tile(linspace_array_15, (3, 1, 2))  # Repeat the 2-D array 3 times along axis 0 (rows)
print(linspace_array_3d)
# Output
# [[[ 0. 20. 40. 60. 80.  0. 20. 40. 60. 80.]]
#  [[ 0. 20. 40. 60. 80.  0. 20. 40. 60. 80.]]
#  [[ 0. 20. 40. 60. 80.  0. 20. 40. 60. 80.]]]

print("\n-----------------------------\n")

print(np.linspace(2, 11, num=5, dtype=int))
# [ 2  4  6  8 11]