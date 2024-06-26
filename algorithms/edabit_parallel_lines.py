def lines_are_parallel(line1, line2):
    if line1[0] == line2[0]:
        return True
    return False


print(lines_are_parallel([1, 2, 3], [1, 2, 4]))
print(lines_are_parallel([2, 4, 1], [4, 2, 1]))
print(lines_are_parallel([0, 1, 5], [0, 1, 5]))
