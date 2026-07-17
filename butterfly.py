'''import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 12 * np.pi, 1000)

# Parametric equations for the butterfly curve
x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t)**2)
y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t)**2)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='purple')
plt.title('Butterfly Curve')
plt.axis('equal')  # Equal scaling for both axes
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt

# Define the parametric equations
def x(t):
    return np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t)**2)

def y(t):
    return np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t)**2)

# Define the range of t values
t_values = np.linspace(0, 12 * np.pi, 1000)  # 1000 points for smoothness

# Calculate the x and y coordinates
x_values = x(t_values)
y_values = y(t_values)

# Create the plot
plt.figure(figsize=(8, 8))  # Set the figure size
plt.plot(x_values, y_values, color='purple')  # Plot the butterfly curve in purple

# Add title and axis labels
plt.title('Butterfly Curve', fontsize=16)
plt.xlabel('X')
plt.ylabel('Y')

# Ensure the aspect ratio is equal so the butterfly is not distorted
plt.axis('equal')

# Show the plot
plt.grid(True)  # Optionally add a grid
plt.show()
