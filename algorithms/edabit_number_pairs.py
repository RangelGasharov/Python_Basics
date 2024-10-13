def number_pairs(numbers_string):
    amount_of_pairs = 0
    index_last_pairs = -1
    numbers = numbers_string.split()[1:]
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1] and i != index_last_pairs:
            amount_of_pairs += 1
            index_last_pairs = i + 1
    return amount_of_pairs


print(number_pairs("7 1 2 1 2 1 3 2"))
print(number_pairs("9 10 20 20 10 10 30 50 10 20"))
print(number_pairs("4 2 3 4 1"))
print(number_pairs("13 10 20 20 10 10 30 50 10 20 50 50 30 20"))
print(number_pairs("10 1 2 5 6 5 2 1 7 8 1"))
print(number_pairs("16 2 3 5 11 1 11 5 7 9 13 17 3 8 7 2 1"))
print(number_pairs("6 1 2 2 4 3 4"))
