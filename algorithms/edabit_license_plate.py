def license_plate(license_code, group_length):
    filtered_code = ""
    for i in range(len(license_code)):
        if license_code[i] != "-":
            filtered_code += license_code[i].upper()
    filtered_code_groups = []
    current_group_index = -1
    for i in range(1, len(filtered_code) + 1):
        if i % group_length == 0:
            filtered_code_groups.append(
                filtered_code[-i:current_group_index] + (i == group_length) * filtered_code[-1])
            current_group_index = -i
    if current_group_index != -(len(filtered_code)):
        filtered_code_groups.append(filtered_code[0:current_group_index])
    final_license_code = ""
    for i in range(1, len(filtered_code_groups)):
        final_license_code += filtered_code_groups[-i] + "-"
    final_license_code += filtered_code_groups[-len(filtered_code_groups)]
    return final_license_code


print(license_plate("5F3Z-2e-9-w", 4))
print(license_plate("2-5g-3-J", 2))
print(license_plate("2-4A0r7-4k", 3))
print(license_plate("nlj-206-fv", 3))
