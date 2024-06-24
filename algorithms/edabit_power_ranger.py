def power_ranger(degree, start, end):
    amount_of_powers = 0
    for num in range(start, end + 1):
        if num ** (1 / degree) % 1 == 0:
            amount_of_powers += 1
    return amount_of_powers


print(power_ranger(2, 49, 65))
print(power_ranger(3, 1, 27))
print(power_ranger(10, 1, 5))
print(power_ranger(5, 31, 33))
print(power_ranger(4, 250, 1300))
