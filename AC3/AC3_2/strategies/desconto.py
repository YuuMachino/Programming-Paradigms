from abc import ABC, abstractmethod


class DescontoStrategy(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

    def get_nome(self) -> str:
        return self.__class__.__name__
