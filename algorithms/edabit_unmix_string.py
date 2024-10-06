def unmix(string_combination):
    resulting_string = []
    for i in range(0, len(string_combination) - 1, 2):
        resulting_string.append(string_combination[i + 1])
        resulting_string.append(string_combination[i])
    if len(string_combination) % 2 != 0:
        resulting_string.append(string_combination[-1])
    return "".join(resulting_string)


print(unmix("123456"))
print(unmix("hTsii  s aimex dpus rtni.g"))
print(unmix("badce"))
print(unmix(' Imaf eeilgna l tilt eidzz!y'))
print(unmix(''))
