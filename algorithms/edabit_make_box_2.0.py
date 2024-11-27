def char_box(num):
    if not isinstance(num, int):
        return -1
    if num < 0:
        return -1
    if num == 0:
        return [[]]
    matrix = [["" for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if i == 0 or i == num - 1:
                matrix[i][j] = "#"
            elif j == 0 or j == num - 1:
                matrix[i][j] = "#"
            else:
                matrix[i][j] = " "
    return matrix


def print_matrix(matrix):
    result_string = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_string += matrix[i][j]
        result_string += "\n"
    print(result_string)


print(char_box("Hi"))
print(char_box(.23))
print(char_box(-4))
print(char_box(0))
print_matrix(char_box(1))
print_matrix(char_box(4))
print_matrix(char_box(10))
