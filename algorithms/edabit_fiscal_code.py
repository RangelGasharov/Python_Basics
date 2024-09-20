vowels = {"a", "e", "i", "o", "u"}


def fiscal_code(person_information):
    person_surname = person_information["surname"]
    person_name = person_information["name"]
    person_gender = person_information["gender"]
    person_date_of_birth = person_information["dob"]


def get_surname_code(surname):
    word_consonants = []
    word_vowels = []
    for letter in surname:
        if letter.lower() not in vowels:
            word_consonants.append(letter.upper())
        else:
            word_vowels.append(letter.upper())
    if len(surname) < 3:
        result = ""
        if len(word_consonants) > 0:
            for letter in word_consonants:
                result += letter
        if len(word_vowels) > 0:
            for letter in word_vowels:
                result += letter
        result += "X" * (3 - len(surname))
        return result

    if len(word_consonants) >= 3:
        return "".join(word_consonants[:3])
    else:
        result = ""
        if len(word_consonants) > 0:
            for letter in word_consonants:
                result += letter
        if len(word_vowels) > 0:
            for i in range(0, 3 - len(word_consonants)):
                result += word_vowels[i]
        return result


def get_name_code(name):
    word_consonants = []
    word_vowels = []
    for letter in name:
        if letter.lower() not in vowels:
            word_consonants.append(letter.upper())
        else:
            word_vowels.append(letter.upper())

    if len(name) < 3:
        result = ""
        if len(word_consonants) > 0:
            for letter in word_consonants:
                result += letter
        if len(word_vowels) > 0:
            for letter in word_vowels:
                result += letter
        result += "X" * (3 - len(name))
        return result

    if len(word_consonants) == 3:
        return "".join(word_consonants[:3])
    elif len(word_consonants) > 3:
        return word_consonants[0] + word_consonants[2] + word_consonants[3]
    else:
        result = ""
        if len(word_consonants) > 0:
            for letter in word_consonants:
                result += letter
        if len(word_vowels) > 0:
            for i in range(0, 3 - len(word_consonants)):
                result += word_vowels[i]


def get_birth_gender_code(gender, date_of_birth):
    return ""


print(get_surname_code("Curie"))
print(get_name_code("Brendan"))
