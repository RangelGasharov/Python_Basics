def switcheroo(sentence):
    separated_words = separate_words(sentence)
    new_sentence = build_sentence(separated_words)
    return new_sentence


def separate_words(sentence):
    words = []
    current_word = ""
    for i in range(0, len(sentence)):
        if sentence[i] == " ":
            words.append(current_word)
            current_word = ""
        if i == len(sentence) - 1:
            current_word += sentence[i]
            words.append(current_word)
        else:
            current_word += sentence[i]
    return words


def change_special_ending(word):
    length = 3
    separators = [".", ",", "!", "?"]
    if len(word) < length:
        return word
    if word[-length:] == "nce":
        return word.replace("nce", "nts")
    if word[-length:] == "nts":
        return word.replace("nts", "nce")
    offset = len(word) - 1
    if word[offset] in separators:
        while offset - 3 > 0:
            if word[offset - 3:offset] == "nce" and word[offset] in separators:
                return word.replace("nce", "nts")
            if word[offset - 3:offset] == "nts" and word[offset] in separators:
                return word.replace("nts", "nce")
            offset -= 1
    return word


def build_sentence(words):
    sentence = ""
    for i in range(0, len(words)):
        new_word = change_special_ending(words[i])
        sentence += new_word + " "
    return sentence[:-1]


print(switcheroo("The elephants in France were chased by ants!"))
print(switcheroo("While he rants, I fall into a trance..."))
print(switcheroo("Bounced over the fence!"))
print(switcheroo("Face"))
print(switcheroo("Fats"))
print(switcheroo(""))
