def validate_swaps(list_of_strings, final_string):
    results = []
    for string in list_of_strings:
        if len(string) != len(final_string):
            results.append(False)
            continue
        indexes = []
        for i in range(len(string)):
            if string[i] != final_string[i]:
                indexes.append(i)
        if len(indexes) == 2:
            char_list = list(string)
            char_list[indexes[0]], char_list[indexes[1]] = char_list[indexes[1]], char_list[indexes[0]]
            new_string = "".join(char_list)
            if new_string == final_string:
                results.append(True)
            else:
                results.append(False)
        else:
            results.append(False)
    return results


print(validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE"))
print(validate_swaps(["32145", "12354", "15342", "12543"], "12345"))
print(validate_swaps(["9786", "9788", "97865", "7689"], "9768"))
print(validate_swaps(['123', '321', '132', '13', '12'], '213'))
print(validate_swaps(['123', '1234', '1235'], '12'))
print(validate_swaps(['123', '231', '123'], '133'))
print(validate_swaps(['132', '321', '213'], '123'))
