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
    if is_straight(card_transformed):
        return "Straight"
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
        if cards_list[i][1] != cards_list[i - 1][1]:
            return False
    return True


def is_straight_flush(cards_list):
    cards_list.sort()
    for i in range(1, len(cards_list)):
        if cards_list[i][1] != cards_list[i - 1][1]:
            return False
        if cards_list[i][0] != cards_list[i - 1][0] + 1:
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


def is_straight(cards_list):
    cards_list.sort()
    for i in range(1, len(cards_list)):
        if cards_list[i][0] != cards_list[i - 1][0] + 1:
            return False
    return True


print(poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]))
print(poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]))
print(poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]))
print(poker_hand_ranking(["4h", "9s", "2s", "2d", "Ad"]))
print(poker_hand_ranking(["10s", "9s", "8s", "6s", "7s"]))
print(poker_hand_ranking(["10c", "9c", "9s", "10s", "9h"]))
print(poker_hand_ranking(["8h", "2h", "8s", "3s", "3c"]))
print(poker_hand_ranking(["Jh", "9h", "7h", "5h", "2h"]))
print(poker_hand_ranking(["Ac", "Qc", "As", "Ah", "2d"]))
print(poker_hand_ranking(["10h", "Jh", "Qs", "Ks", "Ac"]))
