def hex_to_binary(hex_num):
    dictionary = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110",
                  "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101",
                  "E": "1110", "F": "1111"}
    result = ""
    for x in range(2, len(hex_num)):
        result += dictionary[hex_num[x]]
    return result


print(hex_to_binary("0xFF"))
print(hex_to_binary("0xAA"))
print(hex_to_binary("0xFA"))
