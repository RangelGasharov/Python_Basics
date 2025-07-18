def get_climbing_stairs(number):
    climbing_stairs_values = [0] * (number + 1)
    climbing_stairs_values[0], climbing_stairs_values[1] = 1, 1

    for i in range(2, number + 1):
        climbing_stairs_values[i] = climbing_stairs_values[i - 1] + climbing_stairs_values[i - 2]

    return climbing_stairs_values[number]


print(get_climbing_stairs(1))
print(get_climbing_stairs(2))
print(get_climbing_stairs(3))
print(get_climbing_stairs(4))
print(get_climbing_stairs(5))
print(get_climbing_stairs(6))
print(get_climbing_stairs(45))
print(get_climbing_stairs(1000))
