def sort_list(array: list) -> list:
    """меняет местами все минимальные и максимальные элементы
    массива, а также добавляет в конец массива одно
    минимальное значение из него"""
    if not array:
        return []

    # можно было бы использовать встроенные функции min() и max(),
    # но тогда пришлось бы 2 раза бежать по массиву
    min_elem, max_elem = array[0], array[0]
    for el in array:
        if el < min_elem:
            min_elem = el
        if el > max_elem:
            max_elem = el

    result = []
    for el in array:
        if el == min_elem:
            result.append(max_elem)
        elif el == max_elem:
            result.append(min_elem)
        else:
            result.append(el)
    result.append(min_elem)

    return result


print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]