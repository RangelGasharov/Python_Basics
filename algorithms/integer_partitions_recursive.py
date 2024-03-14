def count_integer_partitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_integer_partitions(n - m, m) + count_integer_partitions(n, m - 1)


print(count_integer_partitions(3, 3))
print(count_integer_partitions(20, 5))
