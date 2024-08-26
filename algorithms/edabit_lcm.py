def lcm(a, b):
    bigger_number = a * (a > b) + b * (b >= a)
    current_number = bigger_number
    while not (current_number % a == 0 and current_number % b == 0):
        current_number += bigger_number
    return current_number


print(lcm(9, 18))
print(lcm(8, 5))
print(lcm(17, 11))
print(lcm(17, 5))
print(lcm(3, 12))
print(lcm(9, 9))