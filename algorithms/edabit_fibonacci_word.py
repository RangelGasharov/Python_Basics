def fibo_word(n):
    if n < 2:
        return "Invalid"
    fibonacci_words = ["b", "a"]
    fibonacci_words.extend([""] * (n - 2))
    for i in range(2, n):
        fibonacci_words[i] = fibonacci_words[i - 1] + fibonacci_words[i - 2]
    return fibonacci_words[:n]


print(fibo_word(1))
print(fibo_word(3))
print(fibo_word(7))
print(fibo_word(10))
print(fibo_word(20))
