def wash_hands(daily_amount, months):
    duration_in_seconds = 21
    month_length = 30
    amount_in_seconds = duration_in_seconds * daily_amount * months * month_length
    minutes = int(amount_in_seconds / 60)
    seconds = amount_in_seconds - minutes * 60
    return f"{minutes} minutes and {seconds} seconds"


print(wash_hands(8, 7))
print(wash_hands(0, 0))
print(wash_hands(7, 9))
print(wash_hands(13, 3))
print(wash_hands(20, 10))
