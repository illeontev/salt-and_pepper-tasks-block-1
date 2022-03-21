import numbers


def coincidence(list_: list = None, range_: range = None) -> list:
    """определяет элементы из массива list_, значения которого
    входят в указанный диапазон range_"""
    if list_ is None or range_ is None:
        return []
    return [el for el in list_ if isinstance(el, numbers.Number)
            and range_.start <= el < range_.stop]


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
# => [3, 4, 5]

print(coincidence())
# => []

print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
# => [1, 2, 2.5]
