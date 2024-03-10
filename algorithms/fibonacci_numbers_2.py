def get_fibonacci_numbers(n):
    fibonacci_numbers = {}

    for i in range(1, n + 1):
        if i <= 2:
            result = 1
        else:
            result = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers[i] = result
    return fibonacci_numbers[i]


print(get_fibonacci_numbers(7))
print(get_fibonacci_numbers(100))
