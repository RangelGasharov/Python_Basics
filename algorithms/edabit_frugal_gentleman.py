def chosen_wine(wines):
    if len(wines) < 1:
        return None
    if len(wines) == 1:
        return wines[0]["name"]
    cheapest_wine = wines[0]
    second_cheapest_wine = wines[1]
    for i in range(1, len(wines)):
        if wines[i]["price"] < cheapest_wine["price"]:
            second_cheapest_wine = cheapest_wine
            cheapest_wine = wines[i]
        if cheapest_wine["price"] < wines[i]["price"] < second_cheapest_wine["price"]:
            second_cheapest_wine = wines[i]
    return second_cheapest_wine["name"]


print(chosen_wine(
    [{"name": "Wine A", "price": 8.99}, {"name": "Wine 32", "price": 13.99}, {"name": "Wine 9", "price": 10.99}]))
print(chosen_wine(
    [{"name": "Wine A", "price": 8.99}, {"name": "Wine 389", "price": 109.99}, {"name": "Wine 44", "price": 38.44},
     {"name": "Wine 72", "price": 22.77}]))
print(chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine B", "price": 9.99}]))
print(chosen_wine([{"name": "Wine A", "price": 8.99}]))
print(chosen_wine([]))
