def find_cross_sum(number):
    print("The cross sum of the number " + str(number), end=' ')
    cross_sum = 0
    for digit in str(number):
        cross_sum += int(digit)
    return print("is " + str(cross_sum))


num = 8246
find_cross_sum(num)
