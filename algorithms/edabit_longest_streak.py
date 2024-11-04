def longest_streak(dates):
    amount_longest_streak = 1
    current_streak = 1
    dates_evaluated = []
    for date in dates:
        dates_evaluated.append(evaluate_date_string(date))
    for i in range(1, len(dates_evaluated)):
        if dates_evaluated[i][0] != dates_evaluated[i - 1][0]:
            current_streak = 1
            continue
        if dates_evaluated[i][1] != dates_evaluated[i - 1][1]:
            current_streak = 1
            continue
        if dates_evaluated[i][2] == dates_evaluated[i - 1][2] + 1:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > amount_longest_streak:
            amount_longest_streak = current_streak
    return amount_longest_streak


def evaluate_date_string(date_string):
    date_split = date_string["date"].split("-")
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])
    return [year, month, day]


print(longest_streak([{"date": "2019-09-18"}, {"date": "2019-09-19"}, {"date": "2019-09-20"},
                      {"date": "2019-09-26"}, {"date": "2019-09-27"}, {"date": "2019-09-30"}]))
print(longest_streak([{"date": "2019-09-18"}, {"date": "2019-09-19"}, {"date": "2019-09-20"},
                      {"date": "2019-09-21"}, {"date": "2019-09-22"}, {"date": "2019-09-23"}]))
