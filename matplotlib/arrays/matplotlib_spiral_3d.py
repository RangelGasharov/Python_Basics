from matplotlib import pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")
z_line = np.linspace(0, 10, 100)
x_line = np.cos(2*z_line)
y_line = np.sin(2*z_line)
ax.plot3D(x_line, y_line, z_line)

plt.show()
