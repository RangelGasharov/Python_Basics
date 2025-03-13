import math


def extract_primes(number):
    number_string = str(number)
    prime_numbers = []
    for i in range(1, len(number_string) + 1):
        j = 0
        while j + i <= len(number_string):
            current_number_string = number_string[j:j + i]
            if current_number_string[0] == "0":
                j += 1
                continue
            current_number = int(current_number_string)
            if is_prime(current_number):
                prime_numbers.append(current_number)
            j += 1
    prime_numbers.sort()
    return prime_numbers


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 2):
        if number % i == 0 and i != number:
            return False
    return True


print(extract_primes(1))
print(extract_primes(2))
print(extract_primes(313))
print(extract_primes(1313))
print(extract_primes(10234))
