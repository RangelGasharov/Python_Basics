def driver_license(name, available_agents, other_people):
    time = 20
    current_rank = 1
    people_list = separate_words(other_people) + [name]
    people_list.sort()
    for i in range(len(people_list)):
        if people_list[i] == name:
            current_rank += i
            break
    time_needed = time * max((current_rank - available_agents), 0) + time
    return time_needed


def separate_words(text):
    words = []
    current_word = ""
    for i in range(0, len(text)):
        if text[i] == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += text[i]
    words.append(current_word)
    return words


print(driver_license("Eric", 2, "Adam Caroline Rebecca Frank"))
print(driver_license("Zebediah", 1, "Bob Jim Becky Pat"))
print(driver_license("Aaron", 3, "Jane Max Olivia Sam"))
print(driver_license("Zebediah", 4, "Bob Jim Becky Pat"))
print(driver_license("Zebediah", 5, "Bob Jim Becky Pat"))
