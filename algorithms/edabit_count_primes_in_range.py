import math


def prime_count(start, end):
    if end < 2:
        return 0
    sieve = [True] * (end + 1)
    sieve[0], sieve[1] = False, False

    for num in range(2, int(math.sqrt(end)) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

    prime_count_in_range = sum(1 for i in range(max(2, start), end + 1) if sieve[i])
    return prime_count_in_range


print(prime_count(1, 10))
print(prime_count(1, 100))
print(prime_count(1, 1000))
print(prime_count(1, 100000))
print(prime_count(2090, 2098))
