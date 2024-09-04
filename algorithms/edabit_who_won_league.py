teams_table = [
    ['Arsenal', 38, 14, 14, 10, 8],
    ['Aston Villa', 38, 9, 8, 21, -26],
    ['Bournemouth', 38, 9, 7, 22, -26],
    ['Brighton', 38, 9, 14, 15, -15],
    ['Burnley', 38, 15, 9, 14, -7],
    ['Chelsea', 38, 20, 6, 12, 15],
    ['Crystal Palace', 38, 11, 10, 17, -19],
    ['Everton', 38, 13, 10, 15, -12],
    ['Leicester City', 38, 18, 8, 12, 26],
    ['Liverpool', 38, 32, 3, 3, 52],
    ['Manchester City', 38, 26, 3, 9, 67],
    ['Manchester Utd', 38, 18, 12, 8, 30],
    ['Newcastle', 38, 11, 11, 16, -20],
    ['Norwich', 38, 5, 6, 27, -49],
    ['Sheffield Utd', 38, 14, 12, 12, 0],
    ['Southampton', 38, 15, 7, 16, -9],
    ['Tottenham', 38, 16, 11, 11, 14],
    ['Watford', 38, 8, 10, 20, -28],
    ['West Ham', 38, 10, 9, 19, -13],
    ['Wolves', 38, 15, 14, 9, 11]
]


def who_won(table, team_name):
    team_rank = 1
    team_index = -1
    for i in range(len(table)):
        if table[i][0] == team_name:
            team_index = i
            break
    team_points = table[team_index][2] * 3 + table[team_index][3]
    for i in range(team_index):
        points = table[i][2] * 3 + table[i][3]
        team_rank += (points > team_points or (points == team_points and table[i][5] > table[team_index][5]))
    for i in range(team_index + 1, len(table)):
        points = table[i][2] * 3 + table[i][3]
        team_rank += (points > team_points or (points == team_points and table[i][5] > table[team_index][5]))
    team_text = get_team_text(team_name, team_rank, team_points, table[team_index][5])
    return team_text


def get_team_text(team_name, team_rank, team_points, team_goal_difference):
    rank_ending = "th"
    if team_rank > 20 or team_rank < 10:
        if str(team_rank)[-1] == "1":
            rank_ending = "st"
        if str(team_rank)[-1] == "2":
            rank_ending = "nd"
        if str(team_rank)[-1] == "3":
            rank_ending = "rd"
    result_string = f"{team_name} came {team_rank}{rank_ending} with {team_points} and a goal difference of {team_goal_difference}!"
    return result_string


print(who_won(teams_table, "Liverpool"))
print(who_won(teams_table, "Manchester Utd"))
print(who_won(teams_table, "Norwich"))
print(who_won(teams_table, "Tottenham"))
print(who_won(teams_table, "Aston Villa"))
print(who_won(teams_table, "Southampton"))
print(who_won(teams_table, "Manchester City"))
