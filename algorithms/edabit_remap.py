def remap(value, low1, high1, low2, high2):
    if high1 == low1:
        return 0
    return (value - low1)/(high1-low1) * (high2 - low2) + low2


print(remap(7, 2, 12, 0, 100))
print(remap(17, 5, 55, 100, 30))
print(remap(50, 1, 51, 0, 100))
print(remap(2.5, 2, 3, -80, 80))
print(remap(0, 0, 0, 0, 0))
print(remap(20, 10, 50, 50, 10))
print(remap(0, 5, -20, 60, 1000))
print(remap(17, 17, 17, 519, 1085))