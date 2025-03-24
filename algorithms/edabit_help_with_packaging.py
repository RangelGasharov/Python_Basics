def can_fit(weights, amount_of_bags):
    weight_per_bag = 10
    bags = [0] * amount_of_bags
    weights.sort(reverse=True)
    for weight in weights:
        placed = False
        for i in range(amount_of_bags):
            if bags[i] + weight <= weight_per_bag:
                bags[i] += weight
                placed = True
                break
        if not placed:
            return False
    return True


print("True statements:")
print(can_fit([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2], 4))
print(can_fit([2, 5, 1, 6, 2, 9, 5, 2, 1, 6, 1, 6, 6, 1], 6))
print(can_fit([7, 1, 2, 6, 1, 2, 3, 5, 9, 2, 1, 2, 5], 5))
print(can_fit([4, 1, 2, 3, 5, 5, 1, 9], 3))
print(can_fit([3, 1, 2, 7, 2, 6, 1], 3))
print(can_fit([3, 7, 2, 8, 1, 9], 3))
print("False statements:")
print(can_fit([2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2], 4))
print(can_fit([9, 6, 2, 3, 1, 2, 4, 8, 3, 1, 3], 4))
print(can_fit([2, 5, 1, 6, 2, 9, 5, 2, 1, 6, 1, 6, 6, 1], 5))
