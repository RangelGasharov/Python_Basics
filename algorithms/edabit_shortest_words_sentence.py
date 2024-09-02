def find_shortest_words(text):
    shortest_words = []
    separated_words = separate_words(text)
    shortest_length = len(separated_words[0])
    for word in separated_words:
        if len(word) < shortest_length:
            shortest_words = [word.lower()]
            shortest_length = len(word)
        elif len(word) == shortest_length:
            shortest_words.append(word.lower())
    shortest_words.sort()
    return shortest_words


def separate_words(text):
    separated_words = []
    current_word = ""
    for i in range(len(text) - 1):
        if text[i].isalpha():
            current_word += text[i]
        elif text[i] == " ":
            separated_words.append(current_word)
            current_word = ""
    current_word += (text[-1].isalpha()) * text[-1]
    separated_words.append(current_word)
    return separated_words


print(find_shortest_words("I think the solution is fairly obvious."))
print(find_shortest_words("Chase two rabbits, catch none."))
print(find_shortest_words("We become what we think about."))
print(find_shortest_words("The quick brown fox jumped over the lazy dogs back."))
print(find_shortest_words("If you are depressed you are living in the past. If you are anxious you are living in" +
                          " the future. If you are at peace you are living in the present."))
print(find_shortest_words("Remember that happiness is a way of travel, not a destination."))
