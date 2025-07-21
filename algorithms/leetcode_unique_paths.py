import math


def unique_paths(m, n):
    return math.comb(m + n - 2, m - 1)


print(unique_paths(3, 7))
print(unique_paths(7, 3))
print(unique_paths(3, 2))
print(unique_paths(2, 3))
print(unique_paths(6, 10))
