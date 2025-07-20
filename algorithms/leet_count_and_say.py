def count_and_say(number):
    result = "1"
    for i in range(2, number + 1):
        result = get_rle(result)
    return result


def get_rle(number_string):
    result = ""
    current_digit = number_string[0]
    amount_of_current_digit = 1
    for i in range(1, len(number_string)):
        if number_string[i] != current_digit:
            result += f"{amount_of_current_digit}{current_digit}"
            current_digit = number_string[i]
            amount_of_current_digit = 1
        else:
            amount_of_current_digit += 1
    result += f"{amount_of_current_digit}{current_digit}"
    return result


print(count_and_say(1))
print(count_and_say(2))
print(count_and_say(3))
print(count_and_say(4))
print(count_and_say(5))
print(count_and_say(10))
print(count_and_say(15))
print(count_and_say(20))
