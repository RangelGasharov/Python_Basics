from collections import defaultdict


def get_amount_of_ways(number, coins):
    memo = defaultdict(lambda _: 0)

    memo[0] = 1
    for i in range(1, number + 1):
        memo[i] = 0

        for coin in coins:
            sub_problem = i - coin
            if sub_problem < 0:
                continue

            memo[i] = memo[i] + memo[sub_problem]
    return memo[number]


print(get_amount_of_ways(10, [1, 2, 5]))
