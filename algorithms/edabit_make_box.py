def make_box(num):
    box_components = []
    if num == 1:
        box_components.append("#")
        return box_components
    for i in range(1, num + 1):
        if i == 1 or i == num:
            box_components.append("#" * num)
        else:
            box_components.append("#" + " " * (num - 2) + "#")
    return box_components


def print_box(box):
    for x in box:
        print(x)


print_box(make_box(1))
print_box(make_box(2))
print_box(make_box(3))
print_box(make_box(4))
print_box(make_box(5))
print_box(make_box(6))
