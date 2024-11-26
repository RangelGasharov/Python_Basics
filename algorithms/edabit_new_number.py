def is_new(number):
    number_string = str(number)
    if len(number_string) == 1:
        return True
    if len(number_string) == 2:
        return (number_string[1] > number_string[0]) or (number_string[1] == "0")
    i, j = 0, 1
    while j < len(number_string):
        if number_string[j - 1] != "0":
            i = j - 1
        if number_string[j] == "0":
            if number_string[j - 1] != "0" and number_string[j + 1] != "0" and j - 1 != 0 and len(number_string) > 3:
                return False
        if int(number_string[j]) < int(number_string[i]) and number_string[j] != "0":
            return False
        j += 1
    return True


print("True values")
print(is_new(0))
print(is_new(90))
print(is_new(102))
print(is_new(123))
print(is_new(40567))
print(is_new(30004))
print(is_new(4444))
print("False values")
print(is_new(321))
print(is_new(601))
print(is_new(10783))
print(is_new(23401))
print(is_new(125609))
print(is_new(40003))
