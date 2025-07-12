def longest_common_prefix(words):
    if not words:
        return ""

    longest_prefix = ""
    current_index = 0
    min_len = min(len(w) for w in words)

    while current_index < min_len:
        current_letter = words[0][current_index]

        for i in range(len(words)):
            if words[i][current_index] != current_letter:
                return longest_prefix

        longest_prefix += current_letter
        current_index += 1

    return longest_prefix


print(longest_common_prefix(["apple", "application", "apply"]))
print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["reflower", "flow", "flight"]))
