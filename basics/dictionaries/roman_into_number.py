s = input("Write down the roman number you want to translate.\n")


def roman_into_integer(s):
    roman_digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    for i in s:
        if i in roman_digits:
            value += roman_digits[i]

    if "IV" in s:
        value -= 2
    if "IX" in s:
        value -= 2
    if "XL" in s:
        value -= 20
    if "XC" in s:
        value -= 20
    if "CD" in s:
        value -= 200
    if "CM" in s:
        value -= 200

    return value


print(roman_into_integer(s))
