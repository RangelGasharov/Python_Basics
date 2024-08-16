def cube_diagonal(cube_volume):
    side_length = cube_volume ** (1 / 3)
    diagonal = (3 * side_length ** 2) ** (1 / 2)
    return round(diagonal, 2)


print(cube_diagonal(8))
print(cube_diagonal(343))
print(cube_diagonal(1157.625))
print(cube_diagonal(1728))
