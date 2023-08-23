import pyshorteners

url = input("Enter your url: ")

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    print(shortener.tinyurl.short(url))

shorten_url(url)