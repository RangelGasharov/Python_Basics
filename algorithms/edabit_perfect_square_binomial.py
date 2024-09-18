def perfect_square(number):
    amount_perfect_squares = 0
    for p in range(1, int(number ** 0.5) + 1):
        for q in range(1, int(number ** 0.5) + 1):
            a, b, c = p ** 2, 2 * p * q, q ** 2
            if a <= number and b <= number and c <= number:
                amount_perfect_squares += 1
    return amount_perfect_squares


print(perfect_square(6))
print(perfect_square(30))
print(perfect_square(100))
