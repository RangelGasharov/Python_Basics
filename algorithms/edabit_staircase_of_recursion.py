def ways_to_climb(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    if num == 2:
        return 2
    return ways_to_climb(num - 1) + ways_to_climb(num - 2)


print(ways_to_climb(4))
