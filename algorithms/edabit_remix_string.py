def remix(word, indexes):
    if len(word) != len(indexes):
        return ""
    word_array = [""] * len(indexes)
    for i in range(len(indexes)):
        word_array[indexes[i]] = word[i]
    return "".join(word_array)


print(remix("PlOt", [1, 3, 0, 2]))
print(remix("computer", [0, 2, 1, 5, 3, 6, 7, 4]))
print(remix("abcd", [0, 3, 1, 2]))
print(remix("sequence", [5, 7, 3, 4, 0, 1, 2, 6]))
print(remix("Interference", [6, 9, 10, 11, 7, 3, 0, 2, 5, 1, 8, 4]))
