def sum_complex(complex_numbers):
    return 0


def split_up_complex_number(complex_number):
    real_part = 0
    complex_part = 0
    indexes_signs = []
    index_imaginary_unit = -1
    end_real = -1
    for i in range(len(complex_number)):
        if complex_number[i] in ["+", "-"]:
            indexes_signs.append(i)
        if complex_number[i] == "i":
            index_imaginary_unit = i
    if len(indexes_signs) > 1:
        end_real = indexes_signs[1]
        real_part = int(complex_number[0:end_real])
        complex_part = int(complex_number[end_real + 1:-2])
        return [real_part, complex_part]
    else:
        if indexes_signs[0] > 0:
            end_real = indexes_signs[0]
            real_part = int(complex_number[0:end_real])
            complex_part = int(complex_number[end_real + 1:-1])
            return [real_part, complex_part]
        else:
            if index_imaginary_unit > -1:
                if indexes_signs[0] == len(complex_number) - 2:
                    return [0, int(complex_number[0] + "1")]
                else:
                    return [0, int(complex_number[:-1])]
            else:
                end_real = len(complex_number)
    return [real_part, complex_part]


print(split_up_complex_number("2+2i"))
print(split_up_complex_number("+2i"))
print(split_up_complex_number("-2"))
