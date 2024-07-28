def security(positioning_string):
    filtered_string = filter_out_empty_spaces(positioning_string)
    for i in range(1, len(filtered_string)):
        if filtered_string[i - 1] == "T" and filtered_string[i] == "$":
            return "ALARM!"
        if filtered_string[i - 1] == "$" and filtered_string[i] == "T":
            return "ALARM!"
    return "Safe"


def filter_out_empty_spaces(positioning_string):
    filtered_string = ""
    for x in positioning_string:
        if x != "x":
            filtered_string += x
    return filtered_string


print(security("xxxxTTxGxx$xxTxxx"))
print(security("xxTxxG$xxxx$xxxx"))
print(security("TTxxxx$xxGxx$Gxxx"))
print(security("xxxTxxxxT"))
print(security("xxTxxxxxxxx$xGxxxxxxT"))
