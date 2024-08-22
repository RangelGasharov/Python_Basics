def we_have_house(side_wall_height, house_width, house_length, roof_wall_height):
    max_allowed_height = 20
    garden_size = 50
    garden_path_size = 3
    door_height = 7
    door_width = 3
    window_height = 3
    window_width = 4
    window_area = window_width * window_height
    height_gray_paint = 2

    if house_width > garden_size - 2 * garden_path_size or house_length > garden_size - 2 * garden_path_size:
        return "House too big."
    if side_wall_height + roof_wall_height > max_allowed_height:
        return "No permission."
    if 2 * window_width + door_width + 4 > house_width or 2 * window_width + 3 > house_length:
        return "House too small."
    if door_height > side_wall_height:
        return "House too small."
    gray_paint_area = 2 * height_gray_paint * house_width - door_width * height_gray_paint + \
                      2 * height_gray_paint * house_length
    yellow_paint_area = 2 * (side_wall_height - height_gray_paint) * house_length - 4 * window_area + \
                        2 * house_width * (side_wall_height - height_gray_paint) - 4 * window_area - (
                                door_height - height_gray_paint) * door_width + house_width * roof_wall_height
    return f"Yellow: {yellow_paint_area}, Gray: {gray_paint_area}"


print(we_have_house(8, 30, 32, 8))
print(we_have_house(9, 14, 20, 9))
print(we_have_house(10, 31, 30, 11))
print(we_have_house(10, 40, 40, 10))
print(we_have_house(9, 38, 36, 9))
print(we_have_house(8, 15, 12, 6))
print(we_have_house(8, 30, 45, 6))
print(we_have_house(9, 20, 14, 8))
