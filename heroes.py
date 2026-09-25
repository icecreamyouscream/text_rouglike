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

    start_lvl = 1
    start_exp = 0
    base_hp = 100
    base_dmg = 5
    base_def = 5
    base_mana = 10

    def __init__(self, name):
        self.name = name
        self.__lvl = self.start_lvl
        self.__exp = self.start_exp
        self.__hp = self.base_hp
        self.__dmg = self.base_dmg
        self.__def = self.base_def
        self.__mana = self.base_mana

    def get_lvl(self):
        return self.__lvl

    def get_exp(self):
        return self.__exp

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def get_def(self):
        return self.__def

    def get_mana(self):
        return self.__mana


class Knight(Hero):
    """
    Класс рыцаря, наследуемый базовыйм классом Hero
    """
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return (f'{self.name} - {self.get_lvl()} lvl\n'
                f'{self.get_hp()}hp/{self.get_mana()}mp\n'
                f'{self.get_exp()} exp')
