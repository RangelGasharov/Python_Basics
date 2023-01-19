import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 12, 0.1)
y1 = (1 / 3) * (x ** 2) - x - 1
t1_1 = (-7 / 3) * x - (7 / 3)
t1_2 = (1 / 3) * x - (7 / 3)

y2 = (x ** 2) - 2 * x + 3
t2_1 = (-8) * x - 6
t2_2 = 2 * x ** 0

fig, ax = plt.subplots(2)
ax[0].plot(x, y1, x, t1_1, x, t1_2)
ax[0].set_title("Tangents on function")
ax[0].plot(x, y1, linewidth=0.5)
ax[0].grid(True)

ax[1].plot(x, y2, x, t2_1, x, t2_2)
ax[1].set_title("Tangents on function")
ax[1].plot(x, y2, linewidth=0.5)
ax[1].grid(True)

plt.show()
