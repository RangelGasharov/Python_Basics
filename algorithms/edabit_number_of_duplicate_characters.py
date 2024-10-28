def duplicate_count(text):
    amount_duplicate_letters = 0
    dictionary = {}
    for letter in text:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    for key, value in dictionary.items():
        amount_duplicate_letters += (value > 1)
    return amount_duplicate_letters


print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("Aa"))
print(duplicate_count("bb2c"))
print(duplicate_count("aa1112"))
print(duplicate_count("indivisibility"))
