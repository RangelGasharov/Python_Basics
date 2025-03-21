def nums_with_unique_digits(num):
    amount_unique_numbers = 0
    for i in range(0, num + 1):
        amount_unique_numbers += get_amount_unique_digits_numbers(i)
    if num >= 1:
        amount_unique_numbers -= 1
    return amount_unique_numbers


def get_amount_unique_digits_numbers(num):
    if num == 0:
        return 1
    if num == 1:
        return 10
    amount_unique_numbers = 9
    for i in range(1, num):
        amount_unique_numbers *= (10 - i)
    return amount_unique_numbers


print(nums_with_unique_digits(0))
print(nums_with_unique_digits(1))
print(nums_with_unique_digits(2))
print(nums_with_unique_digits(3))
print(nums_with_unique_digits(4))
print(nums_with_unique_digits(5))
print(nums_with_unique_digits(6))
print(nums_with_unique_digits(7))
print(nums_with_unique_digits(8))
print(nums_with_unique_digits(9))
