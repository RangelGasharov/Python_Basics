def compress(char_list):
    result = ""
    current_amount = 1
    for i in range(1, len(char_list)):
        if char_list[i] == char_list[i - 1]:
            current_amount += 1
        else:
            if current_amount == 1:
                result += char_list[i - 1]
            else:
                result += char_list[i - 1] + str(current_amount)
            current_amount = 1
    result += char_list[-1] + (current_amount > 1) * str(current_amount)
    return result


print(compress(["t", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "s", "s", "s", "h"]))
print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(compress(["a", "a", "a", "b", "b", "a", "a"]))
