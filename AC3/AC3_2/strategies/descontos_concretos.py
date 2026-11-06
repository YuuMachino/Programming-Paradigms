from strategies.desconto import DescontoStrategy


class DescontoComum(DescontoStrategy):

    def calcular(self, valor: float) -> float:
        return valor - (valor * 0.05)


class DescontoVIP(DescontoStrategy):

    def calcular(self, valor: float) -> float:
        return valor - (valor * 0.10)


class DescontoPremium(DescontoStrategy):

    def calcular(self, valor: float) -> float:
        return valor - (valor * 0.20)
