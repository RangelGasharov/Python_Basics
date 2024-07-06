def final(rows, cols, increments):
    identity_mtrx = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in increments:
        identity_mtrx = read_incrementation(x, identity_mtrx)
    return identity_mtrx


def read_incrementation(string, mtrx):
    operation = string[-1]
    number = int(string[0: len(string) - 1])
    if operation == "c":
        for i in range(0, len(mtrx)):
            mtrx[i][number] += 1
    if operation == "r":
        for i in range(len(mtrx[0])):
            mtrx[number][i] += 1
    return mtrx


def print_id_mtrx(matrix):
    for x in matrix:
        print(x)


print_id_mtrx(final(5, 5, ["1r", "3r"]))
print_id_mtrx(final(2, 2, ["0r", "0r", "0r", "1c"]))
print_id_mtrx(final(2, 2, ["0c"]))
print_id_mtrx(final(3, 3, ["0c", "1c", "1c", "2c", "2c", "2c"]))
print_id_mtrx(final(3, 3, []))
