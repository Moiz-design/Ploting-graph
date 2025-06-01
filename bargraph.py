# Import matplotlib library for plotting
import matplotlib.pyplot as plt

# Define y-axis data - popularity percentages
y=[22.2,17.6,8.8,9,7.7,6.7]

# Define x-axis data - programming language names 
x=['java','Python','PHP','JavaScript','C#','C+']

# Define colors for each bar
col = ['r', 'm', 'y', 'b', 'g', 'khaki',]

# Create bar plot with specified colors, transparency and width
ax=plt.bar(x,y,color=col,alpha=.9,width=0.7)

# Add title and axis labels
plt.title("Bar Graph")
plt.xlabel("Programing Language")
plt.ylabel("Popularity")

# Display the plot
plt.show()
