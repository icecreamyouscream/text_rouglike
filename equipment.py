class Equip:
    """Общий класс предметов."""

    def __init__(self, name) -> None:
        """Метод инициализации класса.

        :param name: Наименование предмета"""

        self.name = name

    def __repr__(self) -> str:
        """Метод представления объекта.

        :return: Строку, содержащую в себе наименование предмета"""

        return self.name

class Armor(Equip):
    """Класс брони."""

    def __init__(self, name: str) -> None:
        """Метод инициализации класса.

        :param name: Наименование брони"""

        super().__init__(name)

    def __repr__(self) -> str:
        """Метод представления брони.

        :return: Строку, содержащую в себе наименование брони"""

        return self.name

class Weapon(Equip):
    """Класс оружия"""
    
    def __init__(self, name: str) -> None:
        """Метод инициализации класса.
        
        :param name: Наименование оружия"""
        
        super().__init__(name)

    def __repr__(self) -> str:
        """Метод представления оружия.

        :return: Строку, содержащую в себе наименование оружия"""

        return self.name
