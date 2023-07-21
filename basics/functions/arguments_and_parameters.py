# parameters
def function_1(x, y, z):
    print(x, y, z)
    pass


# arguments
function_1(1, 2, 3)
function_1(z=2, y=0, x=3)


# error: function_1(z=2, 1, y=3)


def function_2(x, y, z=None):
    print(x, y, z)
    pass


function_2(1, 2)


def function_3(x, y, z=10):
    print(x, y, z)
    pass


function_3(1, 2)
function_3(1, 2, 3)


def function_4(x, y, *args):
    print(x, y, args)
    pass


function_4(1, 2, 1, 4, 0, 9, 8, 1)


def function_5(*args, **kwargs):
    print(args, kwargs["a"])
    pass


function_5(1, 2, 3, a=3, b=True, c=False, d="Text")


def function_6(a, b, c=False, d=True):
    print(a, b, c, d)
    pass


function_6(*[8, 12], **{"c": "alpha", "d": "beta"})
