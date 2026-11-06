'''
2.O -Open/close
'''
from abc import ABC, abstractmenthod
'''
Aqui estou criando uma interface
No python, temos o ABC que server como nossa interface no java
o abstractmethod é tipo um contrato, sem corpo, apenas uma função, sendo obrigado a utilizado
'''
class Desconto(ABC):
    @abstractmenthod
    def calcular(self, valor):
        pass

class DescontoComum(Desconto):
    def calcular(self, valor):
        return valor * 0.05

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.10

#funcao responsavel por aplicar desconto
def aplicar_desconto(desconto, valor):
    return desconto.calcular(valor)

 

comum=DescontoComum()
premim=DescontoPremium()

valor_compra=1000

desconto_comum = aplicar_desconto(comum, valor_compra)
desconto_premim=aplicar_desconto(premim, valor_compra)

print(desconto_comum:.2f)
print(desconto_premim:.2f)


''' 
Nossa interface veio justo para subistituir todos esses metodos dentro de uma classe, onde se
precisarmos adicionar outro tipo de cliente, tipo um gold, não precisamos modificar nossa classe
nos apenas adicionamos mais uma classe com nosso contrato(DESCONTO)

class CalcularDesconto(Desconto):

    def calcular(self, tipo_cliente, valor):
       if tipo_cliente == "comum":
            return valor * 0.05
        elif tipo_cliente == "Premium":
            return valor * 0.1
        elif tipo_cliente == "vip":
            return valor * 0.15'''