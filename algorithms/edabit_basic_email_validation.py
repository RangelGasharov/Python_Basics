def validate_email(email_string):
    at_char_index = -1
    dot_index = -1
    for i in range(len(email_string)):
        if email_string[i] == "@":
            at_char_index = i
        if email_string[i] == ".":
            dot_index = i
    if at_char_index < 1:
        return False
    if dot_index <= at_char_index:
        return False
    return True


print(validate_email('@edabit.com'))
print(validate_email('@edabit'))
print(validate_email('matt@edabit.com'))
print(validate_email('hello.gmail@com'))
print(validate_email('bill.gates@microsoft.com'))
print(validate_email('%^%$#%^%'))
print(validate_email('www.email.com'))
print(validate_email('email'))
