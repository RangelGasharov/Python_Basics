import matplotlib.pyplot as plt
import numpy as np

step_of_calculation = 0.1
start_x_axes = 0
end_x_axes = 10

x = np.arange(start_x_axes + 0.01, end_x_axes + step_of_calculation, step_of_calculation)
y = np.log(x)
for i in range(start_x_axes + 1, end_x_axes + 1):
    x_coordinates = i
    tangent = (1 / x_coordinates) * x + (np.log(x_coordinates) - 1 / x_coordinates * x_coordinates)
    plt.plot(x, tangent, linewidth=1, color="red")

plt.plot(x, y, linewidth=2)
plt.grid(True)

plt.show()
