# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Define data points for the histogram
x=[2,4,14,14,16,7,8,9,10,11,19,18,15,15,16,13,12,7,8,9,12,]

# Create evenly spaced points from 1 to 20 (not used in histogram)
y=np.linspace(1,20,20)

# Define color for histogram bars
colors = ['g']

# Create histogram with 20 bins, green bars and black edges
plt.hist(x,bins=20,color=colors,edgecolor='black',linewidth=.5)

# Display the plot
plt.show()