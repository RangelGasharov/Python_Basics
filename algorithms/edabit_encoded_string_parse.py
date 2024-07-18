def parse_code(string):
    words = get_separated_words(string)
    dictionary_of_words = get_dictionary(words)
    return dictionary_of_words


def get_separated_words(string):
    separated_words = []
    current_word = ""
    for i in range(0, len(string)):
        if string[i] == "0":
            if current_word != "":
                separated_words.append(current_word)
            else:
                continue
            current_word = ""
        elif i == len(string) - 1:
            current_word += string[i]
            separated_words.append(current_word)
        else:
            current_word += string[i]
    return separated_words


def get_dictionary(words):
    return {
        "first_name": words[0],
        "last_name": words[1],
        "id": words[2]
    }


print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
print(parse_code("Thomas0000Lee0000045553"))
