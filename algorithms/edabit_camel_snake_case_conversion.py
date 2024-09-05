def to_camel_case(text):
    separated_words = separate_snake_case(text)
    result = separated_words[0]
    for i in range(1, len(separated_words)):
        result += separated_words[i].capitalize()
    return result


def to_snake_case(text):
    separated_words = separate_camel_case(text)
    result = ""
    for i in range(0, len(separated_words) - 1):
        result += separated_words[i] +  "_"
    result += separated_words[-1]
    return result


def separate_camel_case(text):
    result = []
    current_word = ""
    for char in text:
        if char.isupper():
            result.append(current_word)
            current_word = char.lower()
        else:
            current_word += char
    result.append(current_word)
    return result


def separate_snake_case(text):
    result = []
    current_word = ""
    for char in text:
        if char == "_":
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    result.append(current_word)
    return result


print(to_camel_case("hello_edabit"))
print(to_camel_case("is_modal_open"))
print(to_camel_case("get_background_color"))
print(to_camel_case("x"))
print(to_snake_case("helloEdabit"))
print(to_snake_case("getBackgroundColor"))
print(to_snake_case("getColor"))
print(to_snake_case("x"))
