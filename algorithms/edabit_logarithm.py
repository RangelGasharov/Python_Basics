import math


def logarithm(base, number):
    try:
        result = math.log(number) / math.log(base)
    except:
        result = "Invalid"
    return result


print(logarithm(5, 25))
print(logarithm(2, 64))
print(logarithm(2, 3))
print(logarithm(2, 4))
print(logarithm(5, 9765625))
print(logarithm(1, 2))
print(logarithm(0, 2))
print(logarithm(-1, 2))
print(logarithm(2, 0))
print(logarithm(2, -1))
