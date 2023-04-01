import matplotlib.pyplot as plt
import numpy as np

step_of_calculation = 0.1
start_x_axes = -10
end_x_axes = 10

x = np.arange(start_x_axes, end_x_axes + step_of_calculation, step_of_calculation)
y = 3 * x ** 2
for i in range(start_x_axes, end_x_axes + 1):
    x_coordinates = i
    y_first_derivative = 6 * x_coordinates * x + (3 * x_coordinates ** 2 - 6 * x_coordinates ** 2)
    plt.plot(x, y_first_derivative, linewidth=1, color="red")

plt.plot(x, y, linewidth=2)
plt.grid(True)

plt.show()
