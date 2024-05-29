import math


def number_length(num):
    num = abs(num)
    if num < 1:
        return 1

    return math.floor(math.log10(num) + 1)

print(number_length(10))
print(number_length(9))
print(number_length(0))
print(number_length(1000))
