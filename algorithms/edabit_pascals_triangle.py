def pascals_triangle(row_number):
    pascal_triangle = [([0] * (row_number + 1)) for i in range(row_number + 1)]
    pascal_triangle[0][0] = 1
    for i in range(1, row_number + 1):
        for j in range(i + 1):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j] + (j > 0) * (pascal_triangle[i - 1][j - 1])
    return pascal_triangle[-1]


print(pascals_triangle(1))
print(pascals_triangle(4))
print(pascals_triangle(6))
print(pascals_triangle(8))
print(pascals_triangle(22))
print(pascals_triangle(29))
