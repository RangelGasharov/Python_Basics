def find_glasses(words_list):
    for i in range(len(words_list)):
        if has_glasses(words_list[i]):
            return i
    return 0


def has_glasses(word):
    start_is_right = False
    end_is_right = False
    for i in range(len(word)):
        if word[i] == "O" and start_is_right and word[i - 1] == "-":
            return True
        if word[i] == "O" and not end_is_right:
            start_is_right = True
        if word[i] not in ["-", "O"] and start_is_right:
            start_is_right = False
    return False


print(find_glasses(["phone", "O-O", "coins", "keys"]))
print(find_glasses(["OO", "wallet", "O##O", "O----O"]))
print(find_glasses(["O--#--O", "dustO---Odust", "more dust"]))
print(find_glasses(['O--#--O', 'dustO---Odust', 'more dust']))
print(find_glasses(['floor', 'the floor again', 'pockets', 'bed', 'cabinet', 'the top of my head O-O']))
print(find_glasses(['OOOO----~OOO', '-------', 'OOOOOOO', 'OO-OO-OO-O']))
