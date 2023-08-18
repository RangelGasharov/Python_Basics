import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.;:-_/\\!?`´*'=&%$§°+#"

upper, lower, nums, syms = True, True, True, True

used_elements = ""

if upper:
    used_elements += uppercase_letters
if lower:
    used_elements += lowercase_letters
if nums:
    used_elements += digits
if syms:
    used_elements += symbols

length = 20
amount = 5

for x in range(amount):
    password = "".join(random.sample(used_elements, length))
    print(password)
