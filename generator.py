from abc import ABC, abstractmethod
from typing import Any


class IGeneratable(ABC):
    """Абстрактный класс генератора сущностей."""

    @abstractmethod
    def generate(self, some_type) -> Any:
        pass
