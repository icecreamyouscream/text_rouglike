class Equip:
    """Общий класс предметов. """

    def __init__(self, name) -> None:
        """Метод инициализации класса.

        :param name: Наименование предмета"""

        self.name = name

    def __repr__(self) -> str:
        """Метод строкового представления объекта (Equip).

        :return: Строку, содержащую в себе наименование предмета"""

        return self.name
