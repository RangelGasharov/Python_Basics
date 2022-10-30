import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 10)
y1 = np.array((3 * x) / (2 * x + 1))
y2 = np.array((x ** 2) / (2 * x + 3))
y3 = np.array((3 * x + 1) / x)
limit1 = 1.5
limit3 = 3

fig, ax = plt.subplots(3)

ax[0].set_title("Mathematical sequences, increasing and decreasing")
ax[0].scatter(x, y1, color="green")
ax[0].grid(True)
ax[0].axhline(y=limit1, color='r', linestyle='-')

ax[1].scatter(x, y2, color="blue")
ax[1].grid(True)

ax[2].scatter(x, y3, color="red")
ax[2].axhline(y=limit3, color='r', linestyle='-')
ax[2].grid(True)
plt.show()
