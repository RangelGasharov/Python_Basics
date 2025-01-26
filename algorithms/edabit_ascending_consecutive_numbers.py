def ascending(number_string):
    current_length = 1
    while True:
        is_consecutive = True
        if current_length > len(number_string) / 2:
            return False
        numbers = []
        for i in range(0, len(number_string), current_length):
            numbers.append(int(number_string[i:i + current_length]))
        for i in range(1, len(numbers)):
            if numbers[i] != numbers[i - 1] + 1:
                is_consecutive = False
                current_length += 1
                break
        if is_consecutive:
            return True


print(ascending("444445"))
print(ascending("123412351236"))
print(ascending("500001500002500003"))
print(ascending("57585960616263"))
print(ascending("35236237238"))
print(ascending("2324256"))
print(ascending("90090190290"))
print(ascending("54321"))
