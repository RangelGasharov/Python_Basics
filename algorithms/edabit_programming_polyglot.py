def get_languages(number):
    languages_scores = {"C#": 1, "C++": 2, "Java": 4, "Javascript": 8, "PHP": 16, "Python": 32,
                        "Ruby": 64, "Swift": 128}
    languages_scores_reversed = dict(reversed(list(languages_scores.items())))
    proficient_languages = []
    for language, score in languages_scores_reversed.items():
        if number >= score:
            number -= score
            proficient_languages.append(language)
    proficient_languages.sort()
    return proficient_languages


print(get_languages(12))
print(get_languages(25))
print(get_languages(47))
print(get_languages(53))
print(get_languages(100))
print(get_languages(255))
