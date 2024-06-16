def ave_spd(up_time, up_spd, down_spd):
    distance_up = up_time / 60 * up_spd
    down_time = distance_up / down_spd
    average_speed = 2 * distance_up / (up_time/60 + down_time)
    return average_speed


print(ave_spd(18, 20, 60))
print(ave_spd(30, 10, 30))
print(ave_spd(30, 8, 24))
