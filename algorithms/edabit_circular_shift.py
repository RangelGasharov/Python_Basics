def circular_shift(arr1, arr2, n):
    if len(arr1) != len(arr2):
        return False
    n = n % len(arr1) if arr1 else 0
    arr1_shifted = arr1[-n:] + arr1[:-n]
    return arr1_shifted == arr2


print(circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2))
print(circular_shift([1, 1], [1, 1], 6))
print(circular_shift([0, 1, 2, 3, 4, 5], [3, 4, 5, 2, 1, 0], 3))
print(circular_shift([0, 1, 2, 3], [1, 2, 3, 1], 1))
print(circular_shift(list(range(32)), list(range(32)), 0))
print(circular_shift([1, 2, 1], [1, 2, 1], 3))
