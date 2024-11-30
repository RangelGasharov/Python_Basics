def lcm_of_list(numbers):
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    current_number = max_number
    divisible_by_all = False
    while not divisible_by_all:
        divisible_by_all = True
        for i in range(len(numbers)):
            if not current_number % numbers[i] == 0:
                divisible_by_all = False
        current_number += max_number
    return current_number - max_number


print((lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
print(lcm_of_list([13, 6, 17, 18, 19, 20, 37]))
print(lcm_of_list([44, 64, 12, 17, 65]))
print(lcm_of_list([200, 30, 18, 11, 8, 64, 34]))
