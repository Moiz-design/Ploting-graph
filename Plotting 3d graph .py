# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the x-axis data using linspace to create 10 evenly spaced points from 1 to 10
x = np.linspace(1, 10, 10)
# Define the y-axis data as an array of 10 values
y = np.array([5, 12, 23, 12, 3, 4, 6, 23, 45, 12])
# Define the z-axis data as an array of zeros (for 3D plotting)
z = np.zeros(10)

# Create a figure with a 2x2 grid of subplots, each with 3D projection
fig, ax = plt.subplots(2, 2, figsize=(12, 6), subplot_kw={'projection': '3d'})

# First subplot - 3D Line plot
# Plot a 3D line with markers, green color, and yellow marker edge color
ax[0, 0].plot(x, y, z, marker='o', color='g', mec='y', label="Line Plot")
ax[0, 0].legend()

# Second subplot - 3D Bar Plot
# Define the dimensions of the bars (dx, dy, dz) as arrays of ones
dx = np.ones(10)
dy = np.ones(10)
dz = np.ones(10)
# Define a list of colors for the bars
col = ['r', 'm', 'y', 'b', 'g', 'k', 'c', 'pink', 'khaki', 'lime']

# Create a 3D bar plot using the defined data and colors
ax[0, 1].bar3d(x, y, z, dx, dy, dz, color=col)
ax[0, 1].set_title("Test Data")
ax[0, 1].set_xlabel('X-axis')
ax[0, 1].set_ylabel('Y-axis')

# Third subplot - 3D Scatter Plot
# Create a 3D scatter plot using the defined data and colors
ax[1, 0].scatter(x, y, z, c=col[:len(x)], alpha=0.8)

# Fourth subplot - 3D Contour Plot
# Define the x and y data for the contour plot using linspace
x1 = np.linspace(1, 10, 10)
y1 = np.linspace(1, 10, 10)
# Create a meshgrid for the contour plot
X, Y = np.meshgrid(x1, y1)
# Calculate the z values for the contour plot using a sine function
Z = np.sin(np.sqrt(X**2 + Y**2 + 2))  # Fix calculation using Y

# Create a 3D contour plot with 20 levels and linewidth of 1
ax[1, 1].contour3D(X, Y, Z, 20, linewidths=1)

# Display the plot
plt.show()
