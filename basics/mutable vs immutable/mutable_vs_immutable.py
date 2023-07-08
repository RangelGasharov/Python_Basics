# immutable
tuple1 = (1, 2)
tuple2 = tuple1
tuple1 = (1, 2, 3)
print(tuple1, tuple2)
# mutable
list1 = [1, 2]
list2 = list1
list1[0] = 100
# both list1 and list2 are referencing the same object
print(list1, list2)


def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers[-n:]


nums = [1, 456, 9, 18, 99, 766, 45, 32, 129]

print(nums)
largest = get_largest_numbers(nums, 3)
# nums list gets modified in the function (sort statement) --> mutable
print(nums)
print(largest)
