def sort_by_last(text):
    if len(text) < 1:
        return ""
    words = separate_words(text)
    words.sort(key=lambda x: x[-1])
    text = build_text(words)
    return text


def separate_words(text):
    separated_words = []
    current_word = ""
    for i in range(len(text)):
        if text[i] == " ":
            separated_words.append(current_word)
            current_word = ""
        else:
            current_word += text[i]
    separated_words.append(current_word)
    return separated_words


def build_text(words):
    text = ""
    for i in range(len(words) - 1):
        text += words[i] + " "
    text += words[-1]
    return text


print(sort_by_last("herb camera dynamic"))
print(sort_by_last("stab traction artist approach"))
print(sort_by_last("sample partner autonomy swallow trend"))
print(sort_by_last("brick moral institution loud talk resign worth"))
print(sort_by_last("card warrant opinion medium illustrate"))
print(sort_by_last(""))
