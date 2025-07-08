def get_divisibility_rule(num):
    number_constant = get_number_constant(num)
    while True:
        new_constant = get_number_constant(number_constant)
        if number_constant == new_constant:
            return number_constant
        else:
            number_constant = new_constant


def get_number_constant(num):
    number_list = get_number_list(num)
    number_constant = get_sum_of_products(number_list)
    return number_constant


def get_number_list(num):
    num_list = []
    for char in str(num):
        num_list.append(int(char))
    return num_list


def get_sum_of_products(num_list):
    constants = [1, 10, 9, 12, 3, 4, 1]
    products = []
    for i in range(len(num_list)):
        products.append(num_list[-(i + 1)] * constants[i % 6])
    return sum(products)


print(get_divisibility_rule(85299258))
