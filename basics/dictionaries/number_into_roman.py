x = int(input("Write down the number which will be translated into a roman number.\n"))

roman_digits = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
                "CM": 900, "M": 1000}


def int_to_rome(x):
    roman_numeral = ""
    for i in reversed(roman_digits):
        while x >= roman_digits[i]:
            roman_numeral += i
            x -= roman_digits[i]
    return roman_numeral


print(int_to_rome(x))
