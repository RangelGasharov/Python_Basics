def simplify_sqrt(number):
    divisors = get_divisors(number)
    multiplication = 1
    square_root_number = number
    index_last_pair = -1
    for i in range(1, len(divisors)):
        if divisors[i] == divisors[i - 1] and (i - 1) != index_last_pair:
            index_last_pair = i
            multiplication *= divisors[i]
            square_root_number /= divisors[i] * divisors[i]
    return [multiplication, int(square_root_number)]


def get_divisors(number):
    divisors = []
    i = 2
    while number > 1:
        if number % i == 0:
            divisors.append(i)
            number /= i
        else:
            i += 1
    return divisors


print(simplify_sqrt(72))
print(simplify_sqrt(160))
print(simplify_sqrt(36))
print(simplify_sqrt(35))
print(simplify_sqrt(100000))
