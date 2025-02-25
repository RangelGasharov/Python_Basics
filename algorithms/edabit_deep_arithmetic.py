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
            numbers_sum += deep_sum_recursive(array[i], numbers_sum)
        else:
            numbers_sum += get_number_sum_in_string(array[i])
    return numbers_sum


def get_number_sum_in_string(string):
    numbers_sum = 0
    current_number = ""

    for i, char in enumerate(string):
        if char.isdigit() or (char == "-" and current_number == ""):
            current_number += char
        else:
            if current_number and current_number not in ["-", "+"]:
                numbers_sum += int(current_number)
            current_number = "-" if char == "-" else ""

    if current_number and current_number not in ["-", "+"]:
        numbers_sum += int(current_number)

    return numbers_sum


print(deep_sum(["1", "five", "2wenty", "thr33"]))
print(deep_sum([["1X2", "t3n"], ["1024", "5", "64"]]))
print(deep_sum([[["1"], "10v3"], ["738h"], [["s0"], ["1mu4ch3"], "-1s0"]]))
print(deep_sum(
    [[["0", "0x2", "z3r1"], ["1", "55a46"]], [["1", "0b2", "4"], ["0x5fp-2", "nine", "09"], ["4", "4", "4"]], [["03"]],
     []]))
print(deep_sum([[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]))
print(deep_sum([[[[[["-32-64", "a-zA-Z"], ["01-1"]]]]]]))
