from typing import Any
from backpack import Backpack

# TODO test
class Hero:
    """
    Базовый класс героя

    Args:
        name(str): имя героя

    Attributes:
        start_lvl(int): стартовый уровень
        start_exp(int): стартовый показатель опыта
        base_hp(int): стартовый показатель здоровья
        base_dmg(int): стартовый показатель урона
        base_def(int): стартовый показатель защиты
        base_mana(int): стартовый показатель маны
    """

    start_lvl: int = 1
    start_exp: int = 0
    base_hp: int = 100
    base_dmg: int = 5
    base_def: int = 5
    base_mana: int = 10
    storage: dict = Backpack()

    def __init__(self, name: str):
        self.name: str = name
        self.__lvl: int = self.start_lvl
        self.__exp: int = self.start_exp
        self.__hp: int= self.base_hp
        self.__dmg: int = self.base_dmg
        self.__def: int = self.base_def
        self.__mana: int = self.base_mana

    def get_lvl(self) -> int:
        return self.__lvl

    def get_exp(self) -> int:
        return self.__exp

    def get_hp(self) -> int:
        return self.__hp

    def get_dmg(self) -> int:
        return self.__dmg

    def get_def(self) -> int:
        return self.__def

    def get_mana(self) -> int:
        return self.__mana

    def put_in_backpack(self, item, amount=1) -> dict:
        if item in self.storage:
            self.storage[item] += amount
        else:
            self.storage.setdefault(item, amount)
        return self.storage

    def get_from_backpack(self, item, amount=1) -> tuple:
        if item in self.storage:
            self.storage[item] -= amount
        if self.storage[item] < 0:
            print(f'Невозможно взять столько {item}.')
            self.storage[item] += amount
        elif self.storage[item] == 0:
            del self.storage[item]
            print(f'Получено {amount} {item}. В рюкзаке больше нет {item}.')
        else:
            print(f'Получено {amount} {item}. В рюкзаке осталось {self.storage[item]} {item}.')
        return item, amount


    def open_backpack(self) -> dict:
        print("Backpack's content:")
        for key, value in self.storage.items():
            print(f'    {key}: {value}')
        return self.storage


class Knight(Hero):
    """
    Класс рыцаря, наследуемый базовыйм классом Hero
    """
    def __init__(self, name) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return (f'{self.name} - {self.get_lvl()} lvl\n'
                f'{self.get_hp()}hp/{self.get_mana()}mp\n'
                f'{self.get_exp()} exp')
