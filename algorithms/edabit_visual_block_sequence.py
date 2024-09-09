def blocks(n):
    if n == 0:
        return 0
    return int(1 / 2 * n ** 2 + 11 / 2 * n - 1)


# Tn = a*n^2 + b*n + c
# 2a = 2nd difference (Tn+1 - Tn - (Tn - Tn-1)), is a constant
# 3a + b = 2nd term - 1st term
# a + b + c = 1st term

print(blocks(0))
print(blocks(1))
print(blocks(2))
print(blocks(3))
print(blocks(4))
print(blocks(5))
print(blocks(93))
