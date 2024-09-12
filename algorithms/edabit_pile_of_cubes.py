def pile_of_cubes(total_volume):
    current_cube = 1
    current_volume = 1
    while current_volume < total_volume:
        current_cube += 1
        current_volume += current_cube ** 3
    return (current_volume == total_volume) * current_cube or None


print(pile_of_cubes(1071225))
print(pile_of_cubes(4183059834009))
print(pile_of_cubes(40539911473216))
print(pile_of_cubes(112668204662785))
print(pile_of_cubes(10252519345963644753025))
print(pile_of_cubes(10252519345963644753026))
print(pile_of_cubes(102525193459636447530260))
