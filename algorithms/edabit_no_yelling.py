def no_yelling(sentence):
    index_last_mark = len(sentence) - 1
    special_characters = ["?", "!"]
    for i in range(1, len(sentence)+1):
        if sentence[-i] in special_characters and sentence[-(i+1)] not in special_characters:
            index_last_mark = -i
            break
    return sentence[:len(sentence) + index_last_mark + 1]


print(no_yelling("What went wrong?????????"))
print(no_yelling("Oh my goodness!!!"))
print(no_yelling("Oh my goodness!"))
print(no_yelling("I just!!! can!!! not!!! believe!!! it!!!"))
print(no_yelling("That's a ton!! of cheese!!!!"))
print(no_yelling("WHAT?"))
print(no_yelling("What went wrong?????????"))

