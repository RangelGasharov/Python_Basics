def largest_gap(number_list):
    number_list.sort()
    biggest_gap = 0
    for i in range(1, len(number_list)):
        current_gap = number_list[i] - number_list[i - 1]
        if current_gap > biggest_gap:
            biggest_gap = current_gap
    return biggest_gap


print(largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]))
print(largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]))
print(largest_gap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]))
print(largest_gap([26, 17, 4, 25, 29, 26, 8, 30, 4, 20, 2, 7, 29, 7, 20, 30, 23, 5]))
