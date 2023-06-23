# remove prefix and remove suffix
websites = ["www.google.com", "www.wikipedia.com", "www.asean.org", "www.youtube.com", "www.facebook.com"]
for link in websites:
    print(link.removeprefix("www."))
for link in websites:
    print(link.removesuffix(".com"))

# filter with a function + list function

numbers = range(1, 1000)


def is_prime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True


primes = list(filter(is_prime, numbers))

print(primes)
