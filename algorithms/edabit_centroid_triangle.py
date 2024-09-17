def is_polydivisible(number):
    number_as_string = str(number)
    for i in range(1, len(number_as_string)):
        if int(number_as_string[:i]) / i % 1 != 0:
            return False
    return True


print(is_polydivisible(0))
print(is_polydivisible(1))
print(is_polydivisible(1232))
print(is_polydivisible(123220))
print(is_polydivisible(9876545))
print(is_polydivisible(381654729))
print(is_polydivisible(1073741823))
