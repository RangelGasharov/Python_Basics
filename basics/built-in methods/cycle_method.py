import time
from itertools import cycle

lights = [
    ("Green", 2), ("Yellow", 1), ("Red", 2)
]

colors = cycle(lights)
while True:
    color, seconds = next(colors)
    print(color)
    time.sleep(seconds)
