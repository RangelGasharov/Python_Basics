def clock(time):
    time_separated = get_separated_time(time)
    hours = time_separated[0]
    minutes = time_separated[1]
    seconds = time_separated[2]
    angle_hours, angle_minutes = get_angles_of_time(hours, minutes, seconds)
    angle_between_1 = abs(angle_hours - angle_minutes)
    angle_between_2 = 360 - angle_between_1
    return round(min(angle_between_1, angle_between_2), 3)


def get_separated_time(time):
    time_separated = []
    current_number = ""
    for i in range(0, len(time)):
        if time[i] == ":":
            time_separated.append(int(current_number))
            current_number = ""
        elif i == len(time) - 1:
            current_number += time[i]
            time_separated.append(int(current_number))
        else:
            current_number += time[i]
    return time_separated


def get_angles_of_time(hours, minutes, seconds):
    if hours >= 12:
        hours -= 12
    angle_minutes = (minutes / 60 + seconds / 3600) * 360
    angle_hours = (hours / 12 + minutes / (12 * 60) + seconds / (12 * 3600)) * 360
    return angle_hours, angle_minutes


print(clock("12:00:00"))
print(clock("12:15:00"))
print(clock("12:32:44"))
print(clock("03:33:33"))
print(1 / 60 * 360 - 1 / 3600 * 360)
