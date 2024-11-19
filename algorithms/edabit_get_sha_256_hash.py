import hashlib


def get_sha256_hash(word):
    hash_object = hashlib.sha256(word.encode("utf-8"))
    return hash_object.hexdigest()


print(get_sha256_hash("password123"))
print(get_sha256_hash("Fluffy@home"))
print(get_sha256_hash("Hey dude!"))
print(get_sha256_hash("hi"))
print(get_sha256_hash("don't use easy passwords"))
