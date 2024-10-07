def can_find(bigrams_list, words):
    for word in words:
        for i in range(len(word) - 1):
            current_bigrams = word[i] + word[i + 1]
            for bigrams in bigrams_list:
                if current_bigrams == bigrams:
                    bigrams_list.remove(bigrams)
    return len(bigrams_list) < 1


print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
print(can_find(["bo", "ta", "el", "st", "ca"], ["books", "table", "cap", "hostel"]))
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))
print(can_find(["la"], []))
print(can_find(["la", "at", "te", "ea"], ["latte"]))
