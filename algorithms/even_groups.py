def split_integer(number, parts):
    quotient, remainder = divmod(number, parts)
    base_parts_count = parts - remainder
    base_parts = base_parts_count * [quotient]
    extra_parts = remainder * [quotient + 1]
    return base_parts + extra_parts


print(split_integer(3, 4))
print(split_integer(9, 4))
print(split_integer(10, 4))
print(split_integer(11, 4))
print(split_integer(1000, 8))
print(split_integer(1000, 3))
