import matplotlib.pyplot as plt
import numpy as np

step_of_calculation = 0.1
start_x_axes = 0
end_x_axes = 10

for phase in range(1000000):
    x = np.arange(start_x_axes, end_x_axes + step_of_calculation, step_of_calculation)
    y1 = np.sin(x + phase * np.pi / 40)
    y2 = np.sin(x + np.pi - phase * np.pi / 40)
    y3 = y1 + y2
    for i in range(start_x_axes, end_x_axes + 1):
        x_coordinates = i

    plt.plot(x, y1, linewidth=1)
    plt.plot(x, y2, linewidth=1)
    plt.plot(x, y3, linewidth=2)
    plt.pause(0.001)
    plt.clf()
    plt.grid(True)
plt.show()
