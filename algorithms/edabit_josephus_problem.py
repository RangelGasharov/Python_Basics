def josephus(people_count, interval):
    people_list = []
    for i in range(1, people_count + 1):
        people_list.append(i)
    result = josephus_recursive(people_list, interval, 0)
    return result


def josephus_recursive(people, interval, index):
    if len(people) == 1:
        return people[0]
    index = ((index + interval - 1) % len(people))
    people.pop(index)
    return josephus_recursive(people, interval, index)


print(josephus(41, 3))
print(josephus(35, 11))
print(josephus(11, 1))
print(josephus(2, 2))
