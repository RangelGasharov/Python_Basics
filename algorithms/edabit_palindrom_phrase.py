def is_palindrome(sentence):
    separated_words = separate_words(sentence)
    sentence_string = build_sentence_string(separated_words)
    return False


def separate_words(sentence):
    special_characters = [",", ".", "?", "!", "'", " "]
    words = []
    current_word = ""
    for i in range(0, len(sentence)):
        if sentence[i] in special_characters:
            if current_word != "" and current_word not in special_characters:
                words.append(current_word)
            current_word = ""
            continue
        if i == len(sentence) - 1:
            if sentence[i] not in special_characters:
                current_word += sentence[i]
                words.append(current_word)
        else:
            current_word += sentence[i]
    return words


def build_sentence_string(words):
    sentence = ""
    for i in range(0, len(words)):
        sentence += words[i]
    return sentence


print(build_sentence_string(separate_words("Eva, can I see bees in a cave?")))
