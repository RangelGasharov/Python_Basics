def sum_dig_prod(*args):
    sum_numbers = 0
    for arg in args:
        sum_numbers += arg
    result = multiplicative_persistence(sum_numbers)
    return result


def multiplicative_persistence(num):
    if num < 10:
        return num
    sum_current_number = 1
    while num >= 10:
        num_as_string = str(num)
        for num in num_as_string:
            sum_current_number *= int(num)
        num = sum_current_number
        sum_current_number = 1

    return num


print(sum_dig_prod(0))
print(sum_dig_prod(16, 28))
print(sum_dig_prod(1, 2, 3, 4, 5, 6))
print(sum_dig_prod(26, 497, 62, 841))
print(sum_dig_prod(123, -99))
print(sum_dig_prod(111111111))
print(sum_dig_prod(999, 2222))
print(sum_dig_prod(8618, -2))
