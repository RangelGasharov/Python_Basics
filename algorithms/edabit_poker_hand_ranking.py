def poker_hand_ranking(cards_list):
    card_transformed = []
    for card in cards_list:
        card_transformed.append([get_card_value(card[:-1]), card[-1]])
    card_transformed.sort()
    return card_transformed


def get_card_value(card_value_string):
    values = {"J": 11, "Q": 12, "K": 13, "A": 14}
    if card_value_string.isnumeric():
        return int(card_value_string)
    return values[card_value_string]


print(poker_hand_ranking(["Ah", "As", "Qc", "3d", "9d"]))
