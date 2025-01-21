def depth(array):
    max_depth = 0
    for i in range(len(array)):
        if isinstance(array[i], list):
            current_array_depth = depth_recursive(array[i], max_depth)
            if current_array_depth > max_depth:
                max_depth = current_array_depth
    return max_depth + 1


def depth_recursive(array, current_depth):
    max_depth = 0
    for i in range(len(array)):
        if isinstance(array[i], list):
            array_depth = depth_recursive(array[i], current_depth)
            if array_depth > max_depth:
                max_depth = array_depth
    return max_depth + 1


print(depth([1, 2, 3, 4]))
print(depth([1, [2, 3, 4]]))
print(depth([1, [2, [3, 4]]]))
print(depth([1, [2, [3, [4]]]]))
print(depth([1, [2, [3, [4]]], 4]))
print(depth([1, [2], 3, [4], 5, [6]]))
print(depth([1, 2, 3, 4, [[5]], [6], 7]))
