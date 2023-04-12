s = "hello"
print("Capitalize:", s, s.capitalize())
s = "a0BcdEF"
print("Casefold:", s, s.casefold())
print("Center".center(20, "."))
s = "aaaabbbbcccc"
print("Count:", s, "aa:", s.count("aa"))
s = "Text"
print(s.encode(encoding="UTF-8", errors="strict"))
s = "orange"
print("Ends with:", s, "ends with e:", s.endswith("e"))
s = "text\ttext2\ttext3"
print("Expand tabs", s.expandtabs(20))
s = "abcdefg"
print("Find", s, "e:", s.find("e"))
s = "{one} and {two}"
print("Format", s.format(one="first", two="second"))
