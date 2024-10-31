results = [1, 1, 2]


def ways_to_climb(num):
    if num < len(results):
        return results[num]
    else:
        results.append(ways_to_climb(num - 1) + ways_to_climb(num - 2))
    return results[num]


print(ways_to_climb(4))
print(ways_to_climb(5))
print(ways_to_climb(6))
print(ways_to_climb(7))
print(ways_to_climb(23))
print(ways_to_climb(1000))
