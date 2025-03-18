def sudoku_validator(matrix):
    if not has_valid_columns(matrix):
        return False
    if not has_valid_rows(matrix):
        return False
    if not has_valid_boxes(matrix):
        return False
    return True


def has_valid_boxes(matrix):
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = [matrix[row][col] for row in range(block_row, block_row + 3)
                     for col in range(block_col, block_col + 3)]
            is_valid = is_valid_number_list(block)
            if not is_valid:
                return False
    return True


def has_valid_columns(matrix):
    for i in range(len(matrix[0])):
        col_matrix = []
        for j in range(len(matrix)):
            col_matrix.append(matrix[j][i])
        is_valid = is_valid_number_list(col_matrix)
        if not is_valid:
            return False
    return True


def has_valid_rows(matrix):
    for i in range(len(matrix)):
        row_matrix = []
        for j in range(len(matrix[0])):
            row_matrix.append(matrix[i][j])
        is_valid = is_valid_number_list(row_matrix)
        if not is_valid:
            return False
    return True


def is_valid_number_list(number_list):
    return len(number_list) == 9 and set(number_list) == set(range(1, 10))


print(sudoku_validator(
    [
        [1, 5, 2, 4, 8, 9, 3, 7, 6],
        [7, 3, 9, 2, 5, 6, 8, 4, 1],
        [4, 6, 8, 3, 7, 1, 2, 9, 5],
        [3, 8, 7, 1, 2, 4, 6, 5, 9],
        [5, 9, 1, 7, 6, 3, 4, 2, 8],
        [2, 4, 6, 8, 9, 5, 7, 1, 3],
        [9, 1, 4, 6, 3, 7, 5, 8, 2],
        [6, 2, 5, 9, 4, 8, 1, 3, 7],
        [8, 7, 3, 5, 1, 2, 9, 6, 4]
    ]
))

print(sudoku_validator(
    [
        [1, 1, 2, 4, 8, 9, 3, 7, 6],
        [7, 3, 9, 2, 5, 6, 8, 4, 1],
        [4, 6, 8, 3, 7, 1, 2, 9, 5],
        [3, 8, 7, 1, 2, 4, 6, 5, 9],
        [5, 9, 1, 7, 6, 3, 4, 2, 8],
        [2, 4, 6, 8, 9, 5, 7, 1, 3],
        [9, 1, 4, 6, 3, 7, 5, 8, 2],
        [6, 2, 5, 9, 4, 8, 1, 3, 7],
        [8, 7, 3, 5, 1, 2, 9, 6, 4]
    ]
))

print(sudoku_validator(
    [[8, 2, 7, 1, 5, 4, 3, 9, 6],
     [9, 6, 5, 3, 2, 7, 1, 4, 8],
     [3, 4, 1, 6, 8, 9, 7, 5, 2],
     [5, 9, 3, 4, 6, 8, 2, 7, 1],
     [4, 7, 2, 5, 1, 3, 6, 8, 9],
     [6, 1, 8, 9, 7, 2, 4, 3, 5],
     [7, 8, 6, 2, 3, 5, 9, 1, 4],
     [1, 5, 4, 7, 9, 6, 8, 2, 3],
     [2, 3, 9, 8, 4, 1, 5, 6, 7]]
))
