import math


def function_y_1(x):
    return 1 / 5 * x ** 5 - 4 * x ** 4 + 3 * x ** 3 + 5 * x ** 2 - 3 * x + 10


def function_y_first_derivative_1(x):
    return x ** 4 - 16 * x ** 3 + 9 * x ** 2 + 10 * x - 3


def function_y_2(x):
    return x ** 5 - 4 * x ** 4 + 3 * x ** 3 + 5 * x ** 2 - 3 * x + 10


def function_y_first_derivative_2(x):
    return 5 * x ** 4 - 16 * x ** 3 + 9 * x ** 2 + 10 * x - 3


def function_y_3(x):
    return x ** 2 - 4


def function_y_first_derivative_3(x):
    return 2 * x


def function_y_4(x):
    return math.sin(x)


def function_y_first_derivative_4(x):
    return math.cos(x)


def find_zero_point(x, function, function_derivative):
    for i in range(1, 100):
        gradient_tangent = function_derivative(x)
        value_function = function(x)
        value_tangent = gradient_tangent * x
        displacement_y_axis = value_function - value_tangent
        try:
            x = -displacement_y_axis / gradient_tangent
        except ZeroDivisionError:
            return round(x, 10)
    return round(x, 10)


print("Function 1")
print(f"Zero point of function: x = {find_zero_point(1, function_y_1, function_y_first_derivative_1)}")
print(function_y_1(find_zero_point(1, function_y_1, function_y_first_derivative_1)))
print(f"Zero point of function: x = {find_zero_point(100, function_y_1, function_y_first_derivative_1)}")
print(function_y_1(find_zero_point(1, function_y_1, function_y_first_derivative_1)), "\n")

print("Function 2")
print(f"Zero point of function: x = {find_zero_point(1, function_y_2, function_y_first_derivative_2)}")
print(function_y_2(find_zero_point(1, function_y_2, function_y_first_derivative_2)), "\n")

print("Function 3")
print(f"Zero point of function: x = {find_zero_point(1, function_y_3, function_y_first_derivative_3)}")
print(function_y_3(find_zero_point(1, function_y_3, function_y_first_derivative_3)))
print(f"Zero point of function: x = {find_zero_point(-4, function_y_3, function_y_first_derivative_3)}")
print(function_y_3(find_zero_point(1, function_y_3, function_y_first_derivative_3)), "\n")

print("Function 4")
print(f"Zero point of function: x = {find_zero_point(1, function_y_4, function_y_first_derivative_4)}")
print(function_y_4(find_zero_point(1, function_y_4, function_y_first_derivative_4)))
print(f"Zero point of function: x = {find_zero_point(4, function_y_4, function_y_first_derivative_4)}")
print(function_y_4(find_zero_point(1, function_y_4, function_y_first_derivative_4)), "\n")
