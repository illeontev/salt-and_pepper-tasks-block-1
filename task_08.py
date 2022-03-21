def multiply_numbers(inputs):
    """возвращает произведение цифр, входящих в inputs."""
    digits = [digit for digit in str(inputs) if digit.isdigit()]

    if not digits:
        return None

    res = 1
    for digit in digits:
        res *= int(digit)
    return res


print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120