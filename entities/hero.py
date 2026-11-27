import config
from entities.equipment import Equip
from entities.backpack import Backpack


class Hero:
    """Базовый класс героя."""

    storage: Backpack = Backpack()

    def __init__(self, name: str) -> None:
        """Метод инициализации класса.

        :param name: Имя героя"""

        self.name: str = name
        self.__lvl: int = config.START_LVL
        self.__exp: int = config.START_EXP
        self.__hp: int = config.BASE_HP
        self.__dmg: int = config.BASE_DMG
        self.__def: int = config.BASE_DEF
        self.__mana: int = config.BASE_MANA

    def get_lvl(self) -> int:
        """Геттер для получения показателя уровня.

        :return: __lvl"""

        return self.__lvl

    def get_exp(self) -> int:
        """Геттер для получения показателя очков опыта.

        :return: __exp"""

        return self.__exp

    def get_hp(self) -> int:
        """Геттер для получения показателя очков здоровья.

        :return: __hp"""

        return self.__hp

    def get_dmg(self) -> int:
        """Геттер для получения показателя урона.

        :return: __dmg"""

        return self.__dmg

    def get_def(self) -> int:
        """Геттер для получения показателя защиты.

        :return: __def"""

        return self.__def

    def get_mana(self) -> int:
        """Геттер для получения показателя очков маны.

        :return: __mana"""

        return self.__mana

    def put_in_backpack(self, item: Equip) -> None:
        """Метод добавления предмета в рюкзак.

        :param item: Объект предмета
        :return: None"""

        if (needed_type := str(item.item_type)) in self.storage:
            if (needed_item := item.name) in self.storage[needed_type]:
                self.storage[needed_type][needed_item].append(item)
            else:
                self.storage[needed_type].setdefault(item.name, [item])
        else:
            self.storage.setdefault(needed_type, {})
            # todo давай для Backpack сразу создадим небольшую структуру, мы заранее знаем какие у нас есть типы итемов, так что можем минимальную структуру с типами создать на этапе создания рюкзака
            self.storage[needed_type].setdefault(item.name, [item])

    def get_from_backpack(self, item: Equip) -> Equip | None:
        """Метод изъятия предмета из рюкзака.

        :param item: Объект предмета.
        :return: Объект предмета."""

        if (needed_type := str(item.item_type)) in self.storage:
            if (needed_item := item.name) in self.storage[needed_type]:
                taken_item = self.storage[needed_type][needed_item].pop(0)
                if len(self.storage[needed_type][needed_item]) < 1:
                    self.storage.pop(needed_type)
                return taken_item
            else:
                print(f'\nНет предмета: {item}\n')
        else:
            print(f'\nНет предмета: {item}\n')

    def open_backpack(self) -> None:
        """Метод просмотра содержимого рюкзака.

        :return: None"""

        print("Содержимое рюкзака:")
        for key, value in self.storage.items():
            print(f"    {key}:")
            for piece in value.values():
                print(f"        {piece[0]} * {len(piece)}")


class Knight(Hero):
    """Класс рыцаря."""

    def __init__(self, name: str) -> None:
        """Метод инициализации класса.

        :param name: Имя рыцаря"""

        super().__init__(name)

    def __str__(self) -> str:
        """Метод возврата строкового представления объекта (Рыцарь).

        :return: Строку, содержащую в себе информацию о рыцаре"""

        return (
            f"{self.name} - {self.get_lvl()} lvl\n"
            f"{self.get_hp()}hp/{self.get_mana()}mp\n"
            f"{self.get_exp()} exp\n"
        )
