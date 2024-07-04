def freed_prisoners(prisoners):
    free_prisoners = 0
    if prisoners[0] == 0:
        return 0
    free_prisoners = 1
    for i in range(1, len(prisoners)):
        if prisoners[i] != prisoners[i - 1]:
            free_prisoners += 1
    return free_prisoners


print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
print(freed_prisoners([1, 1, 1]))
print(freed_prisoners([0, 0, 0]))
print(freed_prisoners([0, 1, 1, 1]))
print(freed_prisoners([1, 0, 0, 1, 1, 1, 0, 1]))
print(freed_prisoners([1]))
