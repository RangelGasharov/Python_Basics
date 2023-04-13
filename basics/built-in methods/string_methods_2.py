S = ""
s = "hello"
print("Capitalize:", s, s.capitalize())
s = "a0BcdEF"
print("Casefold:", s, s.casefold())
print("Center".center(20, "."))
s = "aaaabbbbcccc"
print("Count:", s, "aa:", s.count("aa"))
s = "Text"
print("Ecode", s.encode(encoding="UTF-8", errors="strict"))
s = "orange"
print("Ends with:", s, "ends with e:", s.endswith("e"))
s = "text\ttext2\ttext3"
print("Expand tabs", s.expandtabs(20))
s = "abcdefg"
print("Find", s, "e:", s.find("e"))
s = "{one} and {two}"
print("Format", s.format(one="first", two="second"))
coordinates = {"x": 4, "y": 3}
s = "Coordinates ({x}, {y})"
print("Format Map", s.format_map(coordinates))
s = "Text for testing"
print("Index", s, "for:", s.index("for"))
s = "test123"
print("Isalnum", s, s.isalnum())
s = "text"
print("Isalpha", s, s.isalpha())
s = "§"
print("Isascci", s, s.isascii())
s = "532"
print("Isdecimal", s, s.isdecimal())
s = "⓪"
print("Isdigit", s, s.isdigit())
s = "四五八"
print("Isnumeric", s, s.isnumeric())
s = "test-example"
print("Isidentifier", s, s.isidentifier())
s = "Word"
print("Islower", s, s.islower())
s = "Word\n"
print("Isprintable", s, s.isprintable())
s = " "
print("Isspace", s, s.isspace())
s = " "
print("Isspace", s, s.isspace())
s = "The Title Test"
print("Istitle", s, s.istitle())
s = "UPPER"
print("Isupper", s, s.isupper())
s = "-"
print("Join", s.join(["first", "second", "third"]))
s = "ljust"
print("Ljust", s, s.ljust(20, "-"))
