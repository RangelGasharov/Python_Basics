def battle_outcome(number):
    number = str(number)
    result_string = ""
    for i in range(0, len(number) - 1, 2):
        result_string += (int(number[i]) > int(number[i + 1])) * number[i] + (int(number[i]) < int(number[i + 1])) * \
                         number[i + 1]
    if len(number) % 2 != 0:
        result_string += number[-1]
    return result_string


print(battle_outcome(578921445))
print(battle_outcome(111))
print(battle_outcome(78925))
print(battle_outcome(93552129))
print(battle_outcome(3245196))
print(battle_outcome(76811))
print(battle_outcome(5289))
