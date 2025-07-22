def get_maximum_erasure_value(numbers):
    numbers_seen = set()
    left = 0
    current_sum = 0
    max_sum = 0

    for right in range(len(numbers)):
        while numbers[right] in numbers_seen:
            numbers_seen.remove(numbers[left])
            current_sum -= numbers[left]
            left += 1
        numbers_seen.add(numbers[right])
        current_sum += numbers[right]
        max_sum = max(max_sum, current_sum)

    return max_sum


print(get_maximum_erasure_value([4, 2, 4, 5, 6]))
print(get_maximum_erasure_value([5, 2, 1, 2, 5, 2, 1, 2, 5]))
print(get_maximum_erasure_value([6, 6, 1, 10, 1]))
