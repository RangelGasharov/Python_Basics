import json
import random

with open("vocabularies.json", "r") as file:
    units = json.load(file)


def get_vocabularies_by_unit_id(unit_id, units):
    for i in range(len(units)):
        if units[i]["unit_id"] == unit_id:
            return units[i]["vocabularies"]
    return []


def add_vocabularies_correct_answers_amount(vocabularies):
    for i in range(len(vocabularies)):
        vocabularies[i].append(0)
    return vocabularies


def get_random_index(length):
    return int(round(random.random() * length, 0))


def start_vocabulary_check():
    is_choosing_unit = True
    vocabularies_of_unit = []
    while is_choosing_unit:
        unit_index = "UNIT_" + input("Give the number of the unit you would like to get the vocabularies from: ")
        vocabularies_of_unit = get_vocabularies_by_unit_id(unit_index, units)
        if len(vocabularies_of_unit) > 0:
            is_choosing_unit = False
        else:
            print("There seems to be no vocabularies for the given unit. Try out another unit.")
    vocabularies_to_learn = add_vocabularies_correct_answers_amount(vocabularies_of_unit)
    while len(vocabularies_to_learn) > 0:
        random_index = get_random_index(len(vocabularies_to_learn) - 1)
        random_vocabulary = vocabularies_to_learn[random_index]
        user_answer = input(f"What is the translation of the following phrase: {random_vocabulary[1]}?\n")
        if user_answer == random_vocabulary[0]:
            random_vocabulary[2] += 1
        else:
            print(f"The answer is sadly false. The right answer would be: {random_vocabulary[0]}")
            random_vocabulary[2] -= 1
        if random_vocabulary[2] == 3:
            del vocabularies_to_learn[random_index]
    print("Unit finished!")


start_vocabulary_check()
