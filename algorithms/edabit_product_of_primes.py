import math


def product_of_primes(num):
    prime_numbers = get_prime_numbers(num)
    for i in range(len(prime_numbers)):
        if num % prime_numbers[i] == 0:
            if num / prime_numbers[i] in prime_numbers:
                return True
    return False


def get_prime_numbers(boundary):
    prime_numbers = []
    for i in range(2, boundary + 1):
        is_prime = is_prime_number(i)
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


def is_prime_number(number):
    for i in range(2, int(math.sqrt(number)) + 3):
        if number % i == 0 and i != number:
            return False
    return True


print(product_of_primes(2059))
print(product_of_primes(7))
print(product_of_primes(25))
print(product_of_primes(39))
print(product_of_primes(5767))
print(product_of_primes(77))
print(product_of_primes(12))
