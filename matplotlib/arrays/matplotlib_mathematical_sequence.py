import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20)
y1 = np.array((x - 1) / (x + 2))
y2 = np.array((5 * x - 1) / (2 * x - 1))
limit1 = 1
limit2 = 2.5

fig, ax = plt.subplots(2)
ax[0].scatter(x, y1, color="green")
ax[0].set_title("Mathematical sequences, increasing and decreasing")
ax[0].grid(True)
ax[0].axhline(y=limit1, color='r', linestyle='-')

ax[1].scatter(x, y2, color="red")
ax[1].grid(True)
ax[1].axhline(y=limit2, color='r', linestyle='-')

plt.show()
