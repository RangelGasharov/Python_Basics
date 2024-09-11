def eratosthenes(num):
    result = []
    prime_numbers = [True for i in range(num + 1)]
    current_prime_number = 2
    while current_prime_number ** 2 <= num:
        if prime_numbers[current_prime_number]:
            for i in range(current_prime_number ** 2, num + 1, current_prime_number):
                prime_numbers[i] = False
        current_prime_number += 1

    for i in range(2, num + 1):
        if prime_numbers[i]:
            result.append(i)
    return result


print(eratosthenes(0))
print(eratosthenes(1))
print(eratosthenes(30))
print(eratosthenes(1000))
