def bed_time(*args):
    times_to_sleep = []
    for time_range in args:
        hours_end, minutes_end = get_hours_minutes(time_range[0])
        hours_to_sleep, minutes_to_sleep = get_hours_minutes(time_range[1])
        time_to_sleep = get_time_to_sleep(hours_end, minutes_end, hours_to_sleep, minutes_to_sleep)
        times_to_sleep.append(time_to_sleep)
    return times_to_sleep


def get_hours_minutes(time):
    hours, minutes = int(time[0:2]), int(time[3:5])
    return hours, minutes


def get_time_to_sleep(hours_end, minutes_end, hours_to_sleep, minutes_to_sleep):
    minutes_start = minutes_end - minutes_to_sleep
    hours_start = hours_end - hours_to_sleep
    if minutes_start < 0:
        minutes_start += 60
        hours_start -= 1
    if hours_start < 0:
        hours_start += 24
    return get_time_as_string(hours_start, minutes_start)


def get_time_as_string(hours, minutes):
    hours_as_string, minutes_as_string = "", ""
    if hours < 10:
        hours_as_string += "0"
    hours_as_string += str(hours)
    if minutes < 10:
        minutes_as_string += "0"
    minutes_as_string += str(minutes)
    return hours_as_string + ":" + minutes_as_string


print(bed_time(["07:50", "07:50"]))
print(bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]))
print(bed_time(["05:45", "04:00"], ["07:10", "04:30"]))
