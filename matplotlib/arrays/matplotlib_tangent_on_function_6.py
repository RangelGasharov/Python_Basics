import matplotlib.pyplot as plt
import numpy as np

step_of_calculation = 0.1
start_x_axes = -5
end_x_axes = 10

x = np.arange(start_x_axes, end_x_axes + step_of_calculation, step_of_calculation)
y = np.e ** x
for i in range(start_x_axes, end_x_axes + 1):
    x_coordinates = i
    tangent = (np.e ** x_coordinates) * x + (np.e ** x_coordinates - np.e ** x_coordinates * x_coordinates)
    plt.plot(x, tangent, linewidth=1, color="red")

plt.plot(x, y, linewidth=2)
plt.grid(True)

plt.show()
