class Dessert:

    def __init__(self, name: str = None, calories: str = None) -> None:
        self.name = name
        self.calories = calories

    def get_name(self) -> str:
        return self.name

    def set_name(self, name):
        self.name = name

    def get_calories(self) -> str:
        return self.calories

    def set_calories(self, calories: str):
        self.calories = calories

    def is_healthy(self) -> bool:
        """возвращает True при условии калорийности десерта
        менее 200"""
        if self.calories is None:
            return False

        try:
            calories_num = float(self.calories)
        except:
            return False

        return calories_num < 200

    def is_delicious(self) -> bool:
        """возвращает True для всех десертов"""
        return True


# этот файл импортируется в task_12.py, поэтому ставим такую защиту
if __name__ == '__main__':
    dessert1 = Dessert()
    dessert1.set_calories("test_calories")
    print(dessert1.is_healthy())
    print(dessert1.is_delicious())

    dessert2 = Dessert()
    dessert2.set_calories('195.58')
    print(dessert2.is_healthy())
    print(dessert2.is_delicious())

