def valid_name(full_name):
    valid_combinations = [[True, False], [True, True, False], [False, True, False], [False, False, False]]
    separated_names = separate_words(full_name)
    if len(separated_names) > 3 or len(separated_names) < 2:
        return False
    for i in range(len(separated_names)):
        if separated_names[i][0].islower():
            return False
    initials_combinations = []
    for i in range(len(separated_names)):
        initials_combinations.append(is_initial(separated_names[i]))
    if initials_combinations not in valid_combinations:
        return False
    return True


def is_initial(name):
    if len(name) != 2:
        return False
    if name[0].islower():
        return False
    if name[1] != ".":
        return False
    return True


def separate_words(full_name):
    separated_words = []
    current_word = ""
    for i in range(len(full_name)):
        if full_name[i] == " ":
            separated_words.append(current_word)
            current_word = ""
        else:
            current_word += full_name[i]
    separated_words.append(current_word)
    return separated_words


print(valid_name("H. Wells"))
print(valid_name("H. Wells"))
print(valid_name("Herbert G. Wells"))
print(valid_name("Herbert George Wells"))
print(valid_name("Herbert"))
print(valid_name("Herbert W. G. Wells"))
print(valid_name("h. Wells"))
print(valid_name("herbert G. Wells"))
print(valid_name("H Wells"))
print(valid_name("Herb. Wells"))
print(valid_name("H. George Wells"))
print(valid_name("Herbert George W."))
