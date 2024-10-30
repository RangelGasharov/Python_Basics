def wiggle_string(text):
    resulting_strings = []
    for i in range(len(text) + 1):
        offset_string = " " * i
        resulting_strings.append(offset_string + text)
    for i in range(1, len(text) + 1):
        offset_string = (len(text) - i) * " "
        resulting_strings.append(offset_string + text)
    return resulting_strings


def print_strings(text_strings):
    for text in text_strings:
        print(text)


print_strings(wiggle_string("hello"))
print_strings(wiggle_string("EDABIT"))
print_strings(wiggle_string("Wiggle Time"))
