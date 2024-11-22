def num_split(number):
    numbers = []
    number_string = str(number)
    is_negative = False
    if number_string[0] == "-":
        is_negative = True
    for i in range(0 + 1 * is_negative, len(number_string)):
        numbers.append(int(number_string[i]) * 10 ** (len(number_string) - i - 1) * (-1 if is_negative else 1))
    return numbers


print(num_split(39))
print(num_split(-434))
print(num_split(100))
print(num_split(-100))
print(num_split(10293))
print(num_split(3929))
