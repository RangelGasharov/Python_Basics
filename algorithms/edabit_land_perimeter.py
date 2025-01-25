def islands_perimeter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_perimeter = 0
    for i in range(rows):
        for j in range(cols):
            current_is_land = (matrix[i][j] == 1)
            if not current_is_land:
                continue
            if i == 0 or matrix[i - 1][j] == 0:
                total_perimeter += 1
            if i == rows - 1 or matrix[i + 1][j] == 0:
                total_perimeter += 1
            if j == 0 or matrix[i][j - 1] == 0:
                total_perimeter += 1
            if j == cols - 1 or matrix[i][j + 1] == 0:
                total_perimeter += 1
    return total_perimeter


print(islands_perimeter([
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]))

print(islands_perimeter([
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
]))

print(islands_perimeter([
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
]))
