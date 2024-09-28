def distance_to_nearest_vowel(word):
    vowels = ["a", "e", "i", "o", "u"]
    indexes_prior_vowel = []
    distances_nearest_vowel = []
    index_current_prior_vowel = ""
    for i in range(len(word)):
        if word[i] in vowels:
            indexes_prior_vowel.append(i)
            index_current_prior_vowel = i
        else:
            indexes_prior_vowel.append(index_current_prior_vowel)
    index_first_vowel = 0
    index_last_vowel = indexes_prior_vowel[-1]
    for i in range(len(indexes_prior_vowel)):
        if isinstance(indexes_prior_vowel[i], int):
            index_first_vowel = i
            break
    for j in range(index_first_vowel):
        indexes_prior_vowel[j] = index_first_vowel
    for i in range(len(indexes_prior_vowel)):
        distances_nearest_vowel.append(abs(i - indexes_prior_vowel[i]))
    for i in range(len(distances_nearest_vowel) - 1):
        if distances_nearest_vowel[i + 1] < distances_nearest_vowel[i] - 1:
            distances_nearest_vowel[i] = distances_nearest_vowel[i + 1] + 1
    for i in range(len(distances_nearest_vowel)):
        if distances_nearest_vowel[-i] < distances_nearest_vowel[-(i + 1)] and i > len(
                distances_nearest_vowel) - index_last_vowel - 1:
            distances_nearest_vowel[-(i + 1)] = distances_nearest_vowel[-i] + 1
    return distances_nearest_vowel


print(distance_to_nearest_vowel("aaaaa"))
print(distance_to_nearest_vowel("babbb"))
print(distance_to_nearest_vowel("abcdabcd"))
print(distance_to_nearest_vowel("shopper"))
print(distance_to_nearest_vowel("singingintherain"))
print(distance_to_nearest_vowel("treesandflowers"))
print(distance_to_nearest_vowel("beautiful"))
