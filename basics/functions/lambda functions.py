def add(x, y):
    return x + y


sum = add(3, 5)
print(sum)

sum = lambda x, y: x + y
print(sum(3, 5))


def starts_with_A(s):
    return s[0] == 'A'


fruits = ['Apple', 'Pear', 'Apricot', 'Orange', 'Banana']
for fruit in fruits:
    print(fruit, "begins with A?:", starts_with_A(fruit))

map_object = map(starts_with_A, fruits)
print(list(map_object))

map_object_with_lambda = map(lambda fruit: fruit[0] == 'A', fruits)
print(list(map_object_with_lambda))

filter_object = filter(starts_with_A, fruits)
print(list(filter_object))

filter_object_with_lambda = filter(lambda fruit: fruit[0] == 'A', fruits)
print(list(filter_object_with_lambda))

from functools import reduce

numbers = [2, 4, 7, 3]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
