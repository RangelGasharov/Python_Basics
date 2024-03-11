def minimum_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def get_minimum_coins(number, coins):
    minimum_coins = {}

    minimum_coins[0] = 0
    for i in range(1, number + 1):
        for coin in coins:
            sub_problem = i - coin
            if sub_problem < 0:
                continue
            minimum_coins[i] = minimum_ignore_none(minimum_coins.get(i), minimum_coins.get(sub_problem) + 1)
    return minimum_coins[number]


print(get_minimum_coins(10000, {1, 2, 5, 10, 20, 50, 100, 200}))
