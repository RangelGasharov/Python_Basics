def sock_pairs(letters_string):
    letters_string_array = list(letters_string)
    letters_string_array.sort()
    index_last_pair = -1
    amount_of_pairs = 0
    for i in range(len(letters_string_array) - 1):
        if letters_string_array[i] == letters_string_array[i + 1] and i != index_last_pair:
            amount_of_pairs += 1
            index_last_pair = i + 1
    return amount_of_pairs


print(sock_pairs("AA"))
print(sock_pairs("ABABC"))
print(sock_pairs("CABBACCC"))
print(sock_pairs("ACDBE"))
print(sock_pairs(""))
print(sock_pairs("ABABAB"))
print(sock_pairs("AAAAA"))
