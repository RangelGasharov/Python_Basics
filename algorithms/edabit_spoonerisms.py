def spoonerise(word_string):
    words = word_string.split()
    first_word = words[0]
    second_word = words[1]
    vowels = ["a", "o", "u", "e", "i"]
    index_first_word = -1
    index_second_word = -1
    for i in range(len(first_word)):
        if first_word[i] in vowels:
            index_first_word = i
            break
    for i in range(len(second_word)):
        if second_word[i] in vowels:
            index_second_word = i
            break
    result = f"{second_word[0:index_second_word]}{first_word[index_first_word:]} " \
             f"{first_word[0:index_first_word]}{second_word[index_second_word:]}"
    return result


print(spoonerise("history lecture"))
print(spoonerise("loud noises"))
print(spoonerise("chow mein"))
print(spoonerise("edabit rules!"))
print(spoonerise("chocolate biscuits"))
