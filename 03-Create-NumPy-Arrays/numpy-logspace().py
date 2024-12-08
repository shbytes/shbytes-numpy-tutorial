import numpy as np

# np.logspace() - Create an array from 10^1 to 10^3 (i.e., from 10 to 1000) with Default Parameters
logspace_array_1 = np.logspace(1, 3) # Generate 50 points for base 10 start from 1 to 3
print(logspace_array_1)

# Output
# [  10.           10.98541142   12.06792641   13.25711366   14.56348478
#    15.9985872    17.57510625   19.30697729   21.20950888   23.29951811
#    25.59547923   28.11768698   30.88843596   33.93221772   37.2759372
#    40.94915062   44.98432669   49.41713361   54.28675439   59.63623317
#    65.51285569   71.9685673    79.06043211   86.85113738   95.40954763
#   104.81131342  115.13953993  126.48552169  138.94954944  152.64179672
#   167.68329368  184.20699693  202.35896477  222.29964825  244.20530945
#   268.26957953  294.70517026  323.74575428  355.64803062  390.69399371
#   429.19342601  471.48663635  517.94746792  568.9866029   625.05519253
#   686.648845    754.31200634  828.64277285  910.29817799 1000.        ]
print("\n-----------------------------\n")

# np.logspace() - Create Array with Specified Number of Points (num)
logspace_array_2 = np.logspace(0, 3, num=10)  # Generate 10 points from 10^0 to 10^3
print(logspace_array_2)
# Output => [   1.            2.15443469    4.64158883   10.           21.5443469
#    46.41588834  100.          215.443469    464.15888336 1000.        ]

# logspace_array_3 = np.logspace(0, 3, num=-10)  # Negative value for num
# print(logspace_array_3)
# Output => ValueError: Number of samples, -10, must be non-negative.

print("\n-----------------------------\n")

# np.logspace() - Create an array from 2^1 to 2^10 with base=2
logspace_array_4 = np.logspace(1, 10, num=10, base=2) # Generate 10 points for base 2 start from 1 to 10
print(logspace_array_4)
# Output
# [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]

# np.logspace() - Create an array from 3^1 to 3^7 with base=3
logspace_array_5 = np.logspace(1, 7, num=7, base=3) # Generate 7 points for base 3 start from 1 to 7
print(logspace_array_5)
# Output
# [   3.    9.   27.   81.  243.  729. 2187.]

print("\n-----------------------------\n")

# np.logspace() - Create an array from 2^1 to 2^10 with base=2 using endpoint=True (default)
logspace_array_6 = np.logspace(1, 10, num=10, base=2) # Generate 10 points for base 2 start from 1 to 10
print(logspace_array_6)
# Output
# [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]

# np.logspace() - Create an array from 2^1 to 2^10 with base=2 using endpoint=Fals
logspace_array_7 = np.logspace(1, 10, num=10, base=2, endpoint=False) # Generate 10 points for base 2 start from 1 to 9
print(logspace_array_7)
# Output
# [  2.           3.73213197   6.96440451  12.99603834  24.25146506
#   45.254834    84.44850629 157.58648491 294.06677888 548.74801282]

print("\n-----------------------------\n")
logspace_array_8 = np.logspace(0, 5, num=6, dtype=str)  # Array with string data-type
print("String Array:", logspace_array_8)
# Output => String Array: ['1.0' '10.0' '100.0' '1000.0' '10000.0' '100000.0']

logspace_array_9 = np.logspace(0, 5, num=6, dtype=bool)  # Array with boolean data-type
print("Boolean Array:", logspace_array_9)
# Output => Boolean Array: [ True  True  True  True  True  True]

logspace_array_10 = np.logspace(0, 5, num=6, base=2, dtype=complex)  # Array with complex data-type
print("Complex Array:", logspace_array_10)
# Output => Complex Array: [ 1.+0.j  2.+0.j  4.+0.j  8.+0.j 16.+0.j 32.+0.j]

logspace_array_11 = np.logspace(0, 5, num=6, dtype=int)  # Array with integer data-type
print("Integer Array:", logspace_array_11)
# Output => Integer Array: [     1     10    100   1000  10000 100000]

print("\n-----------------------------\n")

logspace_array_12 = np.logspace(-3, 2, num=6, base=2)  # Array start=-3 (negative) and stop=2 (positive)
print("Array:", logspace_array_12)
# Output => Array: [0.125 0.25  0.5   1.    2.    4.   ] (elements in ascending order)

logspace_array_13 = np.logspace(-8, -3, num=6, base=2)  # Array start=-8 (negative) and stop=-3 (negative)
print("Array:", logspace_array_13)
# Output => Array: [0.00390625 0.0078125  0.015625   0.03125    0.0625     0.125     ] (elements in ascending order)

logspace_array_14 = np.logspace(2, -3, num=6, base=2)  # Array start=2 (positive) and stop=-3 (negative)
print("Array:", logspace_array_14)
# Output => Array: [4.    2.    1.    0.5   0.25  0.125] (elements in descending order)

logspace_array_15 = np.logspace(3, 3, num=6, base=4)  # Array start = stop = 3
print("Array:", logspace_array_15)
# Output => Array: [64. 64. 64. 64. 64. 64.]

print("\n-----------------------------\n")

# Create a 2-D array (e.g., 2x3 array)
logspace_array_16 = np.logspace(1, 3, 6, base=10).reshape(2, 3)
print(logspace_array_16)
# Output => [[  10.           25.11886432   63.09573445]
#  [ 158.48931925  398.10717055 1000.        ]]

# Create a 3-D array (e.g., 2x3x4 array)
logspace_array_17 = np.logspace(1, 4, 24, base=2).reshape(2, 3, 4)
print(logspace_array_17)
# Output => [[[ 2.          2.18924707  2.39640137  2.62315735]
#   [ 2.87136977  3.14306893  3.44047723  3.76602735]
#   [ 4.12238218  4.51245656  4.93944116  5.40682855]]
#
#  [[ 5.91844179  6.47846568  7.09148101  7.76250202]
#   [ 8.49701741  9.30103525 10.1811321  11.14450682]
#   [12.19903947 13.35335573 14.61689747 16.        ]]]

print("\n-----------------------------\n")
print(np.logspace(1, 4, num=3, base=2, endpoint=False, dtype=int))

print("\n-----------------------------\n")
import matplotlib.pyplot as plt

# Generate logarithmic spaced values
x = np.logspace(0.1, 2, num=100)
y = np.log10(x)

# Plotting
plt.plot(x, y)
plt.xscale('log')
plt.yscale('linear')
plt.title("Logarithmic Plot")
plt.xlabel("Logarithmically spaced values")
plt.ylabel("Log10 of values")
plt.show()
