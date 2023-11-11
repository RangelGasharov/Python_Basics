import time


def get_non_repeating_digits_numbers(numbers_of_digits):
    test_list = []
    for x in range(1234, 10 ** numbers_of_digits):
        test_list.append(x)
    return [sub for sub in test_list if len(set(str(sub))) == len(str(sub))]


start_time = time.time()
result = get_non_repeating_digits_numbers(4)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
