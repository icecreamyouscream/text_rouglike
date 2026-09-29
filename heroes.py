from typing import NoReturn
from backpack import Backpack


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
    storage: Backpack = Backpack()

    def __init__(self, name: str) -> None:
        """
        Метод инициализации класса
        Args:
            name(str): имя героя
        """
        self.name: str = name
        self.__lvl: int = self.start_lvl
        self.__exp: int = self.start_exp
        self.__hp: int= self.base_hp
        self.__dmg: int = self.base_dmg
        self.__def: int = self.base_def
        self.__mana: int = self.base_mana

    def get_lvl(self) -> int:
        """
        Геттер для получения показателя уровня
        Returns: __lvl
        """
        return self.__lvl

    def get_exp(self) -> int:
        """
        Геттер для получения показателя очков опыта
        Returns: __exp
        """
        return self.__exp

    def get_hp(self) -> int:
        """
        Геттер для получения показателя очков здоровья
        Returns: __hp
        """
        return self.__hp

    def get_dmg(self) -> int:
        """
        Геттер для получения показателя урона
        Returns: __dmg
        """
        return self.__dmg

    def get_def(self) -> int:
        """
        Геттер для получения показателя защиты
        Returns: __def
        """
        return self.__def

    def get_mana(self) -> int:
        """
        Геттер для получения показателя очков маны
        Returns: __mp
        """
        return self.__mana

    def put_in_backpack(self, item, amount=1) -> NoReturn:
        """
        Метод добавления предмета и его количества в рюкзак
        Args:
            item(str): наименование предмета
            amount(int): количество предметов

        Returns: None
        """
        if item in self.storage:
            self.storage[item] += amount
        else:
            self.storage.setdefault(item, amount)

    def get_from_backpack(self, item, amount=1) -> tuple[str, int]:
        """
        Метод изъятия предмета и его количества из рюкзака
        Args:
            item(str): Наименование предмета
            amount(int): Количество предметов

        Returns:
            Кортеж, содержащий наименование и количество предметов
            tuple[str, int]
        """
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


    def open_backpack(self) -> NoReturn:
        """
        Метод просмотра содержимого рюкзака
        Returns: None
        """
        print("Содержимое рюкзака:")
        for key, value in self.storage.items():
            print(f'    {key}: {value}')


class Knight(Hero):
    """
    Класс рыцарь. Родитель Hero.
    """
    def __init__(self, name: str) -> None:
        """
        Метод инициализации класса
        Args:
            name(str): Имя рыцаря
        """
        super().__init__(name)

    def __str__(self) -> str:
        """
        Метод возврата строкового представления объекта (Рыцарь)
        Returns: str
        """
        return (f'{self.name} - {self.get_lvl()} lvl\n'
                f'{self.get_hp()}hp/{self.get_mana()}mp\n'
                f'{self.get_exp()} exp')
