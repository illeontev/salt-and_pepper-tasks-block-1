from numbers import Number

def max_odd(array: list) -> Number:
    """определяет максимальный нечетный элемент в массиве array"""
    odd_elems = [el for el in array if isinstance(el, Number) and el % 2 == 1]
    if odd_elems:
        return int(max(odd_elems))
    return None


print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4])) # => None