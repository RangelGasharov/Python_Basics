import matplotlib.pyplot as plt
import numpy as np

step_of_calculation = 0.1
start_x_axes = -5
end_x_axes = 7
starting_point = 1
ending_point = 5
amount_of_rectangles = 4
delta_x = (ending_point - starting_point) / amount_of_rectangles

x = np.arange(start_x_axes, end_x_axes + step_of_calculation, step_of_calculation)
y = 1 / 4 * x ** 2 + 2


def normal_function(x):
    return 1 / 4 * x ** 2 + 2


def get_definite_integral(x):
    return 1 / 12 * x ** 3 + 2 * x


def get_area_definite_integral(start, end):
    return get_definite_integral(end) - get_definite_integral(start)


def get_area_sub_sum(start, n):
    sum_of_area = 0
    for i in range(0, n):
        sum_of_area += delta_x * normal_function(start + i * delta_x)
    return sum_of_area


def get_area_top_sum(start, n):
    sum_of_area = 0
    for i in range(1, n + 1):
        sum_of_area += delta_x * normal_function(start + i * delta_x)
    return sum_of_area


print(get_area_sub_sum(starting_point, amount_of_rectangles))
print(get_area_top_sum(starting_point, amount_of_rectangles))
print(get_area_definite_integral(starting_point, ending_point))

plt.plot(x, y, linewidth=2)
plt.grid(True)

plt.show()
