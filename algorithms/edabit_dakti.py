def dakiti(sentence):
    separated_words = separate_words(sentence)
    sorted_words = [""] * len(separated_words)
    for word in separated_words:
        for char in word:
            if char.isdigit():
                index = int(char) - 1
                cleaned_word = word.replace(char, "")
                sorted_words[index] = cleaned_word
                break
    resulting_sentence = form_sentence(sorted_words)
    return resulting_sentence


def separate_words(text):
    words = []
    current_word = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            words.append(current_word)
            current_word = ""
        elif i == len(text) - 1:
            current_word += text[i]
            words.append(current_word)
        else:
            current_word += text[i]
    return words


def form_sentence(words):
    sentence = ""
    for i in range(len(words) - 1):
        sentence += words[i] + " "
    sentence += words[-1]
    return sentence


print(dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves"))
print(dakiti('h4as don2de ah1i n3o ll5egado q7ue 8yo te9-llevare s6abes'))
print(dakiti("quie3res bebe4r dime1 e5s qu6e qu2e tu7 er8es m9i-bebe"))
print(dakiti('y1 de2 nos3tros qu4ien v5a a6 h7ablar 8si 9no'))
print(dakiti('no1 n2os v4er de3jamos'))
