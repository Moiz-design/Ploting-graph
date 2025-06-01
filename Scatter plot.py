import numpy as np
import matplotlib.pyplot as plt
plt.clf()# Clears the graphic window
x1= np.linspace(1,10,8)
y=[12 ,123 ,1 ,34, 54 ,123,3,5]
colors = ['k', 'r', 'g', 'y', 'b', 'm', 'c', 'orange']
plt.scatter(x1, y, color=colors, alpha=1)
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.show()