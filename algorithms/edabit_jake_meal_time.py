def time_to_eat(time_string):
    times = [7, 12, 19]
    separator_index = time_string.find(":")
    hours = int(time_string[0:separator_index])
    hours += (hours < 12) * 12 * (time_string[-4] == "p") - 12 * (time_string[-4] == "a" and hours == 12)
    minutes = int(time_string[separator_index + 1: separator_index + 3])
    hours_remaining = 0
    minutes_remaining = 0
    for i in range(len(times)):
        if times[i] - hours >= 0:
            minutes_remaining = -minutes
            hours_remaining = times[i] - hours - (minutes_remaining < 0)
            minutes_remaining += (minutes_remaining < 0) * 60
            break
        minutes_remaining = -minutes
        hours_remaining = times[0] - (hours - 24) - (minutes_remaining < 0)
        minutes_remaining += (minutes_remaining < 0) * 60
    return [hours_remaining, minutes_remaining]


print(time_to_eat("2:00 p.m."))
print(time_to_eat("5:50 a.m."))
print(time_to_eat("6:37 p.m."))
print(time_to_eat("12:00 a.m."))
print(time_to_eat("11:58 p.m."))
print(time_to_eat("3:33 p.m."))
