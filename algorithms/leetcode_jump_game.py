def jump_game(nums):
    max_reachable = 0
    for i in range(len(nums)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])
    return True


print(jump_game([2, 3, 1, 1, 4]))
print(jump_game([3, 2, 1, 0, 4]))
print(jump_game([3, 2, 1, 1, 4]))
print(jump_game([4, 3, 2, 1, 6]))
print(jump_game([1, 1, 100]))
