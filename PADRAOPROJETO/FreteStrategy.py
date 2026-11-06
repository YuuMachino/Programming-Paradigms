from abc import ABC, abstractmethod

class FreteStrategy(ABC):
    @abstractmethod
    def calcular(self):
        pass


class FreteEconomico(FreteStrategy):
    def calcular(self):
        return 10.0

class FreteExpresso(FreteStrategy):
        def calcular(self):
            return 25.0

class RetirarLoja(FreteStrategy):
        def calcular(self):
            return 0.0

class FreteDrone(FreteStrategy):
        def calcular(self):
            return 5.0

class Pedido:
    def __init__(self, frete: FreteStrategy):
        self.frete=frete

    def calcular_total(self, valor):
        if valor<0:
            raise ValueError("Valor invalido")
        return valor + self.frete.calcular()

pedido1=Pedido(FreteEconomico())
pedido2=Pedido(FreteExpresso())
pedido3=Pedido(RetirarLoja())
pedido4=Pedido(FreteDrone())

print(f"Frete Economico: {pedido1.calcular_total(100)}")
print(f"Frete Expresso: {pedido2.calcular_total(100)}")
print(f"Retirar na loja: {pedido3.calcular_total(100)}")
print(f"Frete por drone: {pedido4.calcular_total(100)}")

