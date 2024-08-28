def route_diff(directions_list):
    steps_own_route = len(directions_list)
    directions = {"N": 0, "E": 0, "S": 0, "W": 0}
    for direction in directions_list:
        directions[direction] += 1
    steps_not_needed = 2 * (directions["N"] > directions["S"]) * (directions["S"])
    steps_not_needed += 2 * (directions["S"] >= directions["N"]) * (directions["N"])
    steps_not_needed += 2 * (directions["E"] > directions["W"]) * (directions["W"])
    steps_not_needed += 2 * (directions["W"] >= directions["E"]) * (directions["E"])
    steps_optimal_route = steps_own_route - steps_not_needed
    return steps_own_route - steps_optimal_route


print(route_diff(["N", "E", "S", "W"]))
print(route_diff(["N", "N", "N", "E", "N", "E"]))
print(route_diff(["N", "S", "N", "S", "E", "W", "E", "E"]))
print(route_diff(['S', 'S', 'S', 'S', 'S', 'N']))
print(route_diff(['S', 'S', 'S']))
print(route_diff(['N', 'N', 'S', 'S', 'S', 'S', 'E']))
