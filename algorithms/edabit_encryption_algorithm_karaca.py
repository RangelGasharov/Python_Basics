def encrypt(string):
    result = "".join(reversed(string))
    vowels_chart = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    translation_table = result.maketrans(vowels_chart)
    return result.translate(translation_table) + "aca"


print(encrypt("apple"))
print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
