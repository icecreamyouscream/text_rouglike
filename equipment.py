from abc import ABC, abstractmethod
from enum import StrEnum
from generator import IGeneratable


class EquipType(StrEnum):
    """Класс типов предметов."""

    WEAPON = "Оружие"
    ARMOR = "Броня"
    COLLECTIBLE = "Расходники"

class Equip(ABC):
    """Абстрактный класс предметов."""

    @abstractmethod
    def __init__(self, name: str, item_type: str) -> None:
        """Метод инициализации класса.

        :param name: Наименование предмета.
        :param item_type: Тип предмета."""

        self.name = name
        self.item_type = item_type


class Armor(Equip):
    """Класс брони."""

    def __init__(self, name: str) -> None:
        """Метод инициализации класса.

        :param name: Наименование брони."""

        super().__init__(name=name, item_type=EquipType.ARMOR)

    def __repr__(self):
        """Класс репрезентации класса.

        :return: Строковое наименование класса."""
        return self.name


class Weapon(Equip):
    """Класс оружия"""
    
    def __init__(self, name: str) -> None:
        """Метод инициализации класса.
        
        :param name: Наименование оружия"""
        
        super().__init__(name=name, item_type=EquipType.WEAPON)

    def __repr__(self):
        """Метод репрезентации класса.

        :return: Строковое наименование класса."""
        return self.name


class Collectible(Equip):
    """Класс расходников"""

    def __init__(self, name: str) -> None:
        """Метод инициализации класса.

        :param name: Наименование предмета."""

        super().__init__(name=name, item_type=EquipType.COLLECTIBLE)

    def __repr__(self):
        """Метод репрезентации класса.

        :return: Строковое представление класса."""
        return self.name


class EquipGenerator(IGeneratable):


    def generate(self, name: str) -> Equip:
        pass
