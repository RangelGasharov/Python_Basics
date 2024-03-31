def decimal_to_binary(decimal):
    if decimal == 0:
        return 0
    else:
        return decimal % 2 + 10 * decimal_to_binary(int(decimal // 2))


print(decimal_to_binary(10))
print(decimal_to_binary(100))
print(decimal_to_binary(30000000))