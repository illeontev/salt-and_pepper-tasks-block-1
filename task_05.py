from datetime import datetime, timedelta


def date_in_future(integer: int) -> datetime:
    """возвращает текущую дату через integer дней.
    Если integer не является целым числом, метод
    возвращает текущую дату"""
    format_string = '%d-%m-%Y %H:%M:%S'
    current_date = datetime.now()

    if not isinstance(integer, int):
        return current_date.strftime(format_string)

    result_date = current_date + timedelta(days=integer)
    return result_date.strftime(format_string)


print(date_in_future([]))  # => текущая дата
print(date_in_future(2))  # => текущая дата + 2 дня
