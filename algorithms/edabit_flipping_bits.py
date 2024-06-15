def flipping_bits(num):
    num_binary = decimal_to_binary(num, 32)
    num_binary_flipped = flip_binary_number(num_binary)
    return binary_to_decimal(num_binary_flipped)


def flip_binary_number(binary_num):
    num_binary_flipped = ""
    for x in binary_num:
        if x == "1":
            num_binary_flipped += "0"
        else:
            num_binary_flipped += "1"
    return num_binary_flipped


def decimal_to_binary(num, length):
    current_rest = num
    binary_number_as_string = ""
    for i in reversed(range(length)):
        if current_rest >= 2 ** i:
            current_rest -= 2 ** i
            binary_number_as_string += "1"
        else:
            binary_number_as_string += "0"
    return binary_number_as_string


def binary_to_decimal(binary_num):
    current_num = 0
    length_num = len(binary_num)
    for index, x in enumerate(binary_num):
        if x == "1":
            current_num += 2 ** (length_num - index - 1)
    return current_num


print(flipping_bits(2147483647))
print(flipping_bits(1))
print(flipping_bits(4))
