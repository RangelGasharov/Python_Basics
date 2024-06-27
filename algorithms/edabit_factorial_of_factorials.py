def get_factorial(num):
    if num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)


def fact_of_fact(num):
    result = 1
    for x in range(1, num + 1):
        result *= get_factorial(x)
    return result


print(fact_of_fact(4))
print(fact_of_fact(5))
print(fact_of_fact(6))
