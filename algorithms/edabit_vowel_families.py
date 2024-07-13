def same_vowel_group(word_list):
    vowels_to_compare = get_vowels(word_list[0])
    words_with_same_vowels = [word_list[0]]
    for i in range(1, len(word_list)):
        if has_same_vowels(vowels_to_compare, word_list[i]):
            words_with_same_vowels.append(word_list[i])
    return words_with_same_vowels


def get_vowels(word):
    word = set(word)
    vowels_of_word = []
    vowels = ["a", "e", "i", "o", "u"]
    for x in word:
        if x in vowels:
            vowels_of_word.append(x)
    return vowels_of_word


def has_same_vowels(vowels_to_compare, word):
    vowels_list = get_vowels(word)
    for x in vowels_list:
        if x not in vowels_to_compare:
            return False
    for x in vowels_to_compare:
        if x not in vowels_list:
            return False
    return True


print(same_vowel_group(["toe", "ocelot", "maniac"]))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))
print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))
print(same_vowel_group(["a", "apple", "flat", "map", "shark"]))
