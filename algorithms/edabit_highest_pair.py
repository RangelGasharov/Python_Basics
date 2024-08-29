def highest_pair(cards):
    card_values = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9,
                   "J": 10, "Q": 11, "K": 12, "A": 13}
    contains_pairs = False
    pair_sign = ""
    pair_value = 0
    cards.sort()
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1] and card_values[cards[i]] > pair_value:
            pair_sign = cards[i]
            pair_value = card_values[cards[i]]
            contains_pairs = True

    if not contains_pairs:
        return False
    return [contains_pairs, pair_sign]


print(highest_pair(["A", "A", "Q", "Q", "6"]))
print(highest_pair(["J", "6", "3", "10", "8"]))
print(highest_pair(["K", "7", "3", "9", "3"]))
print(highest_pair(["K", "9", "10", "J", "Q"]))
print(highest_pair(["3", "5", "5", "5", "5"]))
print(highest_pair(['A', 'K', 'K', 'K', 'Q']))
print(highest_pair(['A', 'K', 'Q', 'Q', '5']))
print(highest_pair(['A', '3', '3', '4', '4']))
print(highest_pair(['A', 'K', 'Q', 'J', '10']))
