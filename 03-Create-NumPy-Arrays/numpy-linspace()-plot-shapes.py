import numpy as np
import matplotlib.pyplot as plt

# Plot Circle
# Generate theta values (angle) from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Parametric equations for a circle
x = np.cos(theta)
y = np.sin(theta)

# Plot the circle
plt.plot(x, y)
plt.title("Circle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio ensures it's a circle
plt.grid(True)
plt.show()

print("\n-----------------------------\n")

# Plot Parabola y=x^2
# Generate x values between -10 and 10
x = np.linspace(-10, 10, 400)

# Parabola equation y = x^2
y = x**2

# Plot the parabola
plt.plot(x, y)
plt.title("Parabola: y = x^2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

print("\n-----------------------------\n")
# Plot Sine wave

x = np.linspace(0, 4 * np.pi, 1000) # Generate x values from 0 to 4*pi
y = np.sin(x) # Sine function

# Plot the sine wave
plt.plot(x, y)
plt.title("Sine Wave: y = sin(x)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

print("\n-----------------------------\n")
# Plot a spiral

theta = np.linspace(0, 4 * np.pi, 1000) # Generate theta values (angle) from 0 to 4*pi
r = theta # Generate radius values that increase linearly with theta

# Parametric equations for the spiral
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the spiral
plt.plot(x, y)
plt.title("Spiral: r = θ")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio for proper spiral shape
plt.show()

print("\n-----------------------------\n")
# Plot an ellipse

# Generate theta values (angle) from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 100)

# Ellipse equation parameters
a = 7  # Semi-major axis
b = 3  # Semi-minor axis

# Parametric equations for an ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plot the ellipse
plt.plot(x, y)
plt.title("Ellipse")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio ensures correct ellipse shape
plt.grid(True)
plt.show()
