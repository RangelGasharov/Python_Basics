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
s = "UPPERCASE"
print("Lower", s, s.lower())
s = "Random text"
print("Lstrip", s, s.lstrip("Random "))
s = "aaabbbccc"
t = s.maketrans("a", "g")
print("Maketrans and translate", s, s.translate(t))
s = "a+b=c"
print("Partition", s, s.partition("="))
s = "undefined"
print("Removeprefix", s, s.removeprefix("un"))
s = "actually"
print("Removesuffix", s, s.removesuffix("ly"))
s = "The result is 7"
print("Replace", s, s.replace("7", "8"))
s = "abcdeffedcba"
print("Rfind", s, s.rfind("a"))
s = "abbbbcade"
print("Rindex", s, s.rindex("a"))
s = "text"
print("Rjust", s, s.rjust(20, "-"))
s = "a=b=c=d"
print("Rjpartition", s, s.rpartition("="))
s = "www.website.com"
print("RSplit", s, s.rsplit("."))
print("Split", s, s.split(".", maxsplit=1))
s = "Redundant data data"
print("RStrip", s, s.rstrip("data"))
s = "Line1\n Line2\n Line3"
print("Splitlines", s, s.splitlines(keepends=True))
s = "Orange"
print("Startswith", s, s.startswith("O"))
s = "Redundant data again again"
print("Strip", s, s.strip("again"))
s = "let this be a title"
print("Title", s, s.title())
s = "this text is uppercase"
print("Upper", s, s.upper())
s = "text"
print("Zfill", s, s.zfill(10))
