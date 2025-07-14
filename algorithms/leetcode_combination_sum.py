def get_combinationsum(candidates, target):
    results = []

    def get_path_recursive(start, remaining, path):
        if remaining == 0:
            results.append(path[:])
            return
        for i in range(start, len(candidates)):
            num = candidates[i]
            if num > remaining:
                break
            path.append(num)
            get_path_recursive(i, remaining - num, path)
            path.pop()

    get_path_recursive(0, target, [])
    return results


print(get_combinationsum([2, 3, 6, 7], 7))
print(get_combinationsum([2, 3, 5], 8))
print(get_combinationsum([2], 8))
print(get_combinationsum([2], 1))
