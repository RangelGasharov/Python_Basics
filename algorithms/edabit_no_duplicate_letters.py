def no_duplicate_letters(text):
    words = separate_words(text)
    for x in words:
        if check_duplicate_letter(x):
            return False
    return True


def separate_words(text):
    words = []
    current_word = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            words.append(current_word)
            current_word = ""
        if i == len(text) - 1:
            current_word += text[i]
            words.append(current_word)
        current_word += text[i]
    return words


def check_duplicate_letter(word):
    word_sorted = sorted(word)
    for i in range(0, len(word_sorted) - 1):
        if word_sorted[i] == word_sorted[i + 1]:
            return True
    return False


print(no_duplicate_letters("Fortune favours the bold."))
print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap."))
print(no_duplicate_letters("An apple a day keeps the doctor away."))
