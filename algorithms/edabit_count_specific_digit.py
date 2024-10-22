def digit_occurrences(min_num, max_num, digit):
    digit_occurrence = 0
    for current_num in range(min_num, max_num + 1):
        digit_occurrence += get_digit_occurrence(current_num, digit)
    return digit_occurrence


def get_digit_occurrence(num, digit):
    digit_occurrence = 0
    num, digit = str(num), str(digit)
    for letter in num:
        digit_occurrence += (letter == digit)
    return digit_occurrence


print(digit_occurrences(51, 55, 5))
print(digit_occurrences(1, 8, 9))
print(digit_occurrences(-8, -1, 8))
print(digit_occurrences(71, 77, 2))
print(digit_occurrences(-500, -45, 4))
print(digit_occurrences(5, 335, 6))
print(digit_occurrences(18, 37, 3))
print(digit_occurrences(20, 30, 2))
