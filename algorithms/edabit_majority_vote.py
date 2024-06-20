def majority_vote(voting_list):
    dictionary = {}
    for x in voting_list:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    max_count = 0
    majority_element = None
    for key, count in dictionary.items():
        if count > max_count and count > len(voting_list) / 2:
            max_count = count
            majority_element = key
    return majority_element


print(majority_vote([]))
print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
print(majority_vote(["A", "B", "C", "A", "C", "C"]))
print(majority_vote(["A", "B", "C", "A", "C", "C", "C"]))
