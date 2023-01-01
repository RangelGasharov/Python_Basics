import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

x_data = np.arange(0, 50, 0.1)
y_data = np.arange(0, 50, 0.1)
z_data = np.sin(x_data) * np.cos(y_data)

ax.plot(x_data, y_data, z_data, color="green")
ax.set_title("Funny Function")
ax.set_xlabel("sin(x)")
ax.set_ylabel("cos(y)")
ax.set_zlabel("sin(x) * cos(y)")
plt.show()
