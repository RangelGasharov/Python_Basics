def can_see_stage(mtrx):
    width = len(mtrx[0])
    height = len(mtrx)
    for x in range(0, width):
        for y in range(1, height):
            if mtrx[y][x] <= mtrx[y - 1][x]:
                return False
    return True


print(can_see_stage([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(can_see_stage([[0, 0, 0], [1, 1, 1], [2, 2, 2]]))
print(can_see_stage([[2, 0, 0], [1, 1, 1], [2, 2, 2]]))
print(can_see_stage([[1, 0, 0], [1, 1, 1], [2, 2, 2]]))
