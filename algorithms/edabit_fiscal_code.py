vowels = {"a", "e", "i", "o", "u"}
months = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "H", 7: "L", 8: "M", 9: "P", 10: "R", 11: "S", 12: "T"}


def fiscal_code(person_information):
    person_surname = person_information["surname"]
    person_name = person_information["name"]
    person_gender = person_information["gender"]
    person_date_of_birth = person_information["dob"]
    surname_code = get_surname_code(person_surname)
    name_code = get_name_code(person_name)
    birthdate_gender_code = get_birthdate_gender_code(person_gender, person_date_of_birth)
    return surname_code + name_code + birthdate_gender_code


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
        return result


def get_birthdate_gender_code(gender, date_of_birth):
    birthdate_dates = []
    current_date = ""
    for i in range(len(date_of_birth)):
        if date_of_birth[i] == "/":
            birthdate_dates.append(current_date)
            current_date = ""
        else:
            current_date += date_of_birth[i]
    birthdate_dates.append(current_date)
    birthdate_day = birthdate_dates[0]
    birthdate_month = months[int(birthdate_dates[1])]
    birthdate_year = birthdate_dates[2][2:]
    if gender == "M":
        if int(birthdate_day) < 10:
            birthdate_day = "0" + birthdate_day
    else:
        birthdate_day = str(int(birthdate_day) + 40)
    return birthdate_year + birthdate_month + birthdate_day


print(fiscal_code({"name": "Matt", "surname": "Edabit", "gender": "M", "dob": "1/1/1900"}))
print(fiscal_code({"name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950"}))
print(fiscal_code({"name": "Mickey", "surname": "Mouse", "gender": "M", "dob": "16/1/1928"}))
print(fiscal_code({"name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961"}))
print(fiscal_code({"name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899"}))
print(fiscal_code({"name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867"}))
