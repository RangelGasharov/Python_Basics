def is_shifted(original_numbers, resulting_numbers):
    if len(original_numbers) != len(resulting_numbers):
        return False
    differences_numbers = []
    for i in range(len(original_numbers)):
        differences_numbers.append(resulting_numbers[i] - original_numbers[i])
    for i in range(1, len(differences_numbers)):
        if differences_numbers[i - 1] != differences_numbers[i]:
            return False
    return True


def is_multiplied(original_numbers, resulting_numbers):
    if len(original_numbers) != len(resulting_numbers):
        return False
    factors_numbers = []
    for i in range(len(original_numbers)):
        factors_numbers.append(resulting_numbers[i] / original_numbers[i])
    for i in range(1, len(factors_numbers)):
        if factors_numbers[i - 1] != factors_numbers[i]:
            return False
    return True


print(is_shifted([1, 2, 3], [2, 3, 4]))
print(is_shifted([1, 2, 3], [-9, -8, -7]))
print(is_shifted([1, 2, 3], [2, 3, 5]))
print(is_shifted([1, 2, 3], [-9, -1, -7]))
print(is_multiplied([1, 2, 3], [10, 20, 30]))
print(is_multiplied([1, 2, 3], [-0.5, -1, -1.5]))
print(is_multiplied([1, 2, 3], [0, 0, 0]))
print(is_multiplied([1, 2, 3], [-0.5, -1, -2]))
print(is_multiplied([1, 2, 3], [0, 0, 1]))
