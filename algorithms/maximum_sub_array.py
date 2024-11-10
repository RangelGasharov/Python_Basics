def max_sub_array(numbers):
    if len(numbers) < 1:
        return []
    current_sum = 0
    global_max = numbers[0]

    for number in numbers:
        current_sum += number
        global_max = max(global_max, current_sum)
        if current_sum < 0:
            current_sum = 0
    return global_max


print(max_sub_array([1, 2, 4, -1]))
print(max_sub_array([-1, 2, -4, -1]))
print(max_sub_array([-5, -4, -1]))
print(max_sub_array([9, 2, -10, 5, 6, 2, -3]))
