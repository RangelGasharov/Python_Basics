def row_sum(n):
    sum_numbers = 0
    current_number = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i == n:
                sum_numbers += current_number
            current_number += 1
    return sum_numbers


print(row_sum(1))
print(row_sum(2))
print(row_sum(3))
print(row_sum(4))
print(row_sum(1000))
