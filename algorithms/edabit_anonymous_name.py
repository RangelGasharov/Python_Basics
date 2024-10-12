def is_correct_aliases(names, anonymous_names):
    for i in range(len(names)):
        letter_needed = names[i][0]
        anonymous_name = anonymous_names[i]
        if anonymous_name[0] != letter_needed:
            return False
        for j in range(1, len(anonymous_name)):
            if anonymous_name[j - 1] == " ":
                if anonymous_name[j] != letter_needed:
                    return False
                else:
                    break
    return True


print(is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."],
                         ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"]))
print(is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."],
                         ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"]))
print(is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]))
print(is_correct_aliases(['Bella T.', 'Tom H.', 'Ben C.'], ['Beautiful Barn', 'Talented Tapestry', 'Cool Bamboo']))
print(is_correct_aliases(['Bella T.', 'Tom H.', 'Ben C.'], ['Beautiful Barn', 'Talented Tapestry', 'Bountiful Bamboo']))
