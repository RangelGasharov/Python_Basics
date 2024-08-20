def additive_persistence(num):
    if num < 10:
        return 0
    amount_of_replacements = 0
    sum_current_number = 0
    while num >= 10:
        num_as_string = str(num)
        for num in num_as_string:
            sum_current_number += int(num)
        num = sum_current_number
        sum_current_number = 0
        amount_of_replacements += 1

    return amount_of_replacements


def multiplicative_persistence(num):
    if num < 10:
        return 0
    amount_of_replacements = 0
    sum_current_number = 1
    while num >= 10:
        num_as_string = str(num)
        for num in num_as_string:
            sum_current_number *= int(num)
        num = sum_current_number
        sum_current_number = 1
        amount_of_replacements += 1

    return amount_of_replacements


print(additive_persistence(1679583))
print(additive_persistence(123456))
print(additive_persistence(6))
print(additive_persistence(19999999999999999999999))
print(additive_persistence(5789))

print(multiplicative_persistence(77))
print(multiplicative_persistence(123456))
print(multiplicative_persistence(4))
print(multiplicative_persistence(6788))
print(multiplicative_persistence(277777788888899))
