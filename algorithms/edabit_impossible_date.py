def is_valid_date(day, month, year):
    amount_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12:
        return False
    if month == 2 and year % 4 == 0:
        amount_of_days[1] = 29
    if day > amount_of_days[month - 1]:
        return False
    return True


print(is_valid_date(29, 2, 2020))
print(is_valid_date(29, 2, 2019))
print(is_valid_date(8, 3, 2020))
print(is_valid_date(6, 15, 1969))
print(is_valid_date(35, 2, 2020))
print(is_valid_date(31, 6, 1980))

