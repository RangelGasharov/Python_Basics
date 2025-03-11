def grouping(words):
    groups = {}
    for i in range(len(words)):
        key = get_amount_of_capital_letters(words[i])
        if key not in groups:
            groups[key] = [words[i]]
        else:
            groups[key].append(words[i])
    return groups


def get_amount_of_capital_letters(word):
    amount_capital_letters = 0
    for i in range(len(word)):
        if word[i].isupper():
            amount_capital_letters += 1
    return amount_capital_letters


print(grouping(["MOVIE", "BAKE", "TAKE", "PERSON"]))
print(grouping(["the", "them", "theme", "EVERY"]))
print(grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]))
