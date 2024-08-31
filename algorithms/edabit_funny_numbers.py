def funny_numbers(num, power):
    number_as_string = str(num)
    resulting_number = 0
    for i in number_as_string:
        resulting_number += int(i) ** power
        power += 1
    if resulting_number % num == 0:
        return int(resulting_number / num)
    return None


print(funny_numbers(89, 1))
print(funny_numbers(135, 1))
print(funny_numbers(695, 2))
print(funny_numbers(2697, 3))
print(funny_numbers(10383, 6))
print(funny_numbers(92, 1))
print(funny_numbers(46288, 5))
print(funny_numbers(3456789, 5))
