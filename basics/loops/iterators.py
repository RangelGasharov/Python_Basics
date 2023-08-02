i_value = "words"
i_value2 = [10, 2, 9, 14, 83]
i_object = iter(i_value)
i_object2 = iter(i_value2)

while True:
    try:
        item = next(i_object)
        print(item)
        item2 = next(i_object2)
        print(item2)
    except StopIteration:
        print("No more items to iterate over!")
        break
