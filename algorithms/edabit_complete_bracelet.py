def complete_bracelet(bracelet_list):
    if len(bracelet_list) < 4:
        return False
    for i in reversed(range(2, int(len(bracelet_list) / 2) + 1)):
        if len(bracelet_list) % i != 0:
            continue
        current_pattern = bracelet_list[0:int(len(bracelet_list) / i)]
        if current_pattern * (len(bracelet_list) // len(current_pattern)) == bracelet_list:
            return True
    return False


print(complete_bracelet([2, 2, 1, 1, 2, 2, 1, 1]))
print(complete_bracelet([4, 4, 3, 4, 4, 4, 4, 3, 4, 4]))
print(complete_bracelet([1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2]))
print(complete_bracelet([5, 2, 5, 5, 2, 5, 2, 5, 2, 2, 5, 2, 5, 2, 5, 5, 2, 5, 2, 5, 2, 2, 5, 2]))
print(complete_bracelet([1, 2, 2, 2, 1, 2, 2, 2, 1]))
print(complete_bracelet([1, 1, 6, 1, 1, 7]))
print(complete_bracelet([5, 5, 7, 7]))
