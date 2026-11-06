from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def abastecer (self):
        pass
class VeiculoEletrico(ABC):
    def carregar(self):
        pass

class Carro(Veiculo):
    def abastecer(self):
        print("Abastecendo carro")

class Moto(Veiculo):
    def abastecer(self):
        print("Abastecendo carro")

class CarroEletrico(Veiculo):
    def carregar(self):
        print("Carregando carro")