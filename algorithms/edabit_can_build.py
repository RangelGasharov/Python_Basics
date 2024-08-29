def can_build(available_numbers, numbers_to_build):
    for i in range(len(numbers_to_build)):
        numbers_needed = [0] * 10
        number_as_string = str(numbers_to_build[i])
        for j in range(len(number_as_string)):
            numbers_needed[int(number_as_string[j])] += 1
        for j in range(len(numbers_needed)):
            if numbers_needed[j] > available_numbers[j]:
                return False
            else:
                available_numbers[j] -= numbers_needed[j]
    return True


print(can_build([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]))
print(can_build([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]))
print(can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []))
print(can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3]))
print(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80, 0]))
print(can_build([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 23, 45, 6789]))
print(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 8]))
