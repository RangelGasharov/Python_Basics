def will_fit(cargo_available, cargo_space_needed):
    cargo_types = {"S": 50, "M": 100, "L": 200}
    cargo_available_types = sorted(cargo_available, key=lambda kv: cargo_types[kv[0]])
    cargo_available = []
    for cargo in cargo_available_types:
        cargo_available.append(cargo_types[cargo])
    cargo_space_needed = sorted(cargo_space_needed)
    current_available_index = 0
    current_needed_index = 0
    current_capacity = cargo_available[0]
    is_going = True
    while is_going:
        if current_needed_index > len(cargo_space_needed) - 1:
            return True
        if current_available_index > len(cargo_available) - 1:
            return False
        if current_capacity >= cargo_space_needed[current_needed_index]:
            current_capacity -= cargo_space_needed[current_needed_index]
            current_needed_index += 1
        else:
            current_available_index += 1
            if current_available_index <= len(cargo_available) - 1:
                current_capacity = cargo_available[current_available_index]
            else:
                return False
    return False


print(will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]))
print(will_fit(["L", "L", "M"], [56, 62, 84, 90]))
print(will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70, 80, 90, 200]))
print(will_fit(["S", "L"], [73, 87, 95, 229]))
print(will_fit(["L", "L", "L", "L"], [54, 54, 200, 200, 200]))
