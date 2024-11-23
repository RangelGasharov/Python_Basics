def battle(stats):
    hero_hp = stats["pHP"]
    hero_attack = stats["pATT"]
    hero_defense = stats["pDEF"]
    hero_potions_amount = stats["pPOT"]
    monster_hp = stats["mHP"]
    monster_attack = stats["mATT"]
    monster_defense = stats["mDEF"]
    hero_damage = 2 * hero_attack - monster_defense
    monster_damage = 2 * monster_attack - hero_defense
    current_round = 1
    is_going = True
    while is_going:
        if hero_potions_amount > 0 and hero_hp <= 10 and current_round != 1:
            hero_hp += 10
            hero_potions_amount -= 1
            hero_hp -= monster_damage / 2
            if hero_hp <= 0:
                return f"Game Over in {current_round} rounds"
        else:
            monster_hp -= hero_damage
            if monster_hp <= 0:
                return f"Victory in {current_round} rounds"
            hero_hp -= monster_damage
            if hero_hp <= 0:
                return f"Game Over in {current_round} rounds"
        current_round += 1
    return ""


print(battle({"pHP": 10, "pATT": 10, "pDEF": 10, "pPOT": 0, "mHP": 20, "mATT": 6, "mDEF": 14}))
print(battle({"pHP": 10, "pATT": 10, "pDEF": 10, "pPOT": 2, "mHP": 10, "mATT": 8, "mDEF": 14}))
print(battle({"pHP": 12, "pATT": 7, "pDEF": 6, "pPOT": 2, "mHP": 30, "mATT": 8, "mDEF": 10}))
print(battle({"pHP": 100, "pATT": 12, "pDEF": 8, "pPOT": 3, "mHP": 200, "mATT": 14, "mDEF": 8}))
print(battle({"pHP": 300, "pATT": 5, "pDEF": 4, "pPOT": 0, "mHP": 120, "mATT": 10, "mDEF": 6}))
print(battle({"pHP": 1480, "pATT": 16, "pDEF": 16, "pPOT": 4, "mHP": 860, "mATT": 14, "mDEF": 20}))
print(battle({"pHP": 230, "pATT": 3, "pDEF": 20, "pPOT": 2, "mHP": 140, "mATT": 12, "mDEF": 4}))
print(battle({"pHP": 90, "pATT": 9, "pDEF": 10, "pPOT": 8, "mHP": 300, "mATT": 8, "mDEF": 4}))
