def is_palindrome(string: str) -> bool:
    """определяет, является ли параметр string палиндромом
    при условии игнорирования пробелов, знаков препинания
    и регистра."""
    buf = ''
    for c in str(string).lower():
        if c.isalnum():
            buf += c

    return str(buf) == str(buf)[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False