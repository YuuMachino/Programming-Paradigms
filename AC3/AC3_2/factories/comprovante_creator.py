from abc import ABC, abstractmethod

from factories.comprovante import Comprovante
from factories.comprovantes_concretos import ComprovanteSimples, ComprovanteDetalhado


class ComprovanteCreator(ABC):

    @abstractmethod
    def criar_comprovante(self) -> Comprovante:
        pass

    def emitir_comprovante(self, pedido, total: float) -> str:
        comprovante = self.criar_comprovante()
        return comprovante.emitir(pedido, total)


class ComprovanteSimplesCreator(ComprovanteCreator):

    def criar_comprovante(self) -> Comprovante:
        return ComprovanteSimples()


class ComprovanteDetalhadoCreator(ComprovanteCreator):

    def criar_comprovante(self) -> Comprovante:
        return ComprovanteDetalhado()
