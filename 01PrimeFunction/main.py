#!/usr/bin/python3.10

import math
import sys
from prime import cprimes, pyprimes, print_speedup, speedups
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')  # Use the 'Qt5Agg' backend
print("Python version", sys.version)
print(sys.path)

lengths = [2**i for i in range(1, 40)]

# Create a figure and axis
fig, ax = plt.subplots()

# Start interactive mode
plt.ion()

if __name__ == '__main__':
    for length in lengths:
        print(f"Testing for length 2^{int(math.log(length, 2))}")
        cprimes(length)
        pyprimes(length)

        # Clear the plot
        ax.clear()

        # Plot the speedup curve
        ax.semilogx(lengths[:lengths.index(length)+1],
                    speedups[:lengths.index(length)+1])

        ax.set_xlabel('Length')
        ax.set_ylabel('Speedup')
        ax.set_title('Speedup Curve')

        # Redraw the plot
        plt.draw()

        # Pause for a short period, allowing the plot to update
        plt.pause(0.01)

# End interactive mode
plt.ioff()

# Save the figure to a file
plt.show()
