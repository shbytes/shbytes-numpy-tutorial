import numpy as np

# Create an array from 0 to 11
arange_array_1 = np.arange(12) # start = 0 (default), stop = 12 (exclusive), step = 1 (default)
print("An array created  from range 0 to 11", arange_array_1)

# array created using start value 4 and stop value 13
arange_array_2 = np.arange(4, 14) # start = 4, stop = 14 (exclusive), step = 1 (default)
print ("An array created from range 4 to 13", arange_array_2)

# Array created using specified step size
arange_array_3 = np.arange(0, 30, 3) # start = 0, stop = 30 (exclusive), step = 3
print("An array created  from range  0 to 27", arange_array_3)

# Output
# An array created  from range 0 to 11 [ 0  1  2  3  4  5  6  7  8  9 10 11]
# An array created from range 4 to 13 [ 4  5  6  7  8  9 10 11 12 13]
# An array created  from range  0 to 27 [ 0  3  6  9 12 15 18 21 24 27]

print("\n-----------------------------\n")

# Array create using float datatype
arange_array_4 = np.arange(0, 10, 1, dtype=float) # start = 0, stop = 10 (exclusive), step = 1, dtype = float
print("An Array created with float value  from 0 to 9", arange_array_4)

# Output
# An Array created with float value  from 0 to 9 [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

print("\n-----------------------------\n")
# Array create using boolean datatype
arange_array_5 = np.arange(0, 3, 2, dtype=bool) # start = 0, stop = 3 (exclusive), step = 2, dtype = bool
print("An Array created with bool value from 0 to 2", arange_array_5)

# Array create using boolean datatype
# arange_array_7 = np.arange(0, 5, 2, dtype=bool) # start = 0, stop = 5 (exclusive), step = 2, dtype = bool
# print("An Array created with bool value from 0 to 5", arange_array_7)

# Output
# An Array created with bool value from 0 to 2 [False  True]
# TypeError: arange() is only supported for booleans when the result has at most length 2.

print("\n-----------------------------\n")
# Array create using complex datatype
arange_array_8 = np.arange(0, 10, 2, dtype=complex) # start = 0, stop = 10 (exclusive), step = 2, dtype = complex
print("An Array created with complex value  from 0 to 9", arange_array_8)

# Output
# An Array created with complex value  from 0 to 9 [0.+0.j 2.+0.j 4.+0.j 6.+0.j 8.+0.j]

print("\n-----------------------------\n")
# Array create using float step Size
arange_array_9 = np.arange(0, 6, 0.5) # start = 0, stop = 6 (exclusive), step = 0.5
print("An Array created with float value from 0 to 5", arange_array_9)

# Output
# An Array created with float value from 0 to 5 [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5]

print("\n-----------------------------\n")
# Array create using negative step Size
arange_array_10 = np.arange(6, 0, -0.5) # start = 6, stop = 0 (exclusive), step = -0.5
print("An Array created with float value from 6 to 0", arange_array_10)

# Output
# An Array created with float value from 6 to 0 [6.  5.5 5.  4.5 4.  3.5 3.  2.5 2.  1.5 1.  0.5]

print("\n-----------------------------\n")
# Array create using np.arange() with Negative Start, Stop and Step
arange_array_11 = np.arange(-2, -7, -0.5) # start = -2, stop = -7 (exclusive), step = -0.5
print("An Array created with float value from -2 to -7", arange_array_11)

# Output
# An Array created with float value from -2 to -7 [-2.  -2.5 -3.  -3.5 -4.  -4.5 -5.  -5.5 -6.  -6.5]

print("\n-----------------------------\n")
print(np.arange(2, 11, 2))
print(np.arange(2, 11, 3))
print(np.arange(2, 11.1, 3))
