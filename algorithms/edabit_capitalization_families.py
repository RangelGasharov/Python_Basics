def grouping(words):
    groups = {}
    for word in words:
        key = get_amount_of_capital_letters(word)
        if key not in groups:
            groups[key] = [word]
        else:
            groups[key].append(word)
    for key in groups:
        groups[key].sort(key=str.lower)
    return sorted(groups.items())


def get_amount_of_capital_letters(word):
    amount_capital_letters = 0
    for i in range(len(word)):
        if word[i].isupper():
            amount_capital_letters += 1
    return amount_capital_letters


print(grouping(["MOVIE", "BAKE", "TAKE", "PERSON"]))
print(grouping(["the", "them", "theme", "EVERY"]))
print(grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]))
