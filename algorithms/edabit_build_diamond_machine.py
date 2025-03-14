import math


def diamond(size):
    result = []
    start_index = 1 if size % 2 == 0 else 0
    end_index = size if size % 2 == 0 else size + 1
    for i in range(start_index, math.floor(size / 2) + 1):
        current_row = [0] * size
        left_index = math.floor(size / 2) - i
        right_index = math.ceil(size / 2) + i - 1
        current_row[left_index] = 1
        current_row[right_index] = 1
        result.append(current_row)
    for i in range(math.ceil(size / 2) + 1, end_index):
        current_row = [0] * size
        left_index = math.floor(size / 2) + (i - size)
        right_index = math.ceil(size / 2) - (i - size) - 1
        current_row[left_index] = 1
        current_row[right_index] = 1
        result.append(current_row)
    quality_indicator = "good cut" if size % 2 == 0 else "perfect cut"
    result.append(quality_indicator)
    return result


def print_list(number_list):
    for i in range(len(number_list)):
        print(f"{number_list[i]}")


print_list(diamond(1))
print_list(diamond(3))
print_list(diamond(4))
print_list(diamond(5))
print_list(diamond(6))
print_list(diamond(7))
print_list(diamond(10))
