import math


def is_powerful(num):
    prime_factors = get_prime_factors(num)
    for x in prime_factors:
        if num % x ** 2 != 0:
            return False
    return True


def get_prime_factors(num):
    prime_factors = []
    for i in range(2, math.ceil(math.sqrt(num)) + 2):
        while num % i == 0:
            prime_factors.append(i)
            num /= i
    return prime_factors


print(is_powerful(36))
print(is_powerful(27))
print(is_powerful(81))
print(is_powerful(360))
print(is_powerful(674))
