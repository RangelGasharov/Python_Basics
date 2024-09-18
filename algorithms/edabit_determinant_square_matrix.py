def get_det(matrix):
    size = len(matrix[0])
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0
    current_offset = 0
    for i in range(size):
        current_add = 1
        current_sub = 1
        for j in range(size):
            current_add *= matrix[(j + current_offset) % size][(j + current_offset) % size]
        result += current_add
        current_offset += 1
    return result


print(get_det([
    [0, 1],
    [1, 1]
]))
print(get_det([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(get_det([
    [69, 0],
    [1, 1]
]))

print(get_det([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))

print(get_det([[7,420,8],[5,7,0],[1,1,7]]))
