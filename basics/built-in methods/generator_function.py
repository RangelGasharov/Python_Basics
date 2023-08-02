def gen_function():
    yield 100
    yield "hello"
    yield False


try:
    scrap = gen_function()
    print(next(scrap))
    print(next(scrap))
    print(next(scrap))
    print(next(scrap))
except StopIteration:
    print("This is the last item in the code")


def add_number(num):
    for i in num:
        yield i + i


value = add_number([5, 2])
try:
    print(next(value))
    print(next(value))
    print(next(value))
    print(next(value))
except StopIteration:
    print("No more values to add")
