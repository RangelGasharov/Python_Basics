def remove_leading_trailing(number_as_string):
    index_first_non_zero_integer = -1
    index_last_non_zero_integer = -1
    index_comma = -1
    for i in range(len(number_as_string)):
        if number_as_string[i] != "0":
            if number_as_string[i] == ".":
                index_comma = i
            else:
                index_last_non_zero_integer = i
    for i in range(len(number_as_string)):
        if number_as_string[i] != "0":
            if number_as_string[i] != ".":
                index_first_non_zero_integer = i
                break
    # print(index_first_non_zero_integer, index_last_non_zero_integer, index_comma)
    if index_first_non_zero_integer == -1 and index_last_non_zero_integer == -1:
        return "0"
    if index_first_non_zero_integer > index_comma:
        if index_comma < 0:
            return number_as_string[index_first_non_zero_integer:]
        else:
            return number_as_string[index_comma - 1:index_last_non_zero_integer + 1]
    if index_last_non_zero_integer > index_comma:
        return number_as_string[index_first_non_zero_integer:index_last_non_zero_integer + 1]
    else:
        return number_as_string[index_first_non_zero_integer:index_comma]


print(remove_leading_trailing("0.000000"))
print(remove_leading_trailing("000"))
print(remove_leading_trailing("00.0001"))
print(remove_leading_trailing("00402"))
print(remove_leading_trailing("0404040"))
print(remove_leading_trailing("00420.000"))
print(remove_leading_trailing("230.000"))
print(remove_leading_trailing("30.0000"))
print(remove_leading_trailing("30"))
print(remove_leading_trailing("03.1400"))
print(remove_leading_trailing("00200.1900001"))
print(remove_leading_trailing("1345"))
print(remove_leading_trailing("30.000020"))
