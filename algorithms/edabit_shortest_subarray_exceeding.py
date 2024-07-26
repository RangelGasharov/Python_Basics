def min_length(number_list, number):
    current_sum = 0
    current_count = 0
    for i in range(len(number_list)):
        current_sum += number_list[i]
        if current_sum > number:
            return i + 1
    return -1


print(min_length([5, 8, 2, -1, 3, 4], 9))
print(min_length([3, -1, 4, -2, -7, 2], 4))
print(min_length([1, 0, 0, 0, 1], 1))
print(min_length([0, 1, 1, 0], 2))
print(min_length([3, -1, 4, 3, 0, 1, 2], 7))
