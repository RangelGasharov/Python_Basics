def remove_smallest(ratings):
    if not ratings:
        return []
    smallest_rating = ratings[0]
    smallest_rating_index = 0
    for i in range(1, len(ratings)):
        if ratings[i] < smallest_rating:
            smallest_rating_index = i
            smallest_rating = ratings[i]
    del ratings[smallest_rating_index]
    return ratings


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))
print(remove_smallest([3]))
print(remove_smallest([]))
print(remove_smallest([5, 4, 5, 3, 1, 1]))

