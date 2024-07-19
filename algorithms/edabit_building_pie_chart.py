def pie_chart(values_dictionary):
    sum_dictionary = get_sum_dictionary(values_dictionary)
    new_dictionary = change_dictionary_values(values_dictionary, sum_dictionary)
    return new_dictionary


def change_dictionary_values(values_dictionary, sum_dictionary):
    for x in values_dictionary:
        values_dictionary[x] = round(values_dictionary[x] * 360 / sum_dictionary, 1)
    return values_dictionary


def get_sum_dictionary(values_dictionary):
    sum_values = 0
    for x in values_dictionary:
        sum_values += values_dictionary[x]
    return sum_values


print(pie_chart({"a": 1, "b": 2}))
print(pie_chart({"a": 30, "b": 15, "c": 55}))
print(pie_chart({"a": 8, "b": 21, "c": 12, "d": 5, "e": 4}))
print(pie_chart({"a": 1, "b": 10, "c": 100, "d": 1000, "e": 666}))
