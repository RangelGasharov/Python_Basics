def is_disarium(num):
    sum_digits = 0
    for index, x in enumerate(str(num)):
        digit = int(x) ** (index + 1)
        sum_digits += digit
    return True if sum_digits == num else False


print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(544))
print(is_disarium(518))
print(is_disarium(8))
print(is_disarium(80))
