def tower_of_hanoi(n, a, b, c):
    if n == 1:
        print(f"move 1st disk from {a} to {c}")
        return
    tower_of_hanoi(n - 1, a, c, b)
    print(f"move {n}th disk from {a} to {c}")
    tower_of_hanoi(n - 1, b, a, c)

print(tower_of_hanoi(3, 1, 2, 3))