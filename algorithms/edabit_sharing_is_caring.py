def show_the_love(numbers):
    if len(numbers) < 1:
        return []
    smallest_number = numbers[0]
    index_smallest_number = 0
    amount_removed = 0
    for i in range(len(numbers)):
        if numbers[i] < smallest_number:
            smallest_number = numbers[i]
            index_smallest_number = i
    for i in range(len(numbers)):
        amount_removed += numbers[i] / 4
        numbers[i] -= numbers[i] / 4
    numbers[index_smallest_number] += amount_removed
    return numbers


print(show_the_love([4, 1, 4]))
print(show_the_love([16, 10, 8]))
print(show_the_love([2, 100]))
print(show_the_love([26, 48, 84, 70, 8]))
print(show_the_love([82, 89, 52, 25, 50]))
