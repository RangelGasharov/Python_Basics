def count_lone_ones(number):
    number_string = str(number)
    amount_of_lone_ones = 0
    if len(number_string) == 1:
        return 1 * (number_string[0] == "1")
    for i in range(1, len(number_string) - 1):
        if number_string[i] == "1":
            if number_string[i] != number_string[i - 1] and number_string[i] != number_string[i + 1]:
                amount_of_lone_ones += 1
    amount_of_lone_ones += (number_string[0] == "1" and number_string[1] != "1")
    amount_of_lone_ones += (number_string[-1] == "1" and number_string[-2] != "1")
    return amount_of_lone_ones


print(count_lone_ones(1))
print(count_lone_ones(0))
print(count_lone_ones(101))
print(count_lone_ones(1191))
print(count_lone_ones(11101))
print(count_lone_ones(1111))
print(count_lone_ones(462))
print(count_lone_ones(12131415161718191))
print(count_lone_ones(11231212111))
