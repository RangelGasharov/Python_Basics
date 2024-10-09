def molar_mass(compound):
    compounds = {"Water": "H2 O", "BoricAcid": "H3 B O3", "SulfuricAcid": "H2 S O4",
                 "NitricAcid": "H N O3", "HydroChloricAcid": "H Cl"}
    atoms = {"H": 1, "B": 10, "O": 16, "S": 32, "N": 14, "Cl": 35}
    total_molar_mass = 0
    current_compound = compounds[compound]
    separated_compounds = separate_words(current_compound)
    for i in range(len(separated_compounds)):
        current_group = separated_compounds[i]
        index_amount = 0
        for j in range(len(current_group)):
            if current_group[j].isnumeric():
                index_amount = j
                break
        index_amount = (index_amount == 0) * (len(current_group)) + index_amount
        if index_amount == len(current_group):
            amount_group = 1
        else:
            amount_group = int(current_group[index_amount: len(current_group)])
        total_molar_mass += atoms[current_group[:index_amount]] * amount_group
    return total_molar_mass


def separate_words(text):
    separated_words = []
    current_word = ""
    for i in range(len(text)):
        if text[i] == " ":
            separated_words.append(current_word)
            current_word = ""
        else:
            current_word += text[i]
    separated_words.append(current_word)
    return separated_words


print(molar_mass("Water"))
print(molar_mass("BoricAcid"))
print(molar_mass("SulfuricAcid"))
print(molar_mass("NitricAcid"))
print(molar_mass("HydroChloricAcid"))
