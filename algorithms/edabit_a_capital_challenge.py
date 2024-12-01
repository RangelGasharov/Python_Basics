def select_letters(s1, s2):
    min_length = min(len(s1), len(s2))
    result_string = ""
    for i in range(min_length):
        if s2[i].isupper():
            result_string += s1[i]
    for i in range(min_length):
        if s1[i].isupper():
            result_string += s2[i]
    return result_string


print(select_letters("heLLO", "GUlp"))
print(select_letters("1234567", "XxXxX"))
print(select_letters("EVERYTHING", "SomeThings"))
print(select_letters("PaTtErN", "pAtTeRn"))
print(select_letters("nothing", "nothing"))
print(select_letters("What do you think of it so far?", "RUBBISH!"))
