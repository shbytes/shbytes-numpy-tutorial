import numpy as np

x = np.array([-1, 0, 1, 2, 3]) # NumPy array for x coordinates
y = np.array([3, 4, 5])        # NumPy array for y coordinates
X, Y = np.meshgrid(x, y)   # X and Y resulting grid coordinates
print(X)
# Output => [[-1  0  1  2  3]
#            [-1  0  1  2  3]
#            [-1  0  1  2  3]]
print(Y)
# Output => [[3 3 3 3 3]
#            [4 4 4 4 4]
#            [5 5 5 5 5]]

print("\n-----------------------------\n")
# Create numpy.meshgrid() using linspace() Function

x = np.linspace(-3,3, 7, dtype=int)   # NumPy array for x coordinates
y = np.linspace(-5, 4, 10, dtype=int) # NumPy array for y coordinates
X, Y = np.meshgrid(x, y, indexing="xy")   # X and Y resulting grid coordinates
print(X)
# [[-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]
#  [-3 -2 -1  0  1  2  3]]

print(Y)
# [[-5 -5 -5 -5 -5 -5 -5]
#  [-4 -4 -4 -4 -4 -4 -4]
#  [-3 -3 -3 -3 -3 -3 -3]
#  [-2 -2 -2 -2 -2 -2 -2]
#  [-1 -1 -1 -1 -1 -1 -1]
#  [ 0  0  0  0  0  0  0]
#  [ 1  1  1  1  1  1  1]
#  [ 2  2  2  2  2  2  2]
#  [ 3  3  3  3  3  3  3]
#  [ 4  4  4  4  4  4  4]]

print("\n-----------------------------\n")
# Create numpy.meshgrid() with sparse=True

x = np.linspace(-2,3, 6, dtype=int)  # NumPy array for x coordinates
y = np.linspace(-3, 4, 8, dtype=int) # NumPy array for y coordinates
X, Y = np.meshgrid(x, y, sparse=True)   # X and Y resulting grid coordinates
print(X)
# [[-2 -1  0  1  2  3]]

print(Y)
# [[-3]
#  [-2]
#  [-1]
#  [ 0]
#  [ 1]
#  [ 2]
#  [ 3]
#  [ 4]]

print("\n-----------------------------\n")
# Create numpy.meshgrid() with Matrix Indexing

x = np.linspace(-2,3, 6, dtype=int)  # NumPy array for x coordinates
y = np.linspace(-3, 4, 8, dtype=int) # NumPy array for y coordinates
X_ij, Y_ij = np.meshgrid(x, y, indexing="ij")   # X_ij and Y_ij resulting grid coordinates
print(X_ij)
# [[-2 -2 -2 -2 -2 -2 -2 -2]
#  [-1 -1 -1 -1 -1 -1 -1 -1]
#  [ 0  0  0  0  0  0  0  0]
#  [ 1  1  1  1  1  1  1  1]
#  [ 2  2  2  2  2  2  2  2]
#  [ 3  3  3  3  3  3  3  3]]

print(Y_ij)
# [[-3 -2 -1  0  1  2  3  4]
#  [-3 -2 -1  0  1  2  3  4]
#  [-3 -2 -1  0  1  2  3  4]
#  [-3 -2 -1  0  1  2  3  4]
#  [-3 -2 -1  0  1  2  3  4]
#  [-3 -2 -1  0  1  2  3  4]]

print("\n-----------------------------\n")
# Using meshgrid() for 3-D Plotting

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 20) # NumPy array for x coordinates
y = np.linspace(-5, 5, 20) # NumPy array for y coordinates

X, Y = np.meshgrid(x, y) # Create the meshgrid
Z = np.sin(X**2 + Y**2) # Compute Z values based on the function

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show() # Show the plot

print("\n-----------------------------\n")
# Evaluating Functions on a Grid
x = np.linspace(-3, 3, 7)
y = np.linspace(-2, 2, 5)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
print(Z)
# [[13.  8.  5.  4.  5.  8. 13.]
#  [10.  5.  2.  1.  2.  5. 10.]
#  [ 9.  4.  1.  0.  1.  4.  9.]
#  [10.  5.  2.  1.  2.  5. 10.]
#  [13.  8.  5.  4.  5.  8. 13.]]

print("\n-----------------------------\n")
# Contour Plots
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)
plt.contour(X, Y, Z)
plt.title("Contour plot of z = sin(x^2 + y^2)")
plt.show()
