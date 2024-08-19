import math


def squares(a, b):
    return math.floor(math.sqrt(b)) - math.floor(math.sqrt(a)) + (math.sqrt(b) % 1 == 0) + (math.sqrt(a) % 1 == 0)


print(squares(1, 11))
print(squares(100, 1000))
print(squares(17, 24))
print(squares(1, 1000000000))
print(squares(50979851, 733216221))
print(squares(89784519, 103811134))
print(squares(433, 100000))
