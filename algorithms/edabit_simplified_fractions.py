import math


def simplify(fraction_as_string):
    numbers = get_numbers(fraction_as_string)
    numerator = numbers[0]
    denominator = numbers[1]
    return simplify_fraction(numerator, denominator)


def get_numbers(string):
    numerator = 0
    denominator = 0
    for i in range(0, len(string)):
        if string[i] == "/":
            numerator = int(string[0:i])
            denominator = int(string[i + 1:len(string)])
    return [numerator, denominator]


def simplify_fraction(numerator, denominator):
    if numerator % denominator == 0:
        return int(numerator / denominator)
    if denominator % numerator == 0:
        return "1" + "/" + str(int((denominator / numerator)))
    border = numerator if numerator < denominator else denominator
    for i in range(2, round(math.sqrt(border)) + 1):
        if numerator % i == 0 and denominator % i == 0:
            numerator /= i
            denominator /= i
    return str(int(numerator)) + "/" + str(int(denominator))


print(simplify("3/4"))
print(simplify("10/11"))
print(simplify("100/400"))
print(simplify("8/4"))
print(simplify("4/4"))
