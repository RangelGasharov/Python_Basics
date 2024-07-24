def is_palindrome(sentence):
    separated_words = separate_words(sentence)
    sentence_string = build_sentence_string(separated_words)
    result = is_palindrome_recursive(sentence_string)
    return result


def is_palindrome_recursive(text):
    if len(text) == 0 or len(text) == 1:
        return True
    if text[0].lower() == text[len(text) - 1].lower():
        return is_palindrome(text[1:len(text) - 1])
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


print(is_palindrome("Eva, can I see bees in a cave?"))
print(is_palindrome("Go hang a salami, I'm a lasagna hog!"))
print(is_palindrome("This phrase, surely, is not a palindrome!"))
print(is_palindrome("Maneuquenam"))
