def add_bill(bills_strings):
    bills_strings = bills_strings.split(",")
    sum_bills = 0
    for bill in bills_strings:
        if bill[0] == "d":
            if bill[-1] == "k":
                sum_bills += int(bill[1:-1]) * 1000
            else:
                sum_bills += int(bill[1:])
    return sum_bills


print(add_bill("d20,p40,p60,d50"))
print(add_bill("p30,d20,p60,d150,p360"))
print(add_bill("p30,d2k,p60,d200,p360"))
print(add_bill("d100k"))
print(add_bill("d20k,d100,p40"))
