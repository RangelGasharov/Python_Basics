def bonus(days):
    sum_bonus = 0
    boundaries = [48, 40, 32]
    bonus_reward = [600, 550, 325]

    for i in range(0, len(boundaries)):
        if days > boundaries[i]:
            sum_bonus += (days - boundaries[i]) * bonus_reward[i]
            days -= days - boundaries[i]

    return sum_bonus


print(bonus(15))
print(bonus(37))
print(bonus(50))
print(bonus(49))
