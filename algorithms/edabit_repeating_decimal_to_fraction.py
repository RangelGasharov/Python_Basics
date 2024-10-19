def fractions(number_string):
    index_start_repeating = 0
    index_end_repeating = 0
    for i in range(len(number_string)):
        if number_string[i] == "(":
            index_start_repeating = i
        if number_string[i] == ")":
            index_end_repeating = i
    repeating_part = number_string[index_start_repeating + 1:index_end_repeating]
    return repeating_part


print(fractions("3.(142857)"))
