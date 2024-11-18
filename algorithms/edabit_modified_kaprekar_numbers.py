def kaprekar_numbers(start, end):
    kaprekar_numbers = []
    for i in range(start, end + 1):
        if is_kaprekar_number(i):
            kaprekar_numbers.append(i)
    return get_string_by_numbers_list(kaprekar_numbers)


def is_kaprekar_number(number):
    len_number = len(str(number))
    number_squared = number * number
    number_squared_string = str(number_squared)
    first_number = 0
    if len(number_squared_string) > len_number:
        first_number = int(number_squared_string[:(len(number_squared_string) - len_number)])
    sum_numbers = first_number
    second_number = int(number_squared_string[(len(number_squared_string) - len_number):])
    if second_number == 0:
        return False
    sum_numbers += second_number
    return sum_numbers == number


def get_string_by_numbers_list(numbers_list):
    result_string = ""
    if len(numbers_list) < 1:
        return "INVALID RANGE"
    for i in range(len(numbers_list) - 1):
        result_string += f"{numbers_list[i]} "
    result_string += str(numbers_list[-1])
    return result_string


print(kaprekar_numbers(1, 100))
print(kaprekar_numbers(100, 300))
print(kaprekar_numbers(1, 99999))
print(kaprekar_numbers(1, 10))
print(kaprekar_numbers(2, 4))
