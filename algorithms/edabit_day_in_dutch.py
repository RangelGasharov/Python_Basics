from datetime import datetime


def weekday_dutch(date_string):
    dutch_weekdays = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
    dates_array = [int(date) for date in date_string.split()]
    date_day, date_month, date_year = dates_array[0], dates_array[1], dates_array[2]
    date_weekday_integer = datetime(date_year, date_month, date_day).weekday()
    return dutch_weekdays[date_weekday_integer]


print(weekday_dutch("21 9 1970"))
print(weekday_dutch("23 9 1970"))
print(weekday_dutch("2 9 1945"))
print(weekday_dutch("9 11 2001"))
print(weekday_dutch("12 12 1212"))
