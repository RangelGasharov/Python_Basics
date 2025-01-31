def is_wristband(matrix):
    is_horizontal = get_is_horizontal(matrix)
    if is_horizontal:
        return True
    is_vertical = get_is_vertical(matrix)
    if is_vertical:
        return True
    is_diagonal_asc = get_is_diagonal_asc(matrix)
    if is_diagonal_asc:
        return True
    is_diagonal_desc = get_is_diagonal_desc(matrix)
    if is_diagonal_desc:
        return True
    return False


def get_is_horizontal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(1, cols):
            if matrix[i][j] != matrix[i][j - 1]:
                return False
    return True


def get_is_vertical(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for j in range(cols):
        for i in range(1, rows):
            if matrix[i][j] != matrix[i - 1][j]:
                return False
    return True


def get_is_diagonal_asc(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for d in range(rows + cols - 1):
        i, j = min(d, rows - 1), max(0, d - rows + 1)
        first_value = matrix[i][j]
        while i >= 0 and j < cols:
            if matrix[i][j] != first_value:
                return False
            i -= 1
            j += 1
    return True


def get_is_diagonal_desc(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for d in range(rows):
        i, j = d, 0
        first_value = matrix[i][j]
        while i < rows and j < cols:
            if matrix[i][j] != first_value:
                return False
            i += 1
            j += 1
    for d in range(1, cols):
        i, j = 0, d
        first_value = matrix[i][j]
        while i < rows and j < cols:
            if matrix[i][j] != first_value:
                return False
            i += 1
            j += 1
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

print(is_wristband(
    [
        ["C", "B", "A"],
        ["B", "A", "C"],
        ["A", "C", "C"]
    ]
))

print(is_wristband(
    [
        ["A", "B", "C", "D"],
        ["C", "A", "B", "C"],
        ["D", "C", "A", "B"]
    ]
))
