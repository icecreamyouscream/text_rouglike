import config
from typing import NoReturn
from backpack import Backpack

class Hero:
    """Базовый класс героя

    Attributes:
        storage (Backpack): рюкзак для хранения предметов и расходников"""

    storage: Backpack = Backpack()

    def __init__(self, name: str) -> None:
        """Метод инициализации класса
        :param name: Имя героя
        :type name: str"""
        self.name: str = name
        self.__lvl: int = config.start_lvl
        self.__exp: int = config.start_exp
        self.__hp: int = config.base_hp
        self.__dmg: int = config.base_dmg
        self.__def: int = config.base_def
        self.__mana: int = config.base_mana

    def get_lvl(self) -> int:
        """Геттер для получения показателя уровня
        :return: __lvl"""
        return self.__lvl

    def get_exp(self) -> int:
        """Геттер для получения показателя очков опыта
        :return: __exp"""
        return self.__exp

    def get_hp(self) -> int:
        """Геттер для получения показателя очков здоровья
        :return: __hp"""
        return self.__hp

    def get_dmg(self) -> int:
        """Геттер для получения показателя урона
        :return: __dmg"""
        return self.__dmg

    def get_def(self) -> int:
        """Геттер для получения показателя защиты
        :return: __def"""
        return self.__def

    def get_mana(self) -> int:
        """Геттер для получения показателя очков маны
        :return: __mana"""
        return self.__mana

    def put_in_backpack(self, item, amount: int=1) -> None:
        """Метод добавления предмета и его количества в рюкзак
        :param item: Объект предмета
        :type item: object
        :param amount: Количество предметов
        :type amount: int

        :return: None"""

        if item in self.storage:
            self.storage[item] += amount
        else:
            self.storage.setdefault(item, amount)

    def get_from_backpack(self, item, amount: int=1) -> tuple[object, int]:
        """Метод изъятия предмета из рюкзака

        :param item: Объект предмета
        :type item: object
        :param amount: Количество предметов
        :type amount: int

        :return: Кортеж, состоящий из предмета и его количества"""

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


    def open_backpack(self) -> None:
        """Метод просмотра содержимого рюкзака
        :return: None"""
        print("Содержимое рюкзака:")
        for key, value in self.storage.items():
            print(f'    {key}: {value}')


class Knight(Hero):
    """Класс рыцарь"""
    def __init__(self, name: str) -> None:
        """Метод инициализации класса
        :param name: Имя рыцаря
        :type name: str"""
        super().__init__(name)

    def __str__(self) -> str:
        """Метод возврата строкового представления объекта (Рыцарь)
        :return: строку текущих характеристик рыцаря"""
        return (f'{self.name} - {self.get_lvl()} lvl\n'
                f'{self.get_hp()}hp/{self.get_mana()}mp\n'
                f'{self.get_exp()} exp')
