def word_to_decimal(word):
    sum_word = 0
    highest_letter_index = get_highest_letter(word)
    base = highest_letter_index + 10
    for i, letter in enumerate(word):
        letter_index = get_letter_index(letter)
        sum_word += (10 + letter_index - 1) * base ** (len(word) - i - 1)
    return sum_word


def get_highest_letter(word):
    current_highest = -1
    for i in range(len(word)):
        current_index = get_letter_index(word[i])
        if current_index > current_highest:
            current_highest = current_index
    return current_highest


def get_letter_index(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if letter.lower() == alphabet[i]:
            return i + 1
    return -1


print(word_to_decimal("Edabit"))
print(word_to_decimal("Python"))
print(word_to_decimal("ZERO"))
print(word_to_decimal("eigHt"))
print(word_to_decimal("fIVe"))
