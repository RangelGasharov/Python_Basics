import math


def quartic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 0
    first_solution = (-b + math.sqrt(discriminant)) / 2 * a
    second_solution = (-b - math.sqrt(discriminant)) / 2 * a
    real_solutions = ((first_solution > 0) * 2 + (first_solution == 0) * 1 + (second_solution > 0) * 2 + (
            second_solution == 0) * 1) * (first_solution != second_solution) + (first_solution == second_solution) * (
                             first_solution > 0) * 2
    return real_solutions


print(quartic_equation(1, -5, 4))
print(quartic_equation(4, 3, -1))
print(quartic_equation(1, 10, 9))
print(quartic_equation(4, -11, 6))
print(quartic_equation(6, 19, -7))
print(quartic_equation(9, -4, 0))
print(quartic_equation(1, 1, 0))
