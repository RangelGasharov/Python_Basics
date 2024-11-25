def is_new(number):
    number_string = str(number)
    i, j = 1, 0
    j = 0
    while i < len(number_string):
        if number_string[i] == "0":
            i += 1
            continue
        if int(number_string[i]) < int(number_string[i - 1]):
            return False
        j += 1
        i += 1
    return True


print(is_new(3))
print(is_new(30))
print(is_new(102))
print(is_new(123))
print(is_new(40567))
print(is_new(30004))
print(is_new(40003))
print(is_new(3000014))
print("False values")
print(is_new(321))
print(is_new(23401))
print(is_new(125609))
print(is_new(40003))
