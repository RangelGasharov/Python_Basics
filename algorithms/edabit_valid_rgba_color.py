def valid_color(rgba_string):
    rgba_string = rgba_string.replace(" ", "").replace("\t", "")
    values_start_index = rgba_string.find("(")
    values_end_index = rgba_string.find(")")
    if values_start_index == -1 or values_end_index == -1:
        return False
    string_format = rgba_string[0:values_start_index]
    if string_format not in ["rgb", "rgba"]:
        return False
    if values_end_index < len(rgba_string) - 1:
        return False
    values_are_valid = values_valid(rgba_string[values_start_index + 1:values_end_index], string_format)
    return values_are_valid


def values_valid(values_string, string_format):
    amount_required_parameters = 4 * (string_format == "rgba") + 3 * (string_format == "rgb")
    values_separated = values_string.split(",")
    if len(values_separated) != amount_required_parameters:
        return False
    for i in range(3):
        if len(values_separated[i].strip()) < 1:
            return False
        if values_separated[i][-1] == "%":
            if not values_separated[i][:-1].isnumeric():
                return False
            if int(values_separated[i][:-1]) > 100:
                return False
            continue
        if not values_separated[i].isnumeric():
            return False
        if int(values_separated[i]) > 255:
            return False
    if amount_required_parameters > 3:
        if not is_float(values_separated[3]):
            return False
        if float(values_separated[3]) < 0 or float(values_separated[3]) > 1:
            return False
    return True


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


print("True tests:")
print(valid_color("rgba(0,0,0,0)"))
print(valid_color('rgb(255,255,255)'))
print(valid_color("rgba(0,0,0,0.123456789)"))
print(valid_color('rgb(0%,50%,100%)'))
print(valid_color('rgba(	0 , 127	, 255 , 0.1)'))
print(valid_color('rgba(0,0,0,.8)'))


print("False tests:")
print(valid_color("rgb(255,256,255)"))
print(valid_color('rgb(100%,100%,101%)'))
print(valid_color("rgb(0,,0)"))
print(valid_color('rgba(0,0,0,1.1)'))
print(valid_color('rgba(0,0,0,-1)'))
