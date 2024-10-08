def multiplication_table(number):
    resulting_matrix = []
    for i in range(number):
        temporary_table = []
        for j in range(number):
            temporary_table.append((i + 1) * (j + 1))
        resulting_matrix.append(temporary_table)
    return resulting_matrix


print(multiplication_table(5))
print(multiplication_table(6))
print(multiplication_table(20))
