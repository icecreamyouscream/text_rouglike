from abc import ABC, abstractmethod


class IGeneratable(ABC):

    @abstractmethod
    def generate(self):
        pass
