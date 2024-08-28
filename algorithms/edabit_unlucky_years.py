from datetime import datetime


def how_unlucky(year):
    amount_of_friday_thirteenth = 0
    for month in range(1, 13):
        date_of_day = datetime(year, month, 13)
        if date_of_day.strftime("%u") == "5":
            amount_of_friday_thirteenth += 1
    return amount_of_friday_thirteenth


print(how_unlucky(2000))
print(how_unlucky(2016))
print(how_unlucky(2020))
print(how_unlucky(2026))
print(how_unlucky(2040))
