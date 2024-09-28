def num_to_eng(num):
    if num == 0:
        return "zero"
    numbers_names = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"
    }
    numbers_names_reversed = dict(reversed(list(numbers_names.items())))
    number_words = []
    if int(num / 100) > 0:
        number_words.append(numbers_names[int(num / 100)])
        number_words.append(numbers_names[100])
        num = num % 100
    for number_value, number_name in numbers_names_reversed.items():
        if num == 0:
            break
        if num >= number_value:
            num -= number_value
            number_words.append(numbers_names_reversed[number_value])
    number_as_english_word = ""
    for i in range(len(number_words) - 1):
        number_as_english_word += number_words[i] + " "
    number_as_english_word += number_words[-1]
    return number_as_english_word


print(num_to_eng(0))
print(num_to_eng(18))
print(num_to_eng(26))
print(num_to_eng(106))
print(num_to_eng(126))
print(num_to_eng(199))
print(num_to_eng(519))
print(num_to_eng(909))
print(num_to_eng(999))
