def find_odd(numbers):
    numbers.sort()
    amount_of_same_numbers = 0
    for i in range(len(numbers) - 1):
        amount_of_same_numbers += 1
        if numbers[i] is not numbers[i + 1]:
            if amount_of_same_numbers % 2 != 0:
                return numbers[i]
            amount_of_same_numbers = 0
    return numbers[0]


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))
print(find_odd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]))
