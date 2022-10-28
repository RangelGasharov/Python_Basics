import matplotlib.pyplot as plt
import numpy as np

STARTING_POINT = 50
slope1 = 1.3
slope2 = 0.7
x = np.linspace(0, 20)
y1 = np.array(slope1 ** x)
y2 = np.array(slope2 ** x)

fig, ax = plt.subplots(2)
ax[0].plot(x, y1)
ax[0].set_title("Exponential Graphs, increasing and decreasing")
ax[0].plot(x, y1, color="green", linewidth=0.5)
ax[0].grid(True)

ax[1].plot(x, y2)
ax[1].plot(x, y2, color="red", linewidth=0.5)
ax[1].grid(True)

plt.show()
