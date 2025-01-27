def is_wristband(matrix):
    is_horizontal = get_is_horizontal(matrix)
    is_vertical = get_is_vertical(matrix)
    return is_horizontal or is_vertical


def get_is_horizontal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(1, cols):
            if matrix[i][j] != matrix[i][j - 1]:
                return False
    return True


def get_is_vertical(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        for i in range(1, rows):
            if matrix[i][j] != matrix[i - 1][j]:
                return False
    return True


print(is_wristband([
    ["A", "A"],
    ["B", "B"],
    ["C", "C"]
]))

print(is_wristband([
    ["A", "B"],
    ["A", "B"],
    ["A", "B"]
]))
