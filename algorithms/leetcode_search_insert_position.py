def get_insert_position(numbers, target):
    left = 0
    right = len(numbers)

    while left < right:
        middle = (left + right) // 2
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


print(get_insert_position([1, 3, 5, 6], 5))
print(get_insert_position([1, 3, 5, 6], 2))
print(get_insert_position([1, 3, 5, 6], 7))
print(get_insert_position([1, 3, 5, 6], 0))
