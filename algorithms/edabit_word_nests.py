def valid_word_nest(word, word_nest):
    if len(word_nest) < len(word):
        return False
    if word_nest == word:
        return True
    i = 0
    while i <= len(word_nest) - len(word):
        if word_nest[i:i + len(word)] == word:
            for j in range(i + 1, len(word_nest) - len(word) + 1):
                if word_nest[j:j + len(word)] == word:
                    return False
            word_nest = word_nest[:i] + word_nest[i + len(word):]
            i = 0
        i += 1
    return word_nest == word


print(valid_word_nest("deep", "deep"))
print(valid_word_nest("novel", "nonnonovnovnovelelelvelovelvel"))
print(valid_word_nest("station", "ststatstasstatistationontationtionionation"))
print(valid_word_nest("show", "sshssshowhowhowowhow"))
print(valid_word_nest("salt", "ssaltalt"))
print(valid_word_nest("current", "currccurrcurcurrcucucurrentrrentrrententrententurrentent"))
print(valid_word_nest("broadcast", "broadcbroadcastbroadcastast"))
print(valid_word_nest("undermine", "undermiundermundermiunununderundermineminederminedermineneinene"))
print(valid_word_nest("feed", "feefeeded"))
