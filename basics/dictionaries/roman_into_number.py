s = input("Write down the roman number you want to translate.\n")
numberInArray = []


def roman_into_integer(s):
    roman_digits = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    for i in s:
        if i.upper() in roman_digits:
            numberInArray.append(roman_digits[i.upper()])
    for i in range(len(numberInArray)):
        value += numberInArray[i]
        if numberInArray[i] > numberInArray[i - 1] and i > 0:
            value -= 2 * numberInArray[i - 1]

    return value


print(roman_into_integer(s))
