def moran(number):
    if number % get_digits_sum(number) != 0:
        return "Neither"
    if is_prime(number // get_digits_sum(number)):
        return "M"
    return "H"


def get_digits_sum(number):
    number_string = str(number)
    digits_sum = 0
    for i in range(len(number_string)):
        digits_sum += int(number_string[i])
    return digits_sum


def is_prime(number):
    for i in range(2, int(number ** (1 / 2) + 1) + 1):
        if number % i == 0:
            return False
    return True


print(moran(3030))
print(moran(132))
print(moran(133))
print(moran(3033))
print(moran(20937))
print(moran(134))
print(moran(491423))

