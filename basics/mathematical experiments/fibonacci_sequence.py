from functools import reduce


def get_array_fibonacci_sequence(amount_of_elements):
    a = [1, 1]
    for i in range(0, amount_of_elements):
        b = a[-1] + a[-2]
        a.append(b)
    return a[0:amount_of_elements]


def get_sum_array(array):
    sum_array = reduce(lambda x, y: x + y, array)
    return sum_array


array_fibonacci = get_array_fibonacci_sequence(8)
print(array_fibonacci)
print(get_sum_array(array_fibonacci))
