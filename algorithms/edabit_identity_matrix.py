def id_mtrx(n):
    if n % 1 != 0:
        return "Error"
    if n == 0:
        return []
    const_true = 0 if n < 0 else 1
    const_false = 1 if n < 0 else 0
    matrix = []
    n = abs(n)
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            if i == j:
                temp.append(const_true)
            else:
                temp.append(const_false)
        matrix.append(temp)
    return matrix


def print_id_mtrx(matrix):
    for x in matrix:
        print(x)


print_id_mtrx(id_mtrx(-3))
print_id_mtrx(id_mtrx(2))
print_id_mtrx(id_mtrx(1))
print_id_mtrx(id_mtrx(-10))
