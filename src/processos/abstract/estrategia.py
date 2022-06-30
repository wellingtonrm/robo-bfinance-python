from abc import ABC, abstractmethod


class Estrategia(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def montarestrategia(self) -> None:
        pass

    @abstractmethod
    def foreachSymbolControle(self) -> None:
        pass

    @abstractmethod
    def executarRobo(self):
        pass


