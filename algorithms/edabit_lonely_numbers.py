def get_string_with_number_groups(num):
    text = str(num)
    result_string = ""
    current_digit = text[0]
    start_index = 0
    end_index = -1
    for i in range(1, len(text)):
        if text[i] != current_digit:
            end_index = i
            if end_index - start_index <= 1:
                result_string += 3 * current_digit
            else:
                result_string += text[start_index:end_index]
            current_digit = text[i]
            start_index = i
    if end_index == -1:
        if len(text) >= 2:
            return int(text)
        else:
            return int(3 * current_digit)
    if len(text) - 1 - start_index < 1:
        result_string += 2 * text[-1]
    result_string += text[start_index:len(text)]
    return int(result_string)


print(get_string_with_number_groups(2))
print(get_string_with_number_groups(22))
print(get_string_with_number_groups(222))
print(get_string_with_number_groups(22733))
print(get_string_with_number_groups(4666))
print(get_string_with_number_groups(544))
print(get_string_with_number_groups(123))
print(get_string_with_number_groups(56657))
