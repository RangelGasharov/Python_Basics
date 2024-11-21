def title_to_number(column_string):
    column_number = 0
    alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                "X": 24, "Y": 25, "Z": 26}
    for i in range(len(column_string)):
        column_number += alphabet[column_string[i]] * len(alphabet) ** (len(column_string) - i - 1)
    return column_number


print(title_to_number("A"))
print(title_to_number("Z"))
print(title_to_number("AB"))
print(title_to_number("WEB"))
print(title_to_number("FRIENDS"))
