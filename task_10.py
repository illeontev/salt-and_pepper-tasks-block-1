from collections import Counter


def count_words(string_):
    # оставляем в строке только буквы, цифры и пробелы
    new_string = ''
    for c in string_:
        if c.isalnum() or c == ' ':
            new_string += c

    words = [word.lower() for word in new_string.split()]

    # само собой, я в состоянии сгенерировать такой словарь вручную
    # но в данном случае я хочу продемонстрировать знание Counter()
    return dict(Counter(words))


print(count_words("A man, a plan, a canal -- Panama"))
# => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}

print(count_words("Doo bee doo bee doo"))
# => {"doo": 3, "bee": 2}