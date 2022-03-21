def combine_anagrams(words_array: list) -> list:
    """принимает на вход массив слов и разбивает их на группы
    по анаграммам. Регистр букв не имеет значения при определении
    анаграмм."""
    dict_result = {}
    for word in words_array:
        key = tuple(sorted(list(word.lower())))
        dict_result.setdefault(key, []).append(word)
    return list(dict_result.values())


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four",
                        "scar", "creams", "scream"]))
# => [ ["cars", "racs", "scar"], ["four"], ["for"],
# ["potatoes"], ["creams", "scream"] ])