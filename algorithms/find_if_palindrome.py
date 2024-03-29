def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True

    if text[0] == text[len(text) - 1]:
        return is_palindrome(text[1:len(text) - 1])

    return False


print(is_palindrome("racecar"))
print(is_palindrome("a"))
print(is_palindrome("hello"))
print(is_palindrome("abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"))
