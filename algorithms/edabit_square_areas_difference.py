import math


def square_areas_difference(radius):
    return int(round(4 * radius ** 2 - 4 * (radius * math.sin(math.pi / 4)) ** 2, 0))


print(square_areas_difference(5))
print(square_areas_difference(6))
print(square_areas_difference(7))
