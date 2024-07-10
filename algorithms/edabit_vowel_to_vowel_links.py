def vowel_links(txt):
    words = separate_words(txt)
    result = check_vowel_links(words)
    return result


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


def check_vowel_links(words):
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(0, len(words) - 1):
        if words[i][-1] in vowels and words[i + 1][0] in vowels:
            return True
    return False


print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
print(vowel_links("a sudden applause"))
print(vowel_links("another day is over"))
print(vowel_links("a desperate attempt"))
