import math


def is_heteromecic(number):
    for i in range(math.ceil(math.sqrt(number)) + 1):
        if i * (i + 1) == number:
            return True
    return False


print(is_heteromecic(0))
print(is_heteromecic(2))
print(is_heteromecic(7))
print(is_heteromecic(110))
print(is_heteromecic(136))
print(is_heteromecic(156))
print(is_heteromecic(380))
print(is_heteromecic(462))
print(is_heteromecic(600))
