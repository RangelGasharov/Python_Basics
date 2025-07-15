def is_valid(word):
    word_length = len(word)
    if word_length < 3:
        return False
    vowels = ["a", "e", "i", "o", "u"]
    amount_of_vowels = 0
    for i in range(len(word)):
        if word[i].lower() in vowels:
            amount_of_vowels += 1
        if not word[i].isalnum():
            return False
    if word_length - amount_of_vowels < 1:
        return False
    return True


print(is_valid("234Adas"))
print(is_valid("test"))
print(is_valid("to"))
print(is_valid("b3"))
print(is_valid("a3$e"))
