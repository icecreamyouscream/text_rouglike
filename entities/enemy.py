from enum import StrEnum


class EnemyType(StrEnum):
    """Класс типов врагов."""

    SWORDSMAN = "Мечник"
    SPEARMAN = "Копейщик"
    ARCHER = "Лучник"


class Enemy:
    """Базовый класс врага."""

    def __init__(self, enemy_type: EnemyType) -> None:
        """Метод инициализации класса.

        :param enemy_type: Тип врага."""

        self.enemy_type = enemy_type


class Swordsman(Enemy):
    """Класс врага-мечника."""

    def __init__(self) -> None:
        """Метод инициализации класса."""

        super().__init__(enemy_type=EnemyType.SWORDSMAN)


class Spearman(Enemy):
    """Класс врага-копейщика."""

    def __init__(self) -> None:
        """Метод инициализации класса."""

        super().__init__(enemy_type=EnemyType.SPEARMAN)


class Archer(Enemy):
    """Класс врага-лучника."""

    def __init__(self) -> None:
        """Метод инициализации класса."""

        super().__init__(enemy_type=EnemyType.ARCHER)
