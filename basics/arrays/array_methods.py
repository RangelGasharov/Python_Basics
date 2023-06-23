# remove prefix and remove suffix
websites = ["www.google.com", "www.wikipedia.com", "www.asean.org", "www.youtube.com", "www.facebook.com"]
for link in websites:
    print(link.removeprefix("www."))
for link in websites:
    print(link.removesuffix(".com"))
