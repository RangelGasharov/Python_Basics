def party_people(people_list):
    sorted_people_list = sorted(people_list)
    result = recursive_party_people(sorted_people_list[len(people_list) - 1], sorted_people_list)
    return result


def recursive_party_people(current_minimum, people_list):
    if len(people_list) == 0:
        return 0
    if len(people_list) == 1:
        if current_minimum <= 1:
            return 1
        return 0
    if current_minimum <= len(people_list):
        return len(people_list)
    else:
        people_list.pop()
        return recursive_party_people(people_list[len(people_list) - 1], people_list)


print(party_people([4, 5, 4, 1]))
print(party_people([10, 12, 15, 15, 5]))
print(party_people([2, 1, 2, 0]))
print(party_people([0, 0, 0, 0]))
print(party_people([11, 3, 4, 3, 11, 4, 0, 1, 1, 3]))
print(party_people([15, 3, 8, 0, 2, 12, 13, 7, 6]))
print(party_people([7, 14, 14, 0, 7, 3, 2, 2]))
print(party_people([2, 6, 7, 4, 6, 10, 4, 3, 6, 2, 0]))
print(party_people([9, 7, 5, 5, 5, 3, 2, 1]))
