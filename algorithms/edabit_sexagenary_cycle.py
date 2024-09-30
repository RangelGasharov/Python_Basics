def sexagenary(year):
    stems = ["Wood", "Fire", "Earth", "Metal", "Water"]
    branches = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"]
    start_year = 1984
    stems_years = 2
    branches_years = 12
    return f"{stems[(int((year - start_year - 1 * (year < start_year)) / stems_years)) % len(stems)]} " \
           f"{branches[(year - start_year) % branches_years]}"


print(sexagenary(1927))
print(sexagenary(1942))
print(sexagenary(1958))
print(sexagenary(1971))
print(sexagenary(1974))
print(sexagenary(1982))
print(sexagenary(1983))
print(sexagenary(1984))
print(sexagenary(2000))
print(sexagenary(2017))
