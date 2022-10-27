a = float(input("Choose the number you want to calculate the square root of. \n"))
b = float(input("Choose a starting point. \n"))
for i in range(0, 10):
    b = 0.5 * (b + a / b)
    print(" ", i, " ", b)
