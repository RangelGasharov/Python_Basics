def over_time(info):
    start, end, hourly_rate, overtime_factor = info[0], info[1], info[2], info[3]
    normal_hours = (min(end, 17) - start)
    overtime_hours = (end - 17) * (end > 17)
    payment = round(hourly_rate * (normal_hours + overtime_hours * overtime_factor), 2)
    return "${:0.2f}".format(payment)


print(over_time([9, 17, 30, 1.5]))
print(over_time([16, 18, 30, 1.8]))
print(over_time([13.25, 15, 30, 1.5]))
print(over_time([13, 21, 38.6, 1.8]))
print(over_time([10.5, 17, 32.25, 1.5]))
print(over_time([11.5, 19, 40, 1.8]))
print(over_time([10, 17, 30, 1.5]))
