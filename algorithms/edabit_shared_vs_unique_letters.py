def compare_words(word1, word2):
    set1 = set(word1)
    set2 = set(word2)

    shared = set1 & set2
    unique_word1 = set1 - set2
    unique_word2 = set2 - set1

    shared_sorted = sorted(shared)
    unique_word1_sorted = sorted(unique_word1)
    unique_word2_sorted = sorted(unique_word2)

    return ["".join(shared_sorted), "".join(unique_word1_sorted), "".join(unique_word2_sorted)]


print(compare_words("sharp", "soap"))
print(compare_words("board", "bored"))
print(compare_words("happiness", "envelope"))
print(compare_words("kerfuffle", "fluffy"))