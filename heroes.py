import config
from backpack import Backpack

class Hero:
    """Базовый класс героя

    Attributes: # todo излишне
        storage (Backpack): рюкзак для хранения предметов и расходников"""

    storage: Backpack = Backpack()

    def __init__(self, name: str) -> None:
        """Метод инициализации класса
        :param name: Имя героя
        :type name: str"""

        self.name: str = name
        self.__lvl: int = config.start_lvl
        self.__exp: int = config.start_exp
        self.__hp: int= config.base_hp
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

    def put_in_backpack(self, item, amount: int=1) -> None: # todo аннотация итема
        # про эмаунт - убери его, загляни еще раз в задачку, как мы будем вести наш рюкзак
        # upd: нашел у тебя к тому же готовый класс Equip - в качестве небольшого задания добавь в мейне новый предмет
        # пусть это будет Меч в наш рюкзак (представь, что наш Член шел и нашел меч, он его закинул в рюкзак)
        """Метод добавления предмета и его количества в рюкзак

        :param item: Объект предмета
        :type item: object # todo типы договорились не описывать, нигде не видел, чтобы так делали, аннотации достаточно
        :param amount: Количество предметов
        :type amount: int

        :return: None"""

        if item in self.storage:
            self.storage[item] += amount
        else:
            self.storage.setdefault(item, amount)

    def get_from_backpack(self, item, amount: int=1) -> tuple[object, int]: # todo нет аннотации для итема
        # сразу скажу, что если судить по аннотации возвращаемого значения, то ты не прав, подумай еще
        """Метод изъятия предмета и его количества из рюкзака

        :param item: Объект предмета
        :type item: object
        :param amount: Количество предметов
        :type amount: int

        :return: Кортеж, состоящий из объекта предмета и его количества"""

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
        """Метод просмотра содержимого рюкзака # todo первая строчка в докстринге обычно заканчивается точкой
        # а потом идет пустая строка
        :return: None"""
        print("Содержимое рюкзака:")
        for key, value in self.storage.items():
            print(f'    {key}: {value}')


class Knight(Hero):
    """Класс рыцаря"""

    def __init__(self, name: str) -> None:
        """Метод инициализации класса
        :param name: Имя рыцаря"""
        super().__init__(name)

    def __str__(self) -> str:
        """Метод возврата строкового представления объекта (Рыцарь)
        :return: Строку, содержащую в себе информацию о рыцаре"""

        return (f'{self.name} - {self.get_lvl()} lvl\n'
                f'{self.get_hp()}hp/{self.get_mana()}mp\n'
                f'{self.get_exp()} exp')
