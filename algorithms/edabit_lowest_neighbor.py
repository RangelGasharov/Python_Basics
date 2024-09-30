def lowest_element(matrix, row, col):
    lowest_value = matrix[row][col]
    start_row = (row - 1) * (row - 1 >= 0)
    end_row = row + 1 * (row + 1 < len(matrix))
    start_col = (col - 1) * (col - 1 >= 0)
    end_col = col + 1 * (col + 1 < len(matrix[0]))
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if matrix[i][j] < lowest_value:
                lowest_value = matrix[i][j]
    return lowest_value


print(lowest_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(lowest_element([[0, 3, 6], [1, 4, 7], [2, 5, 8]], 2, 2))
print(lowest_element([[50, 30, 10], [42, 69, 420], [9000, 3, 16]], 0, 0))
print(lowest_element([[-2, -5, -500, 49501], [1004, 10502, -5061, 19303], [40012, 487190, 39430, 13899],
                      [3, 1, 4, 1]], 2, 3))
