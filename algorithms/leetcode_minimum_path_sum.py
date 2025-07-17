def get_minimum_path_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    path_sum_matrix = [[0] * m for _ in range(n)]
    path_sum_matrix[0][0] = matrix[0][0]

    for j in range(1, m):
        path_sum_matrix[0][j] = path_sum_matrix[0][j - 1] + matrix[0][j]

    for i in range(1, n):
        path_sum_matrix[i][0] = path_sum_matrix[i - 1][0] + matrix[i][0]

    for i in range(1, n):
        for j in range(1, m):
            path_sum_matrix[i][j] = matrix[i][j] + min(path_sum_matrix[i - 1][j], path_sum_matrix[i][j - 1])

    return path_sum_matrix[n - 1][m - 1]


print(get_minimum_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(get_minimum_path_sum([[1, 2, 3], [4, 5, 6]]))
print(get_minimum_path_sum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
