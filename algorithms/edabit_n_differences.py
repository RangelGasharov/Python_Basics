def n_differences(number_list):
    current_list = number_list
    new_list = []
    for j in range(len(number_list) - 1):
        for i in range(len(current_list) - 1):
            new_list.append(current_list[i + 1] - current_list[i])
        current_list = new_list
        new_list = []
    return current_list[0]


print(n_differences([5, 1, 9, 3, 4, 0]))
print(n_differences([1, 1, 1, 1]))
print(n_differences([5, 8, 8]))
print(n_differences([3, 5]))
print(n_differences([1, 5, 3, 9, 7]))
print(n_differences([5, 1, 9, 6, 1, 7, 3, 4]))
print(n_differences([8, 9, 2, 5, 4, 3, 3, 1, 6]))
