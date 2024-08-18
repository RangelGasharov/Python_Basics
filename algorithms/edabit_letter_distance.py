def letter_distance(word1, word2):
    result = 0
    shorter_length = len(word1) * (len(word1) <= len(word2)) + len(word2) * (len(word2) < len(word1))
    for i in range(shorter_length):
        result += abs(ord(word1[i]) - ord(word2[i]))
    result += abs(len(word1) - len(word2))
    return result


print(letter_distance("house", "fly"))
print(letter_distance("sharp", "sharq"))
print(letter_distance("abcde", "Abcde"))
print(letter_distance("abcde", "bcdef"))
print(letter_distance('abcde', 'A'))
print(letter_distance('very', 'fragile'))
