def censor_string(text, censored_words, char):
    result_string = ""
    current_word = ""
    for i in range(0, len(text)):
        if text[i] == " " or i == len(text) - 1:
            if current_word in censored_words:
                result_string += len(current_word) * char + " "
                current_word = ""
            else:
                result_string += current_word + " "
                current_word = ""
        else:
            current_word += text[i]

    return result_string


print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
