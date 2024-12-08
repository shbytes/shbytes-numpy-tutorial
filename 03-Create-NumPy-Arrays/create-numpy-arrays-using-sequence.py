import numpy as np  # Import numpy library alias name np

list_1 = [15, 32, 43, 44, 65] # list with integer elements
arr_1 = np.array(list_1)
print(arr_1) # Output => [15 32 43 44 65] => Array all elements are integer
print(arr_1.nbytes)

print("\n-----------------------------\n")
# Example Program - Create NumPy Array using List with Heterogeneous Elements

list_2 = [11, 22.3, 33, 55] # list with integer and float data-type elements
array_2 = np.array(list_2)
print(array_2) # Output => [11.  22.3 33.  55. ] => Array all elements are float

list_3 = [10, 'a', 22.4, 51] # list with integer, string and float data-type elements
array_3= np.array(list_3)
print(array_3) # Output => ['10' 'a' '22.4' '51'] => Array all elements are string

string_list = ['Python', 'NumPy', 'Pandas', 'Java'] # list with string data-type elements
string_array= np.array(string_list)
print(string_array) # Output => ['Python' 'NumPy' 'Pandas' 'Java'] => Array all elements are string
print(string_array.nbytes) # 96

list_4 = [11, 2, 34, 76] # list with integer elements
array_4 = np.array(list_4, dtype='U16') # datatype of an array can be defined explicitly
print(array_4) # Output => ['11' '2' '34' '76'] => Array all elements are string

print("\n-----------------------------\n")
# Example Program - Create 2-D NumPy Array using Nested List

nested_list = [[11, 22.3, 33], [41, 52, 63]] # nested list with integer and float data-type elements
arr_2d = np.array(nested_list)
print(arr_2d)

# Output => 2-D Array all elements are float
# [[11.  22.3 33. ]
#  [41.  52.  63. ]]

nested_list_2 = [['a', 22.3, 33], [41, 52, 63]] # nested list with integer, string and float data-type elements
string_array_2d= np.array(nested_list_2)
print(string_array_2d)

# Output => 2-D Array all elements are string
# [['a' '22.3' '33']
#  ['41' '52' '63']]

print("\n-----------------------------\n")
# Create NumPy Array using Tuple

integer_tuple = (23, 34, 367, 76) # tuple with all integer data-type elements
array_using_tuple = np.array(integer_tuple)  # Create NumPy array using Tuple
print(array_using_tuple) # Output => [ 23  34 367  76]

float_tuple = (11, 22.3, 33, 55)  # tuple with integer and float data-type elements
float_array = np.array(float_tuple)  # Create NumPy array using Tuple
print(float_array) # Output => [11.  22.3 33.  55. ] => Array all elements are float

string_float_tuple = [10, 'a', 22.4, 51] # tuple with integer, string and float data-type elements
string_array = np.array(string_float_tuple)
print(string_array) # Output => ['10' 'a' '22.4' '51'] => Array all elements are string

print("\n-----------------------------\n")
# Example Program - Create 2-D NumPy Array using Nested Tuple

nested_tuple = ((45, 67.3, 53), (86, 65, 23)) # nested tuple with integer and float data-type elements
arr_2d = np.array(nested_tuple)
print(arr_2d)

# Output => 2-D Array all elements are float
# [[45.  67.3 53. ]
#  [86.  65.  23. ]]

nested_tuple_2 = (('s', 22.3, 53), (86, 65, 23)) # nested tuple with integer, string and float data-type elements
string_array_2d= np.array(nested_tuple_2)
print(string_array_2d)

# Output => 2-D Array all elements are string
# [['s' '22.3' '53']
#  ['86' '65' '23']]

nested_tuple_3 = (['s', 22.3, 86], [12, 93, True]) # nested tuple with list elements
array_2d= np.array(nested_tuple_3)
print(array_2d)

# Output => 2-D Array all elements are string
# [['s' '22.3' '86']
#  ['12' '93' 'True']]

print("\n-----------------------------\n")
# # Create NumPy Array using Python Array

import array

python_integer_array = array.array('i', [1, 2, 3, 4, 5]) # Python array with integer numbers
numpy_integer_array = np.array(python_integer_array) # NumPy array with integer numbers
print(numpy_integer_array)
# Output => [1 2 3 4 5]

python_float_array = array.array('f', [65.34, 87.22, 12.22, 54.45, 86.46]) # Python array with float numbers
numpy_float_array = np.array(python_float_array) # NumPy array with float numbers
print(numpy_float_array)
# Output => [65.34 87.22 12.22 54.45 86.46]

python_bool_array = array.array('b', [True, False, True, True, False]) # Python array with boolean values represented as 0 or 1
numpy_bool_array = np.array(python_bool_array) # NumPy array with boolean values
print(numpy_bool_array)
# Output => [1 0 1 1 0]
