alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def alphabet_index(alphabet, word):
    word_as_char_array = []
    for letter in word:
        word_as_char_array.append(letter.lower())
    word_as_char_array.sort()
    highest_letter = word_as_char_array[-1]
    result = ""
    for index, letter in enumerate(alphabet, start=0):
        if letter == highest_letter.lower():
            result = f"{index + 1}{highest_letter}"
    return result


print(alphabet_index(alphabet, "Xavier"))
print(alphabet_index(alphabet, "Tesha"))
print(alphabet_index(alphabet, "Flavio"))
print(alphabet_index(alphabet, "Andrey"))
print(alphabet_index(alphabet, "Oscar"))
print(alphabet_index(alphabet, "Hello"))
