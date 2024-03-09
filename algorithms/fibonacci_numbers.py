fibonacci_numbers = {}


def get_fibonacci_numbers(n):
    if n in fibonacci_numbers:
        return fibonacci_numbers[n]
    if n <= 2:
        result = 1
    else:
        result = get_fibonacci_numbers(n - 1) + get_fibonacci_numbers(n - 2)
    fibonacci_numbers[n] = result
    return result


print(get_fibonacci_numbers(7))
print(get_fibonacci_numbers(100))
