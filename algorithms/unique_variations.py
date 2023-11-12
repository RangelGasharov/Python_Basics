import time


def get_non_repeating_digits_numbers(numbers_of_digits):
    test_list = []
    starting_point = 0
    for i in range(1, numbers_of_digits + 1):
        starting_point += i * 10 ** (numbers_of_digits - i)
    for x in range(starting_point, 10 ** numbers_of_digits):
        test_list.append(x)
    return [sub for sub in test_list if len(set(str(sub))) == len(str(sub))]


start_time = time.time()
result = get_non_repeating_digits_numbers(4)
end_time = time.time()
elapsed_time = end_time - start_time
print(result)
print(f"{len(result)} variations")
print(f"{elapsed_time} s")
