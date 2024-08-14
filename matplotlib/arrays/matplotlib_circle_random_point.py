from random import random

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 150)
CIRCLE_RADIUS = 1
AMOUNT_OF_SUBPLOTS = 3
a = CIRCLE_RADIUS * np.cos(theta)
b = CIRCLE_RADIUS * np.sin(theta)

figure, axes = plt.subplots(1, 3)


def get_points_by_rejection(amount_of_points):
    points_coordinates = []
    while len(points_coordinates) < amount_of_points:
        x = CIRCLE_RADIUS * (random() * 2 - 1)
        y = CIRCLE_RADIUS * (random() * 2 - 1)
        if x * x + y * y < CIRCLE_RADIUS:
            points_coordinates.append([x, y])
    return points_coordinates


for i in range(AMOUNT_OF_SUBPLOTS):
    axes[i].plot(a, b)
    axes[i].set_aspect(1)

points_coordinates_1 = get_points_by_rejection(1000)
x_coordinates = [point[0] for point in points_coordinates_1]
y_coordinates = [point[1] for point in points_coordinates_1]
axes[0].plot(x_coordinates, y_coordinates, "bo", markersize=1)
axes[0].set_title("Random dots by rejection")

points_coordinates_2 = get_points_by_rejection(1000)
x_coordinates = [point[0] for point in points_coordinates_2]
y_coordinates = [point[1] for point in points_coordinates_2]
axes[1].plot(x_coordinates, y_coordinates, "bo", markersize=1)

plt.show()
