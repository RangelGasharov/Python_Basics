import math


def perimeter(points_list):
    result = 0
    for i in range(-1, len(points_list) - 1):
        result += get_distance(points_list[i], points_list[i + 1])
    return round(result, 2)


def get_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


print(perimeter([[15, 7], [5, 22], [11, 1]]))
print(perimeter([[0, 0], [0, 1], [1, 0]]))
print(perimeter([[-10, -10], [10, 10], [-10, 10]]))
