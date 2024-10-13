def admirable(number):
    divisors = get_divisors(number)
    sum_divisors = 0
    for divisor in divisors:
        sum_divisors += divisor
    if number == sum_divisors:
        return "Perfect"
    difference_perfect_score = sum_divisors - number
    if difference_perfect_score > 0:
        if difference_perfect_score / 2 in divisors:
            return int(difference_perfect_score / 2)
        else:
            return "Neither"
    else:
        return "Neither"


def get_divisors(number):
    divisors = [1]
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


print(admirable(6))
print(admirable(12))
print(admirable(18))
print(admirable(138))
print(admirable(496))
print(admirable(612))
print(admirable(1876))
print(admirable(5456))
