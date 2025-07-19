def get_maximal_profit(stock_values):
    lowest_price = stock_values[0]
    highest_profit = 0
    for i in range(len(stock_values)):
        if lowest_price > stock_values[i]:
            lowest_price = stock_values[i]
        if stock_values[i] - lowest_price > highest_profit:
            highest_profit = stock_values[i] - lowest_price
    return highest_profit


print(get_maximal_profit([7, 1, 5, 3, 6, 4]))
print(get_maximal_profit([7, 6, 4, 3, 1]))
