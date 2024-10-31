def arrow(num):
    resulting_strings = []
    for i in range(1, num + 1):
        arrow_string = ">" * i
        resulting_strings.append(arrow_string)
    for i in range(1, num):
        arrow_string = (num - i) * ">"
        resulting_strings.append(arrow_string)
    return resulting_strings


def print_arrows(text_strings):
    for text in text_strings:
        print(text)


print_arrows(arrow(3))
print_arrows(arrow(4))
print_arrows(arrow(5))
