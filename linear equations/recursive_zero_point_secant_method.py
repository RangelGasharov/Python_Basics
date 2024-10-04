import math


def find_zero_point(function, amount_of_iterations=20, x0=1, x1=10):
    x2 = ""
    for i in range(amount_of_iterations):
        x2 = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
        x0, x1 = x1, x2
        if abs(x0 - x1) <= 0 or abs(x0 / x1 - 1) <= 0:
            break
    if abs(function(x2)) > 0.001:
        return "There is no zero point for the given function."
    return x2


def secant_function(slope, intercept, x):
    return slope * x + intercept


def function_1(x):
    return x ** 2 - 4


def function_2(x):
    return math.log(x)


def function_3(x):
    return x ** 2 + 1


def function_4(x):
    return math.sqrt(x) - 1


print(find_zero_point(function_1))
print(find_zero_point(function_2))
print(find_zero_point(function_3))
print(find_zero_point(function_4))
