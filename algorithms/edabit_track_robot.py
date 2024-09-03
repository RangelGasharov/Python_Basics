import math


def track_robot(path):
    position = [0, 0]
    current_angle = 0
    directions = {"<": 90, ">": -90}
    for step in path:
        if step == ".":
            position[0] += int(math.cos(current_angle / 180 * math.pi))
            position[1] += int(math.sin(current_angle / 180 * math.pi))
        else:
            current_angle += directions[step]
    return position


print(track_robot("..<.<."))
print(track_robot("<>>>><><<<><>>>><><<<><>>><>"))
print(track_robot(".<..<...<....<.....<......"))
print(track_robot(">>.."))
print(track_robot("..<<..>>..<<..>>.."))
