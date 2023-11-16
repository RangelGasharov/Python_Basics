import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4, 9, 1)
y = [0.004, 0.045, 0.49, 4.7, 51]

fig, ax = plt.subplots(2)
ax[0].plot(x, y)
ax[0].set_title("Algorithm time by number length")
ax[0].plot(x, y, linewidth=0.5)
ax[0].grid(True)

plt.yscale("log")
ax[1].plot(x, y)
ax[1].set_title("Algorithm time by number length")
ax[1].plot(x, y, linewidth=0.5)
ax[1].grid(True)
plt.show()
