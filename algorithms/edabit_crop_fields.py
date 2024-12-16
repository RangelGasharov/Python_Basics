def crop_hydrated(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "c":
                is_hydrated = False
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if matrix[ni][nj] == "w":
                                is_hydrated = True
                if not is_hydrated:
                    return False
    return True


print(crop_hydrated([["w", "c"], ["w", "c"], ["c", "c"]]))
print(crop_hydrated(
    [["c", "w", "w", "w", "c"], ["w", "c", "c", "c", "c"], ["c", "c", "c", "c", "c"], ["w", "c", "c", "w", "c"]]))
print(crop_hydrated([["c", "w"]]))
print(crop_hydrated([
    ["c", "c", "w", "c", "c", "w"],
    ["c", "w", "c", "c", "c", "c"],
    ["c", "c", "c", "c", "c", "c"],
    ["c", "c", "c", "w", "c", "c"],
    ["c", "c", "c", "c", "w", "c"],
    ["c", "c", "c", "c", "c", "c"],
    ["c", "c", "c", "c", "c", "c"],
    ["c", "c", "c", "c", "c", "c"]
]))
print(crop_hydrated([["c", "c", "w", "c", "c", "w", "c", "w"]]))
