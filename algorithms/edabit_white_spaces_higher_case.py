def insert_whitespace(text):
    if len(text) < 1:
        return ""
    result = text[0]
    for i in range(1, len(text)):
        if text[i].isupper() and text[i - 1].islower():
            result += " "
        result += text[i]
    return result


print(insert_whitespace("SheWalksToTheBeach"))
print(insert_whitespace("MarvinTalksTooMuch"))
print(insert_whitespace("TheGreatestUpsetInHistory"))
