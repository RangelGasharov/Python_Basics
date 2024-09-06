def unique_fract():
    sum_unique_fractions = 0
    for denominator in range(2, 10):
        for numerator in range(1, denominator):
            shares_multiple = False
            for i in range(2, denominator):
                if denominator % i == 0 and numerator % i == 0:
                    shares_multiple = True
                    break
            sum_unique_fractions += (numerator / denominator) * (not shares_multiple)
    return sum_unique_fractions


print(unique_fract())
