def shift_sentence(text):
    words = separate_words(text)
    shifted_words = shift_letters(words)
    sentence = build_sentence(shifted_words)
    return sentence


def build_sentence(words):
    sentence = ""
    for i in range(0, len(words) - 1):
        sentence += words[i] + " "
    sentence += words[-1]
    return sentence


def shift_letters(words):
    new_words = []
    for i in range(-1, len(words) - 1):
        previous_word = words[i]
        current_word = words[i + 1]
        new_word = current_word.replace(current_word[0], previous_word[0])
        new_words.append(new_word)
    return new_words


def separate_words(text):
    words = []
    current_word = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            words.append(current_word)
            current_word = ""
        elif i == len(text) - 1:
            current_word += text[i]
            words.append(current_word)
        else:
            current_word += text[i]
    return words


print(shift_sentence("create a function"))
print(shift_sentence("it should shift the sentence"))
print(shift_sentence("the output is not very legible"))
print(shift_sentence("edabit"))
