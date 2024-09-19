def grab_number_sum(text):
    numbers = []
    current_number = ""
    for i in range(len(text)):
        if text[i].isnumeric():
            current_number += text[i]
        elif not text[i].isnumeric() and current_number != "":
            numbers.append(int(current_number))
            current_number = ""
        if i == len(text) - 1:
            if current_number.isnumeric():
                numbers.append(int(current_number))
    sum_numbers = 0
    for num in numbers:
        sum_numbers += num
    return sum_numbers


print(grab_number_sum("aeiou5abc10"))
print(grab_number_sum("75shugeb15hvyff15"))
print(grab_number_sum("aeiou250abc10"))
print(grab_number_sum("one1two2twenty20"))
print(grab_number_sum("900uwu50uwuuwuuwu25uwu25"))
print(grab_number_sum("75"))
