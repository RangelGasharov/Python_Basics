import math


def V_DAC(num):
    if num == 0:
        return 0
    return round(num/1024 * 5, 2)


print(V_DAC(0))
print(V_DAC(1024))
print(V_DAC(400))
