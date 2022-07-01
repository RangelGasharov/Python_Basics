print("Two\nrows")
print("\"Quotation marks\"")

phrase = "This variable is a String"
print("Variable: " + phrase)
print("Is the String upper case?: " + str(phrase.isupper()))
print("Is the String upper case?: " + str(phrase.upper().isupper()))
print("Upper case version of String: " + phrase.upper())
print("Lower case version of String: " + phrase.lower())
print("Length of the String in characters: " + str(len(phrase)))
print("")
print("Position which contains \"S\": " + str(phrase.index("S")))
print("Position which contains \"variable\": " + str(phrase.index("variable")))
# print(phrase.index("z")) --> cannot be found
print(phrase.replace("String", "string."))
