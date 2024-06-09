def add(str1, str2):
    if str1 is None or str2 is None:
        return "Invalid Operation"
    if str1 == "" or str2 == "":
        return "Invalid Operation"
    sum_strings = int(str1) + int(str2)
    return str(sum_strings)


print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))
