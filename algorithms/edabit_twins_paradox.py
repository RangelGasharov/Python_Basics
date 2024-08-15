import math


def twins(twins_age, distance, speed):
    lorentz_factor = math.sqrt(1 - speed ** 2)
    age_of_jack = round(2 * distance / speed * lorentz_factor + twins_age, 1)
    age_of_jill = round(2 * distance / speed + twins_age,1)
    result = f"Jack's age is {age_of_jack}, Jill's age is {age_of_jill}"
    return result


print(twins(20, 10, 0.4))
print(twins(20, 10, 0.8))
print(twins(10, 16.73, 0.999))
print(twins(25, 30, 0.99999))
