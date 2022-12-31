import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4 * np.pi, 0.1)
y1 = np.sin(x)
z1 = np.cos(x)

amplitude_2 = 2
period_seconds_2 = 0.5 * np.pi
angular_velocity_2 = (2 * np.pi) / period_seconds_2
phase_shift_2 = np.pi / 2
displacement_y_axis_2 = 1

y2 = amplitude_2 * np.sin(angular_velocity_2 * x + phase_shift_2) + displacement_y_axis_2

fig, ax = plt.subplots(2)
ax[0].plot(x, y1, x, z1)
ax[0].set_title("Normal sine function")
ax[0].plot(x, y1, linewidth=0.5)
ax[0].grid(True)

ax[1].plot(x, y2)
ax[1].set_title("Modified sine function")
ax[1].plot(x, y2, color="red", linewidth=0.5)
ax[1].grid(True)

plt.show()
