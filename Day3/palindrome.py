def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False
