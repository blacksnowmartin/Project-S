import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor('white')

# Add text to the plot
ax.text(0.5, 0.5, 'I am a Sissy', fontsize=50, color='pink', ha='center', va='center')

# Remove axes
ax.axis('off')

# Show the plot
plt.show()
