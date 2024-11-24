def get_frequencies(items_list):
    if len(items_list) < 1:
        return {}
    frequency_dictionary = {}
    for item in items_list:
        if item in frequency_dictionary:
            frequency_dictionary[item] += 1
        else:
            frequency_dictionary[item] = 1
    return frequency_dictionary


print(get_frequencies(['A', 'A']))
print(get_frequencies(["A", "B", "A", "A", "A"]))
print(get_frequencies([1, 2, 3, 3, 2]))
print(get_frequencies([True, False, True, False, False]))
print(get_frequencies([]))
