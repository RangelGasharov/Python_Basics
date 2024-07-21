def get_primiera_score(cards):
    divided_cards = get_divided_cards(cards)
    card_points = get_card_points(divided_cards)
    return card_points


def get_value_card(card):
    values_dictionary = {"7": 21, "6": 18, "A": 16, "J": 10, "Q": 10, "K": 10, }
    if card[0] not in values_dictionary:
        return int(card[0]) + 10
    return values_dictionary[card[0]]


def get_card_points(cards):
    sum_card_points = 0
    if len(cards) < 4:
        return 0
    for x in cards:
        sum_card_points += max(x)
    return sum_card_points


def get_divided_cards(cards):
    new_cards = []
    temp = []
    current_type = cards[0][1]
    for i in range(0, len(cards)):
        if cards[i][1] == current_type:
            temp.append(get_value_card(cards[i]))
        else:
            current_type = cards[i][1]
            new_cards.append(temp)
            temp = []
            temp.append(get_value_card(cards[i]))
        if i == len(cards) - 1:
            new_cards.append(temp)
    return new_cards


print(get_primiera_score(["Ad", "7d", "5h", "2c", "Ks"]))
print(get_primiera_score(["2d", "Jd", "7h", "Qc", "5s", "As"]))
print(get_primiera_score(["2d", "Jd", "Qc", "5s", "As"]))
print(get_primiera_score(["5d", "7h", "Qc", "Ac", "4c", "Kc", "As"]))
