def party_people(people_list):
    sorted_people_list = sorted(people_list)
    for i in reversed(range(0, len(sorted_people_list))):
        if sorted_people_list[i] <= i + 1:
            return i + 1
    return 0


print(party_people([10, 12, 15, 15, 5]))
print(party_people([2, 1, 2, 0]))
print(party_people([3, 11, 15, 5, 3, 4, 10, 8, 14, 6, 13, 1]))
print(party_people([13, 8, 11, 15, 13, 3, 12, 13, 6, 3]))
print(party_people([5, 5, 5, 5, 5]))
print(party_people([4, 5, 4, 1]))
print(party_people([2, 6, 7, 4, 6, 10, 4, 3, 6, 2, 0]))
