import matplotlib.pyplot as plt
import numpy as np

step_of_calculation = 0.1
start_x_axes = -10
end_x_axes = 10

x = np.arange(start_x_axes, end_x_axes + step_of_calculation, step_of_calculation)
y = x ** 3
for i in range(start_x_axes, end_x_axes + 1):
    x_coordinates = i
    tangent = (3 * x_coordinates ** 2) * x + (x_coordinates ** 3 - 3 * x_coordinates ** 3)
    plt.plot(x, tangent, linewidth=1, color="red")

plt.plot(x, y, linewidth=2)
plt.grid(True)

plt.show()
