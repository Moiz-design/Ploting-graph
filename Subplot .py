# Import required libraries for plotting and numerical operations
import matplotlib.pyplot as plt
import numpy as np

# Clear the current figure
plt.clf

# 1️⃣ Line Plot (Subplot 2,2,2)
# Create x values from 1 to 100 with 10 evenly spaced points
x = np.linspace(1, 100, 10)
# Calculate sine of x values
y = np.sin(x)

# Create subplot in position 2,2,2
plt.subplot(2, 2, 2)
# Plot x vs y with black square markers and no connecting line
plt.plot(x, y, color='k',linestyle='',marker ='s')  # Black color line
plt.title("Line Plot")

# 2️⃣ Bar Chart (Subplot 2,2,1)
# Define categories for x-axis
X = ["Maths", "English", "Science", "Chemistry"]
y = [90, 85, 91, 95]  # Heights of bars representing scores
colors = ['r', 'y', 'b', 'g']  # Define colors for each bar (red, yellow, blue, green)

# Create subplot in position 2,2,1
plt.subplot(2, 2, 1)
# Create bar chart with specified colors, width and transparency
plt.bar(X, y, color=colors, width=0.5, align='center',alpha=0.8)
plt.title("Bar Chart")

# 3️⃣ Scatter Plot (Subplot 2,2,3)
# Create x values from 1 to 10 with 10 evenly spaced points
x1= np.linspace(1,10,10)
# Calculate exponential of x values
y=np.exp(x1)
# Create subplot in position 2,2,3
plt.subplot(2,2,3)
# Create scatter plot with blue dots and 60% opacity
plt.scatter(x1, y, color='b', alpha=0.6)
plt.title("Scatter plot")

# Display all subplots
plt.show()