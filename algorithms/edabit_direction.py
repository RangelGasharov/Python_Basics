def direction(list_of_directions):
    output_direction = "west"
    result = []
    for input_direction in list_of_directions:
        result_word = ""
        index = 0
        for letter in input_direction:
            if letter.isalpha():
                if letter.isupper():
                    result_word += output_direction[index % len(output_direction)].upper()
                else:
                    result_word += output_direction[index % len(output_direction)]
                index += 1
            else:
                result_word += letter
        result.append(result_word)
    return result


print(direction(["east", "EAST", "eastEAST"]))
print(direction(["eAsT EaSt", "EaSt eAsT"]))
print(direction(["east EAST", "e a s t", "E A S T"]))
