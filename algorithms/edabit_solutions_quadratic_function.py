def solutions(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        return 1
    if discriminant < 0:
        return 0
    return 2


print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))
print(solutions(5, 10, 5))
