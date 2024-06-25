def collatz(a, b):
    steps_a = collatz_conjecture(a)
    steps_b = collatz_conjecture(b)
    return "a" if steps_a < steps_b else "b"


def collatz_conjecture(num):
    amount_of_steps = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            amount_of_steps += 1
        else:
            num = num * 3 + 1
            amount_of_steps += 1
    return amount_of_steps


print(collatz(10, 15))
print(collatz(13, 16))
print(collatz(53782, 72534))
