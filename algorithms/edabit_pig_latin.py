def pig_latin(sentence):
    separated_words = separate_words(sentence)
    modified_words = modify_words_pig_latin(separated_words)
    sentence = form_sentence(modified_words, sentence[-1])
    return sentence


def separate_words(text):
    words = []
    current_word = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            words.append(current_word)
            current_word = ""
        elif i == len(text) - 2:
            current_word += text[i]
            words.append(current_word)
        else:
            current_word += text[i]
    return words


def modify_words_pig_latin(words):
    result = []
    vowels = ["a", "e", "i", "o", "u"]
    words[0] = words[0].lower()
    for word in words:
        word_ending = ""
        if word[-1] in vowels:
            word_ending = "way"
        else:
            word_ending = "ay"
        new_word = word[1:] + word[0] + word_ending
        result.append(new_word)
    first_word = result[0]
    first_word = first_word[0].upper() + first_word[1:]
    result[0] = first_word
    return result


def form_sentence(words, ending_sign):
    sentence = ""
    for i in range(len(words) - 1):
        sentence += words[i] + " "
    sentence += words[-1]
    return sentence + ending_sign


print(pig_latin("Cats are great pets."))
print(pig_latin("Tom got a small piece of pie."))
print(pig_latin("He told us a very exciting tale."))
print(pig_latin("A diamond is not enough."))
print(pig_latin("Hurry!"))
