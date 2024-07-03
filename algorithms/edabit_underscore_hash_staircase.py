def staircase(num):
    is_going_up = True if num > 0 else False
    num = abs(num)
    number_of_underscores = num - 1 if is_going_up else 0
    number_of_hashes = num - number_of_underscores
    result = ""
    for i in range(0, num):
        result += "_" * number_of_underscores + "#" * number_of_hashes + "\n"
        number_of_hashes = number_of_hashes + 1 if is_going_up else number_of_hashes - 1
        number_of_underscores = number_of_underscores - 1 if is_going_up else number_of_underscores + 1
    return result


print(staircase(7))
print(staircase(-10))
print(staircase(3))
