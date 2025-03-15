def split_into_buckets(word_string, length_bucket):
    word_split = word_string.split()
    result = []
    current_string = ""
    for i in range(len(word_split)):
        factor = 1 if current_string != "" else 0
        if len(current_string) + len(word_split[i]) + factor <= length_bucket:
            if current_string != "":
                current_string += " " + word_split[i]
            else:
                current_string += word_split[i]
            if i == len(word_split) - 1:
                result.append(current_string)
        else:
            if current_string != "":
                result.append(current_string)
                current_string = word_split[i]
                if i == len(word_split) - 1:
                    result.append(current_string)
            else:
                if len(word_split[i]) <= length_bucket:
                    current_string = word_split[i]
                else:
                    current_string = ""
    return result


print(split_into_buckets("she sells sea shells by the sea", 10))
print(split_into_buckets("the mouse jumped over the cheese", 7))
print(split_into_buckets("fairy dust coated the air", 20))
print(split_into_buckets("a b c d e", 2))
print(split_into_buckets("rich magnificent trees dotted the landscape", 15))
print(split_into_buckets("rich magnificent trees dotted the landscape", 22))
print(split_into_buckets("rich magnificent trees dotted the landscape", 40))
print(split_into_buckets("rich magnificent trees dotted the landscape", 43))
print(split_into_buckets("do the hokey pokey", 12))
