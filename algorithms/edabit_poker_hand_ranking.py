def poker_hand_ranking(cards_list):
    card_transformed = []
    for card in cards_list:
        card_transformed.append([get_card_value(card[:-1]), card[-1]])
    if is_royal_flush(card_transformed):
        return "Royal Flush"
    if is_straight_flush(card_transformed):
        return "Straight Flush"
    if is_flush(card_transformed):
        return "Flush"
    return card_transformed


def get_card_value(card_value_string):
    values = {"J": 11, "Q": 12, "K": 13, "A": 14}
    if card_value_string.isnumeric():
        return int(card_value_string)
    return values[card_value_string]


def is_flush(cards_list):
    cards_list.sort()
    for i in range(1, len(cards_list)):
        if cards_list[i][0] <= cards_list[i - 1][0]:
            return False
    return True


def is_straight_flush(cards_list):
    cards_list.sort()
    for i in range(1, len(cards_list)):
        if cards_list[i][1] != cards_list[i - 1][1]:
            return False
        if cards_list[i][0] <= cards_list[i - 1][0]:
            return False
    return True


def is_royal_flush(cards_list):
    cards_list.sort()
    if cards_list[0][0] != 10:
        return False
    return is_straight_flush(cards_list)


print(poker_hand_ranking(["Ah", "As", "Qc", "3d", "9d"]))
print(poker_hand_ranking(["Ad", "Qd", "Jd", "Kd", "10d"]))
print(poker_hand_ranking(["9d", "Qd", "Jd", "Kd", "10d"]))
