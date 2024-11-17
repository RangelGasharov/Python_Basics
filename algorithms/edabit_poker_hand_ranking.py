def poker_hand_ranking(cards_list):
    card_transformed = []
    for card in cards_list:
        card_transformed.append([get_card_value(card[:-1]), card[-1]])
    if is_royal_flush(card_transformed):
        return "Royal Flush"
    if is_straight_flush(card_transformed):
        return "Straight Flush"
    if is_four_of_a_kind(card_transformed):
        return "Four of a Kind"
    amount_of_pairs = get_amount_of_pairs(card_transformed)
    amount_of_triads = get_amount_of_triads(card_transformed)
    if amount_of_triads == 1 and amount_of_pairs == 1:
        return "Full House"
    if is_flush(card_transformed):
        return "Flush"
    if amount_of_triads == 1:
        return "Three of a Kind"
    if amount_of_pairs == 2:
        return "Two Pair"
    if amount_of_pairs == 1:
        return "Pair"
    return "High Card"


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


def is_four_of_a_kind(cards_list):
    rank_occurrence = {}
    for card in cards_list:
        current_rank = card[0]
        if current_rank in rank_occurrence:
            rank_occurrence[current_rank] += 1
        else:
            rank_occurrence[current_rank] = 1
    return 4 in rank_occurrence.values()


def get_amount_of_pairs(cards_list):
    rank_occurrence = {}
    amount_of_pairs = 0
    for card in cards_list:
        current_rank = card[0]
        if current_rank in rank_occurrence:
            rank_occurrence[current_rank] += 1
        else:
            rank_occurrence[current_rank] = 1
    for key, value in rank_occurrence.items():
        if rank_occurrence[key] == 2:
            amount_of_pairs += 1
    return amount_of_pairs


def get_amount_of_triads(cards_list):
    rank_occurrence = {}
    amount_of_triads = 0
    for card in cards_list:
        current_rank = card[0]
        if current_rank in rank_occurrence:
            rank_occurrence[current_rank] += 1
        else:
            rank_occurrence[current_rank] = 1
    for key, value in rank_occurrence.items():
        if rank_occurrence[key] == 3:
            amount_of_triads += 1
    return amount_of_triads


print(poker_hand_ranking(["Ah", "As", "Qc", "3d", "9d"]))
print(poker_hand_ranking(["Ad", "Qd", "Jd", "Kd", "10d"]))
print(poker_hand_ranking(["9d", "Qd", "Jd", "Kd", "10d"]))
print(poker_hand_ranking(["9d", "9s", "9c", "9h", "10d"]))
