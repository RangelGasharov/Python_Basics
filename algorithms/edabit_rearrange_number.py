def rearranged_difference(number):
    highest_number = get_highest_number(number)
    lowest_number = get_lowest_number(number)
    return highest_number - lowest_number


def get_number(number, is_highest):
    number_array = []
    for digit in str(number):
        number_array.append(digit)
    number_array.sort(reverse=is_highest)
    number_string = ""
    for digit in number_array:
        number_string += digit
    return int(number_string)


def get_highest_number(number):
    return get_number(number, True)


def get_lowest_number(number):
    return get_number(number, False)


print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
print(rearranged_difference(5155458))
