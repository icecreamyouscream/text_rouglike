class Equip:
    """Общий класс предметов"""
    def __init__(self, name: str):
        """Метод инициализации класса
        :param name: наименование предмета"""
        self.name = name

    def __str__(self) -> str:
        """Метод строкового представления объекта (Equip)
        :return: строку, содержащую в себе наименование предмета"""
        return self.name
