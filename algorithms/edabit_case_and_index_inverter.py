def invert(text):
    result = ""
    for i in range(len(text)):
        if text[-i - 1].isupper():
            result += text[-i - 1].lower()
        else:
            result += text[-i - 1].upper()
    return result


print(invert("dLROW YM sI HsEt"))
print(invert("ytInIUgAsnOc"))
print(invert("step on NO PETS"))
print(invert("XeLPMoC YTiReTXeD"))
