def sun_loungers(lounges_string):
    if len(lounges_string) == 1:
        return (lounges_string[0] == "0") * 1
    if len(lounges_string) < 1:
        return 0
    current_free_space = 0
    free_spaces_zones = []
    total_people = 0
    for i in range(len(lounges_string)):
        if lounges_string[i] == "1":
            free_spaces_zones.append(current_free_space)
            current_free_space = 0
        else:
            current_free_space += 1
    if current_free_space > 0:
        if len(free_spaces_zones) < 1:
            return int((current_free_space + 1) / 2)
        total_people += int(current_free_space / 2)
    for i in range(len(free_spaces_zones)):
        total_people += (int((free_spaces_zones[i] + 1) / 2) - 1) * (free_spaces_zones[i] > 1)
    total_people += lounges_string[0] == "0" * (free_spaces_zones[0] > 1) * (len(lounges_string) >= 5)
    return total_people


print(sun_loungers("10000"))
print(sun_loungers("10001"))
print(sun_loungers("00101"))
print(sun_loungers("0"))
print(sun_loungers("00100"))
print(sun_loungers("0000"))
print(sun_loungers("000"))
print(sun_loungers("001000100000001010001010010000001000101000000"))
print(sun_loungers("010000100000000010010000001010000000010100001000000010010000000001" +
                   "000000001000000010000000100100000000100000100100010000001"))
