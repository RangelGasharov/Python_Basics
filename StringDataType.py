print("Two\nrows")
print("\"Quotation marks\"")

phrase = "This variable is a String"
print("Variable: " + phrase)
print(phrase.isupper())
print(phrase.upper().isupper())
print("Upper case version of String: " + phrase.upper())
print("Lower case version of String: " + phrase.lower())
print(len(phrase))
print("")
print(phrase.index("S"))
print(phrase.index("String"))
# print(phrase.index("z")) --> cannot be found
print(phrase.replace("String", "string"))
