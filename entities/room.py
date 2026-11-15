from enum import StrEnum
from abc import ABC, abstractmethod


class RoomType(StrEnum):
    """Класс типов комнат."""

    ITEM_ROOM = "Сокровищница"
    FIGHT_ROOM = "Боевая комната"
    BOSS_ROOM = "Комната босса"
    CRAFT_ROOM = "Комната крафта"
    REST_ROOM = "Комната отдыха"
    LIGHT_ROOM = "Комната-маяк"


class Room(ABC):
    """Абстрактный класс комнаты."""

    @abstractmethod
    def __init__(self, room_type: RoomType) -> None:
        """Метод инициализации класса.

        :param room_type: Тип комнаты."""

        self.room_type = room_type
