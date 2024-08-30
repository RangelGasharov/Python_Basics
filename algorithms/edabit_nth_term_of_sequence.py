def seq(n):
    return int(2 + (n > 1) * (n - 1) * 4 + (n > 2) * (n - 2) * (n - 1) / 2 * 3)


print(seq(1))
print(seq(2))
print(seq(6))
print(seq(18))
print(seq(27))
print(seq(99))
