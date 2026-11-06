from produto import Produto
from strategies.desconto import DescontoStrategy


class Pedido:

    def __init__(self, desconto: DescontoStrategy):
        self.__produtos: list[Produto] = []
        self.__desconto = desconto

    def get_produtos(self) -> list[Produto]:
        return list(self.__produtos)

    def get_desconto(self) -> DescontoStrategy:
        return self.__desconto

    def adicionar_produto(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def calcular_total_bruto(self) -> float:
        return sum(produto.calcular_subtotal() for produto in self.__produtos)

    def calcular_total_final(self) -> float:
        return self.__desconto.calcular(self.calcular_total_bruto())
