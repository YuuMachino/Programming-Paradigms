from abc import ABC, abstractmethod


def formatar_moeda(valor: float) -> str:
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


class Comprovante(ABC):

    @abstractmethod
    def emitir(self, pedido, total: float) -> str:
        pass
