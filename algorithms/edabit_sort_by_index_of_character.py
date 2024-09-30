def sort_by_character(words, index_character):
    words.sort(key=lambda x: x[index_character - 1])
    return words


print(sort_by_character(["az16", "by35", "cx24"], 1))
print(sort_by_character(["az16", "by35", "cx24"], 2))
print(sort_by_character(["az16", "by35", "cx24"], 3))
print(sort_by_character(["az16", "by35", "cx24"], 4))
print(sort_by_character(["mayor", "apple", "petal"], 5))
print(sort_by_character(["mate", "team", "bade"], 3))
