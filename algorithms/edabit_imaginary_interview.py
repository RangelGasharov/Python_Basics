def interview(times, total_time):
    limit_total_time = 120
    amount_of_questions = 8
    given_times = [5, 10, 15, 20]

    if total_time > limit_total_time:
        return "disqualified"
    if amount_of_questions > len(times):
        return "disqualified"
    for i in range(0, len(times)):
        if times[i] > given_times[int(i / 2)]:
            return "disqualified"
    return "qualified"


print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
