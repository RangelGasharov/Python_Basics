import math


def snake_fill(n):
    return math.floor(math.log2(n ** 2))


print(snake_fill(3))
print(snake_fill(6))
print(snake_fill(24))
print(snake_fill(900))
print(snake_fill(900))
print(snake_fill(1))
print(snake_fill(2))
