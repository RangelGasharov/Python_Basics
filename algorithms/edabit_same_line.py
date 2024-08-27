def same_line(points):
    slope_between = []
    for i in range(len(points) - 1):
        current_slope = 0
        if points[i + 1][0] == points[i][0]:
            current_slop = "INFINITY"
        else:
            current_slope = (points[i + 1][1] - points[i][1]) / (points[i + 1][0] - points[i][0])
        slope_between.append(current_slope)
    for i in range(len(slope_between) - 1):
        if slope_between[i] != slope_between[i + 1]:
            return False
    return True


print(same_line([[0, 0], [1, 1], [3, 3]]))
print(same_line([[-2, -1], [2, 1], [0, 0]]))
print(same_line([[-2, 0], [-10, 0], [-8, 0]]))
print(same_line([[0, 0], [0, 5], [0, 7]]))
print(same_line([[0, 0], [1, 1], [1, 2]]))
print(same_line([[3, 4], [3, 5], [6, 6]]))
print(same_line([[9, 9], [8, 8], [6, 6]]))
print(same_line([[1, 1], [0, 0], [-1, -1], [-2, -2], [-3, -3]]))
