def currently_winning(scores):
    result = []
    current_own_points = 0
    current_opponent_points = 0
    for i in range(0, len(scores) - 1, 2):
        current_own_points += scores[i]
        current_opponent_points += scores[i + 1]
        if current_own_points > current_opponent_points:
            result.append("Y")
        elif current_own_points == current_opponent_points:
            result.append("T")
        else:
            result.append("O")
    return result


print(currently_winning([10, 10, 22, 30, 5, 40]))
print(currently_winning([5, 1, 2, 10]))
print(currently_winning([10, 10, 5, 5, 2, 2, 1, 3, 100, 5]))
print(currently_winning([5, 15, 17, 35, 16, 40, 66, 12, 10, 9]))
print(currently_winning([33, 22, 4, 9, 12, 15, 32, 7, 9, 10, 70, 100]))
