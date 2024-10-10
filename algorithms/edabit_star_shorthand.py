def to_star_shorthand(text):
    if len(text) < 1:
        return ""
    shorthand_string = ""
    current_count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            current_count += 1
        else:
            if current_count > 1:
                shorthand_string += f"{text[i]}*{current_count}"
                current_count = 1
            else:
                shorthand_string += text[i]
    if current_count > 1:
        shorthand_string += f"{text[-1]}*{current_count}"
    else:
        shorthand_string += text[-1]
    return shorthand_string


print(to_star_shorthand("abbccc"))
print(to_star_shorthand("77777geff"))
print(to_star_shorthand("abc"))
print(to_star_shorthand(""))
print(to_star_shorthand("11223344"))
print(to_star_shorthand("haaaappyyyyy"))
