import config
from equipment import Equip, EquipType
from backpack import Backpack


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

        if (needed_item := str(item.item_type)) in self.storage:
            for piece in self.storage[needed_item]:
                if item not in piece: # todo СОВЕТ код проще воспринимается, когда у тебя утверждение, а не отрицаие, если можно написать код без not , то лучше написать без нот, то есть в данной ситуации можно поменять иф и элс местами
                    self.storage[needed_item].append([item])
                    break # todo у тебя брейк в любом случае выполняется, подумай как можно сократить на одну строчку, чтобы смысл не потерялся
                else:
                    piece.append(item)
                    break
        else:
            self.storage.setdefault(str(item.item_type), [[item]]) #todo прелесть StrEnum в том что не нужно кастовать к стринге, у тебя уже стринга, как сторедж класса Storage , но унаследован от дикта

    def get_from_backpack(self, item: Equip) -> list[Equip]: # todo pycharm ругается, посмотри - либо измени выход, либо аннотацию выхода
        """Метод изъятия предмета из рюкзака.

        :param item: Объект предмета
        :return: Список изъятых предметов"""

        taken_item = []
        for value in self.storage.values():
            for piece in value:
                if (needed_item := item) in piece:
                    taken_item.append(needed_item)
                    piece.remove(needed_item)
                    break
        if len(taken_item) == 1: #todo а если больше 1?
            return taken_item
        else:
            print(f'В рюкзаке нет {item}')

    def open_backpack(self) -> None:
        """Метод просмотра содержимого рюкзака.

        :return: None"""

        print("Содержимое рюкзака:")
        for key, value in self.storage.items():
            print(f"    {key}:")
            for piece in value:
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
            f"{self.get_exp()} exp"
        )
