def restore_ip_address(text):
    text_length = len(text)
    possible_ip_addresses = []
    for i in range(1, min(4, text_length - 2)):
        for j in range(i + 1, min(i + 4, text_length - 1)):
            for k in range(j + 1, min(j + 4, text_length)):
                part1 = text[:i]
                part2 = text[i:j]
                part3 = text[j:k]
                part4 = text[k:]
                if all(map(is_valid_number, [part1, part2, part3, part4])):
                    ip = f"{part1}.{part2}.{part3}.{part4}"
                    possible_ip_addresses.append(ip)
    return possible_ip_addresses


def is_valid_number(num_string):
    if len(num_string) == 0 or (num_string[0] == "0" and len(num_string) > 1):
        return False
    return 255 >= int(num_string) >= 0


print(restore_ip_address("25525511135"))
print(restore_ip_address("0000"))
print(restore_ip_address("101023"))
