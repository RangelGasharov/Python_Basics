from random import random
import math
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 150)
CIRCLE_RADIUS = 0.5
AMOUNT_OF_DOTS = 2000
AMOUNT_OF_SUBPLOTS = 3
a = CIRCLE_RADIUS * np.cos(theta)
b = CIRCLE_RADIUS * np.sin(theta)

figure, axes = plt.subplots(1, 3)


def get_points_by_rejection(amount_of_points):
    points_coordinates = []
    while len(points_coordinates) < amount_of_points:
        x = CIRCLE_RADIUS * (random() * 2 - 1)
        y = CIRCLE_RADIUS * (random() * 2 - 1)
        if x * x + y * y < CIRCLE_RADIUS * CIRCLE_RADIUS:
            points_coordinates.append([x, y])
    return points_coordinates


def get_points_by_polar(amount_of_points):
    points_coordinates = []
    for x in range(amount_of_points + 1):
        angle = random() * 2 * math.pi
        r = math.sqrt(random())
        points_coordinates.append([r * math.cos(angle) * CIRCLE_RADIUS, r * math.sin(angle) * CIRCLE_RADIUS])
    return points_coordinates


for i in range(AMOUNT_OF_SUBPLOTS):
    axes[i].plot(a, b)
    axes[i].set_aspect(1)

axes[0].set_title("Random dots by rejection")
points_coordinates_1 = get_points_by_rejection(AMOUNT_OF_DOTS)
x_coordinates = [point[0] for point in points_coordinates_1]
y_coordinates = [point[1] for point in points_coordinates_1]
axes[0].plot(x_coordinates, y_coordinates, "bo", markersize=1)

axes[1].set_title("Random dots by using polar")
points_coordinates_2 = get_points_by_polar(AMOUNT_OF_DOTS)
x_coordinates = [point[0] for point in points_coordinates_2]
y_coordinates = [point[1] for point in points_coordinates_2]
axes[1].plot(x_coordinates, y_coordinates, "ro", markersize=1)

plt.show()
