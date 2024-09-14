def shift_to_left(number, power):
    return number * get_power(2, power)


def get_power(number, power):
    if power == 0:
        return 1
    elif power == 1:
        return number
    number *= get_power(number, power - 1)
    return number


print(shift_to_left(5, 2))
print(shift_to_left(10, 3))
print(shift_to_left(-32, 2))
print(shift_to_left(-6, 5))
print(shift_to_left(12, 4))
print(shift_to_left(46, 6))
print(shift_to_left(57, 0))
print(shift_to_left(79, 1))
