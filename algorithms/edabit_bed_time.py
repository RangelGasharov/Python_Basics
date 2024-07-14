def bed_time(times_list):
    times_to_sleep = []
    for time_range in times_list:
        hours_end, minutes_end = get_hours_minutes(time_range[0])
        hours_to_sleep, minutes_to_sleep = get_hours_minutes(time_range[1])
        time_to_sleep = get_time_to_sleep(hours_end, minutes_end, hours_to_sleep, minutes_to_sleep)
        times_to_sleep.append(time_to_sleep)
    return times_to_sleep


def get_hours_minutes(time):
    hours, minutes = int(time[0:2]), int(time[3:5])
    return hours, minutes


def get_time_to_sleep(hours_end, minutes_end, hours_to_sleep, minutes_to_sleep):
    return 0


print(get_hours_minutes("10:20"))
print(bed_time([["07:50", "07:50"], ["08:00", "10:00"], ["09:00", "9:00"]]))
