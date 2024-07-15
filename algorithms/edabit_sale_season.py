import math


def discount(product_prices):
    discount_percentage = get_discount_percentage(product_prices)
    discounted_products = apply_discount(product_prices, discount_percentage)
    return discounted_products


def get_discount_percentage(products):
    sum_prices = sum(products)
    products = sorted(products)
    amount_of_free_products = math.floor(len(products) / 3)
    sum_free_products = sum(products[0:amount_of_free_products])
    return sum_free_products / sum_prices


def apply_discount(products, discount_percentage):
    discounted_products = []
    for x in products:
        discounted_products.append(round(x * (1 - discount_percentage), 2))
    return discounted_products


print(discount([2.99, 5.75, 3.35, 4.99]))
print(discount([10.75, 11.68]))
print(discount([68.74, 17.85, 55.99]))
print(discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]))
