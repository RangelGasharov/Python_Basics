def maximum_seating(seats_list):
    indexes_occupied_seats = []
    total_possible_seats = 0
    for i in range(len(seats_list)):
        if seats_list[i] == 1:
            indexes_occupied_seats.append(i)
    if not indexes_occupied_seats:
        return (len(seats_list) - 1) // 3 + 1
    total_possible_seats += (indexes_occupied_seats[0]) // 3
    total_possible_seats += (len(seats_list) - 1 - indexes_occupied_seats[-1]) // 3
    for i in range(1, len(indexes_occupied_seats)):
        gap = indexes_occupied_seats[i] - indexes_occupied_seats[i - 1] - 1
        if gap >= 5:
            total_possible_seats += get_amount_of_seats(gap)
    return total_possible_seats


def get_amount_of_seats(gap_length):
    if gap_length < 5:
        return 0
    return (gap_length - 2) // 3


print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
print(maximum_seating([0, 0, 0, 0]))
print(maximum_seating([1, 0, 0, 0, 0, 1]))
print(maximum_seating([1, 0, 0, 0, 0, 0, 0, 1]))
print(maximum_seating([1, 0, 0, 0, 0, 1]))
print(maximum_seating([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(maximum_seating([1]))
print(maximum_seating([0]))
print(maximum_seating([0, 0]))
