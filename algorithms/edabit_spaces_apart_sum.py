def space_apart(numbers):
    amount_of_borders = 0
    sum_numbers = 0
    for i in range(len(numbers)):
        if not isinstance(numbers[i], int):
            if numbers[i] == "1":
                amount_of_borders += 1
                if amount_of_borders > 1:
                    return sum_numbers
            continue
        if numbers[i] < 0:
            return "invalid"
        else:
            if amount_of_borders == 1:
                sum_numbers += numbers[i]
    return "invalid"


print(space_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]))
print(space_apart(["1", 9, 20, 38, "1"]))
print(space_apart([3, 2, 9, "1", 0, 0, -1, "1"]))
print(space_apart(["2", "a", 1, "1", 1, 3, 49, "1"]))
print(space_apart(["1", -593, 1, "1", 4, 3, 2, 33, 2]))
print(space_apart([4, 3, "1", "2", 4, "1", "2", "9"]))
