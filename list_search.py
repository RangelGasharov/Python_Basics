numbers = [0, 10, 12, 4, 7, 20, 21, 13]
SEARCHED_NUMBER = int(input("Write down the number you are searchin inside the list.\n"))
if SEARCHED_NUMBER in numbers:
    for i in range(len(numbers)):
        if numbers[i] == SEARCHED_NUMBER:
            print("Position of number:", i)
else:
    print("Position of number could not be found.")
