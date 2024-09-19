def get_det(matrix):
    size = len(matrix[0])
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0
    for i in range(size):
        result -= get_diagonal_product(matrix, i, True)
        result += get_diagonal_product(matrix, i, False)
    return result


def get_diagonal_product(matrix, offset, diagonal_reversed):
    size = len(matrix)
    product = 1
    if diagonal_reversed:
        for i in reversed(range(size)):
            product *= matrix[size - 1 - i][(i + offset) % size]
    else:
        for i in range(size):
            product *= matrix[i][(i + offset) % size]
    return product


print(get_det([[0, 1], [1, 0]]))
print(get_det([[69, 0], [1, 1]]))
print(get_det([[7, 420, 8], [5, 7, 0], [1, 1, 7]]))
print(get_det([[5, 1], [1, 6]]))
print(get_det([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(get_det([[-1, 1, -1], [-1, -55, 1], [1, -1, -1]]))
print(get_det([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
