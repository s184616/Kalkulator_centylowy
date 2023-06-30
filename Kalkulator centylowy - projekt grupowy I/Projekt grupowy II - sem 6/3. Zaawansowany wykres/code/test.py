import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the primary plot
fig, ax1 = plt.subplots()
ax1.plot(x, y1, color='blue')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis 1', color='blue')

# Create the secondary plot
ax2 = ax1.twinx()
ax2.plot(x, y2, color='red')
ax2.set_ylabel('Y-axis 2', color='red')

# Show the plot
plt.show()