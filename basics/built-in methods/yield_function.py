def cube(num):
    for i in num:
        yield i ** 3


bar = cube([1, 2, 3, 4, 5])
print(next(bar))
print(next(bar))
print(next(bar))
print(next(bar))
print(next(bar))
