def uncensor(text, vowels):
    index_vowels = 0
    new_string = ""
    for x in text:
        if x == "*":
            new_string += vowels[index_vowels]
            index_vowels += 1
        else:
            new_string += x

    return new_string


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))
