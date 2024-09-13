def find_broken_keys(initial_phrase, actual_phrase):
    result = []
    for i in range(len(initial_phrase)):
        if initial_phrase[i] != actual_phrase[i]:
            if initial_phrase[i] not in result:
                result.append(initial_phrase[i])
    return result


print(find_broken_keys("happy birthday", "hawwy birthday"))
print(find_broken_keys("starry night", "starrq light"))
print(find_broken_keys("beethoven", "affthoif5"))
