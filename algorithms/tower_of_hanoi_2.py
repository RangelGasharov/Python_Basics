def print_path(start, end):
    print(f"{start} -> {end}")


def towers_of_hanoi(n, start, end):
    if n == 1:
        print_path(start, end)

    else:
        other = 6 - (start + end)
        towers_of_hanoi(n - 1, start, other)
        print_path(start, end)
        towers_of_hanoi(n - 1, other, end)


towers_of_hanoi(3, 1, 3)
