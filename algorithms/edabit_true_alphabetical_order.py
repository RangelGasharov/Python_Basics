def true_alphabetic(sentence):
    separated_words = separate_words(sentence)
    word_lengths = [len(string) for string in separated_words]
    separated_words_string = "".join(separated_words)
    separated_words_chars = [char for char in separated_words_string]
    separated_words_chars.sort()
    sorted_words = []
    current_index = 0
    for length in word_lengths:
        sorted_words.append(separated_words_chars[current_index:current_index + length])
        current_index += length
    result = ""
    for word in sorted_words:
        result += "".join(word) + " "
    result = result[:-1]
    return result


def separate_words(sentence):
    separated_words = []
    current_word = ""
    for character in sentence:
        if character == " ":
            if current_word != "":
                separated_words.append(current_word)
            current_word = ""
        else:
            current_word += character
    if current_word != "":
        separated_words.append(current_word)
    return separated_words


print(true_alphabetic("hello world"))
print(true_alphabetic("edabit is awesome"))
print(true_alphabetic("have a nice day"))
print(true_alphabetic("joshua senoron"))
