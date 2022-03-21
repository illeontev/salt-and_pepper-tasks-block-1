from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, name: str = None, calories: int = None, \
                 flavor: str = None) -> None:
        super().__init__(name, calories)
        self.flavor = flavor

    def is_delicious(self) -> bool:
        """возвращает False в случае если вкус - 'black licorice'"""
        if self.flavor == 'black licorice':
            return False
        return True


if __name__ == '__main__':
    jelly_bean = JellyBean('JB1', 150, 'red licorice')
    print(jelly_bean.is_healthy()) # True
    print(jelly_bean.is_delicious()) # True

    jelly_bean = JellyBean('JB1', 5.45, 'black licorice')
    print(jelly_bean.is_healthy()) # False
    print(jelly_bean.is_delicious()) # False
