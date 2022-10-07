while True:
    try:
        number = int(input("Please write down an integer for the collatz conjecture. \n"))
        break
    except ValueError:
        print("Sorry your input is invalid! Write down an integer!")
        continue

while True:
    if number == 1:
        break
    elif number % 2 == 0:
        number /= 2
    else:
        number = number * 3 + 1
    print(number)
