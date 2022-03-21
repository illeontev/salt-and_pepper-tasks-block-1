class Dessert:

    def __init__(self, name: str = None, calories: int = None) -> None:
        self.name = name
        self.calories = calories

    def is_healthy(self) -> bool:
        """возвращает True при условии калорийности десерта
        менее 200"""
        if self.calories is None:
            return False
        return self.calories < 200

    def is_delicious(self) -> bool:
        """возвращает True для всех десертов"""
        return True


cake = Dessert('cake', 250)
apple = Dessert('apple', 150)
none = Dessert()

print(cake.is_healthy())  # False
print(apple.is_healthy())  # True
print(none.is_healthy())  # False

print(cake.is_delicious())  # True
print(apple.is_delicious())  # True
print(none.is_delicious())  # True
