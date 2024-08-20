def dif_ciph(word):
    result = ""
    if type(word) == str:
        result = encrypt(word)
    if type(word) == list:
        result = decrypt(word)
    return result


def encrypt(word):
    result = [ord(word[0])]
    for i in range(1, len(word)):
        result.append(ord(word[i]) - ord(word[i - 1]))
    return result


def decrypt(word_code):
    result = chr(word_code[0])
    current_char_code = word_code[0]
    for i in range(1, len(word_code)):
        current_char_code += word_code[i]
        result += str(chr(current_char_code))
    return result


print(dif_ciph("Hello"))
print(dif_ciph("How are you?"))
print(dif_ciph("?"))
print(dif_ciph("Sunshine"))
print(dif_ciph(dif_ciph("Double test!")))
print(dif_ciph(
    [84, 27, -2, 2, 3, 0, -3, 8, -75, -12, 19, -19, 80, -3, -77, 73, 5, -78, 84, -12, -3, -69, 71, -6, 17, -14, 1, 9,
     -64]))
print(dif_ciph([72, 33, -73, 84, -12, -3, 13, -13, -68]))
print(dif_ciph(
    [84, 20, -3, -69, 78, -9, 4, -2, 1, -6, 13, 6, -3, 1, -83, 65, 17, -13, -69, 83, 1, -2, -17, 13, -7, -2, -55, 0]))
