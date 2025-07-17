def get_four_sum(numbers, target):
    numbers.sort()
    n = len(numbers)
    results = []

    for i in range(n - 3):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and numbers[j] == numbers[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                if total == target:
                    results.append([numbers[i], numbers[j], numbers[left], numbers[right]])

                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return results


print(get_four_sum([1, 0, -1, 0, -2, 2], 0))
print(get_four_sum([2, 2, 2, 2, 2], 8))
print(get_four_sum([1, 3, 4, 2, -5, 1, 9, -3], 5))
print(get_four_sum([7, 4, 2, 3, -2, 1, 8, -1], 3))
