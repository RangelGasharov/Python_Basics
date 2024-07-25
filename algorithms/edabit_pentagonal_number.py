def pentagonal(num):
    if num == 1:
        return 1
    sum_dots = 0
    for i in range(1, num + 1):
        sum_dots += (i - 1) * 5

    return sum_dots + 1


print(pentagonal(1))
print(pentagonal(2))
print(pentagonal(4))
print(pentagonal(8))
print(pentagonal(62))
