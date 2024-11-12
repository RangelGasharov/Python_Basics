def sum_complex(complex_numbers):
    sum_real_part = 0
    sum_complex_part = 0
    for complex_number in complex_numbers:
        separated_complex_number = split_up_complex_number(complex_number)
        sum_real_part += separated_complex_number[0]
        sum_complex_part += separated_complex_number[1]
    result_string = ""
    result_string += str(sum_real_part) * (sum_real_part != 0)
    result_string += "+" * (sum_complex_part > 0 and sum_real_part != 0) + (str(sum_complex_part) + "i") * (
                sum_complex_part not in [0, 1, -1])
    result_string += ("-" * (sum_complex_part < 0) + str(sum_complex_part)[2:] + "i") * (sum_complex_part in [1, -1])
    result_string += "0" * (sum_real_part == 0 and sum_complex_part == 0)
    return result_string


def split_up_complex_number(complex_number):
    real_part = 0
    complex_part = 0
    indexes_signs = []
    index_imaginary_unit = -1
    for i in range(len(complex_number)):
        if complex_number[i] in ["+", "-"]:
            indexes_signs.append(i)
        if complex_number[i] == "i":
            index_imaginary_unit = i
    if len(indexes_signs) > 1:
        end_real = indexes_signs[1]
        real_part = int(complex_number[0:end_real])
        complex_part = int(complex_number[end_real:-1] + "1" * (len(complex_number[end_real:-1]) == 1))
        return [real_part, complex_part]
    elif len(indexes_signs) == 0:
        if index_imaginary_unit > -1:
            if index_imaginary_unit == 0:
                return [0, 1]
            return [0, int(complex_number[:-1])]
        else:
            return [int(complex_number), complex_part]
    else:
        if indexes_signs[0] > 0:
            end_real = indexes_signs[0]
            real_part = int(complex_number[0:end_real])
            complex_part = int(complex_number[end_real:-1] + "1" * (len(complex_number[end_real:-1]) == 1))
            return [real_part, complex_part]
        else:
            if index_imaginary_unit > -1:
                if indexes_signs[0] == len(complex_number) - 2:
                    return [0, int(complex_number[0] + "1")]
                else:
                    return [0, int(complex_number[:-1])]
            else:
                end_real = len(complex_number)
                real_part = int(complex_number[0:end_real])
                return [real_part, complex_part]


print(sum_complex(["2+3i", "3-i"]))
print(sum_complex(["1", "1"]))
print(sum_complex(["0"]))
print(sum_complex(["i", "2i", "3i"]))
print(sum_complex(["-i"]))
print(sum_complex(["-5", "5"]))
print(sum_complex(["1", "10", "100", "1000"]))
print(sum_complex(["3+4i", "3-4i"]))
print(sum_complex(["2+i", "3+2i", "-5-2i"]))
print(sum_complex(["-1000i", "1000i", "1234"]))
