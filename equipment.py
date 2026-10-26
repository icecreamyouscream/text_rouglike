from abc import ABC, abstractmethod
from enum import StrEnum
from generator import IGeneratable


class EquipType(StrEnum):
    WEAPON = "Оружие"
    ARMOR = "Броня"
    COLLECTIBLE = "Расходники"

class Equip(ABC):
    """Абстрактный класс предметов."""

    @abstractmethod
    def __init__(self, name: str, item_type: str) -> None:
        self.name = name
        self.item_type = item_type


class Armor(Equip):
    """Класс брони."""

    def __init__(self, name: str) -> None:

        super().__init__(name=name, item_type=EquipType.ARMOR)

    def __repr__(self):
        return self.name


class Weapon(Equip):
    """Класс оружия"""
    
    def __init__(self, name: str) -> None:
        """Метод инициализации класса.
        
        :param name: Наименование оружия"""
        
        self.name = name

    def __repr__(self):
        return self.name

    def name(self) -> str:
        return self.name


class Collectible(Equip):
    """Класс расходников"""

    def __init__(self, name: str) -> None:
        """Метод инициализации класса.

        :param name: Наименование предмета."""

        self.name = name

    def __repr__(self):
        return self.name

    def name(self) -> str:
        return self.name

class EquipGenerator(IGeneratable):

    def generate(self, name: str) -> Equip:
        pass
