import math


def fractions(number_string):
    index_decimal_point = number_string.index(".")
    index_start_repeating = number_string.index("(")
    index_end_repeating = number_string.index(")")

    integer_of_number = int(number_string[:index_decimal_point])
    non_repeating_decimal = number_string[index_decimal_point + 1:index_start_repeating]
    repeating_part = number_string[index_start_repeating + 1:index_end_repeating]

    len_non_repeating = len(non_repeating_decimal)
    len_repeating = len(repeating_part)

    if len_non_repeating > 0:
        non_repeating_value = int(non_repeating_decimal)
        repeating_value = int(f"{non_repeating_decimal}{repeating_part}")
    else:
        non_repeating_value = 0
        repeating_value = int(repeating_part)

    numerator = (integer_of_number * (10 ** (len_non_repeating + len_repeating) - 10 ** len_non_repeating)
                 + (repeating_value - non_repeating_value))
    denominator = 10 ** (len_non_repeating + len_repeating) - 10 ** len_non_repeating
    result = simplify_fraction(numerator, denominator)
    return result


def simplify_fraction(numerator, denominator):
    divisor = math.gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor
    return f"{numerator}/{denominator}"


print(fractions("0.(6)"))
print(fractions("1.(1)"))
print(fractions("3.(142857)"))
print(fractions("0.19(2367)"))
print(fractions("0.(09)"))
print(fractions("0.0(45)"))
print(fractions("2.1(313)"))
print(fractions("0.0208(3)"))
print(fractions("12.(12345)"))
print(fractions("1.017(857142)"))
print(fractions("0.(052631578947368421)"))
print(fractions("0.1097(3)"))
print(fractions("4.5(678)"))
