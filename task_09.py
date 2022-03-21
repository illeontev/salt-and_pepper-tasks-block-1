def connect_dicts(dict1: dict, dict2: dict) -> dict:
    """соединяет два переданных словаря, значениями ключей
    в которых являются числа, и возвращает новый словарь,
    полученный по следующим правилам:
    • приоритетными являются ключи того словаря, сумма значений
      ключей которого больше
      (если суммы значений ключей будут равны, то второй словарь
      считается более приоритетным)
    • ключи со значениями меньше 10 не должны попасть в
      финальный словарь
    • получившийся словарь должен вернуться упорядоченным по
      значениям ключей в порядке возрастания."""

    keys = set(dict1.keys()) | set(dict2.keys())

    priority = 2
    if sum(dict1.values()) > sum(dict2.values()):
        priority = 1

    res_dict = {}
    for key in keys:
        value = 0
        if key in dict1 and key in dict2:
            if priority == 1:
                value = dict1[key]
            else:
                value = dict2[key]
        elif key in dict1:
            value = dict1[key]
        elif key in dict2:
            value = dict2[key]

        if value >= 10:
            res_dict[key] = value

    # сортируем итоговый словарь по значениям ключей
    return {k: v for k, v in sorted(res_dict.items(), key=lambda x: x[1])}


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
# => { "c": 11, "b": 12 }

print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
# => { d: 11, "c": 12, "a": 13 }

print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
# => { "c": 11, "b": 12, "a": 15 }