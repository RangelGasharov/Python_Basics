import math


def prime_divisors(number):
    prime_numbers_divisors = []
    prime_numbers = get_prime_numbers(int(math.sqrt(number)) + 3)
    for i in range(len(prime_numbers)):
        if number % prime_numbers[i] == 0:
            prime_numbers_divisors.append(prime_numbers[i])
    if is_prime_number(number):
        if len(prime_numbers_divisors) < 1:
            prime_numbers_divisors.append(number)
    return prime_numbers_divisors


def get_prime_numbers(boundary):
    prime_numbers = []
    for i in range(2, boundary):
        is_prime = is_prime_number(i)
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


def is_prime_number(number):
    for i in range(2, int(math.sqrt(number)) + 2):
        if number % i == 0 and i != number:
            return False
    return True


print(prime_divisors(2))
print(prime_divisors(3))
print(prime_divisors(24))
print(prime_divisors(27))
print(prime_divisors(99))
print(prime_divisors(462))
print(prime_divisors(3457))
print(prime_divisors(1386))
print(prime_divisors(478170))
