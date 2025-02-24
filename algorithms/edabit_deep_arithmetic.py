def deep_sum(array):
    numbers_sum = 0
    for i in range(len(array)):
        if isinstance(array[i], list):
            sum_in_sub_array = deep_sum_recursive(array[i], 0)
            numbers_sum += sum_in_sub_array
        else:
            numbers_sum += get_number_sum_in_string(array[i])
    return numbers_sum


def deep_sum_recursive(array, current_sum):
    numbers_sum = 0
    for i in range(len(array)):
        if isinstance(array[i], list):
            numbers_sum = deep_sum_recursive(array[i], numbers_sum)
        else:
            numbers_sum += get_number_sum_in_string(array[i])
    return numbers_sum


def get_number_sum_in_string(string):
    numbers_sum = 0
    numbers_strings = []
    current_number = ""
    for i in range(0, len(string)):
        if not string[i].isnumeric():
            if current_number != "":
                numbers_strings.append(current_number)
            current_number = ""
        else:
            current_number += string[i]
    if current_number.isnumeric():
        numbers_strings.append(current_number)
    for i in range(len(numbers_strings)):
        numbers_sum += int(numbers_strings[i])
    return numbers_sum


print(get_number_sum_in_string("1e3e2"))
print(deep_sum(["1", "five", "2wenty", "thr33"]))
print(deep_sum(["1", "five", ["2wenty", "thr33"]]))
print(deep_sum(["1", "five", ["2wenty", ["thr33"]]]))