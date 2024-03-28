import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('matplotlib_origami_3d.csv', header=None)
print(data)
data_array = np.array(data)

x_coords = data_array[:, 0]
y_coords = np.arange(len(data_array))
z_values = data_array[:, 1:].T
# print("Shape of z_values:", z_values.shape)

bar_width = 0.75

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, x in enumerate(x_coords):
    for j in range(len(z_values)):
        z = z_values[j, i]
        ax.bar3d(x, j, 0, bar_width, bar_width, z, shade=True)

ax.set_xlabel('X-Coordinates')
ax.set_ylabel('Y-Coordinates')
ax.set_zlabel('Value')
ax.set_title('3D-Bar Chart based on Coordinates and Values')

plt.show()
