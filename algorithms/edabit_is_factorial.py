def is_factorial(number):
    current_factorial = 1
    current_index = 1
    while current_factorial < number:
        current_factorial *= current_index
        current_index += 1
    return number == current_factorial


print(is_factorial(1))
print(is_factorial(2))
print(is_factorial(24))
print(is_factorial(27))
print(is_factorial(720))
print(is_factorial(721))
print(is_factorial(362880))
print(is_factorial(1307674368000))
