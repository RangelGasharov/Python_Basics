def valid_credit_card(credit_card_number):
    credit_card_number = str(credit_card_number)
    digits = []
    for i in range(len(credit_card_number)):
        current_digit = int(credit_card_number[-(i + 1)])
        if i % 2 == 1:
            current_digit *= 2
            digits.append(current_digit - 9 * (current_digit > 9))
        else:
            digits.append(current_digit)
    sum_digits = 0
    for digit in digits:
        sum_digits += digit
    return sum_digits % 10 == 0


print(valid_credit_card(4111111111111111))
print(valid_credit_card(6451623895684318))
print(valid_credit_card(6011000000000004))
print(valid_credit_card(7777777777777777))
print(valid_credit_card(5500000000000004))
print(valid_credit_card(378282246310005))
