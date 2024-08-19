def can_complete(partial_word, final_word):
    index_partial_word = 0
    index_final_word = 0
    is_going = True
    while is_going:
        if index_partial_word == len(partial_word):
            return True
        if index_final_word == len(final_word):
            return False
        if partial_word[index_partial_word] == final_word[index_final_word]:
            index_partial_word += 1
            index_final_word += 1
        else:
            index_final_word += 1


print(can_complete("butl", "beautiful"))
print(can_complete('sg', 'something'))
print(can_complete('sing', 'something'))
print(can_complete("butlz", "beautiful"))
print(can_complete("tulb", "beautiful"))
print(can_complete("bbutl", "beautiful"))
print(can_complete('siing', 'something'))
print(can_complete("wd", "word"))
