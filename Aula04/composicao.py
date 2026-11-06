#Composição: uma classe tem outra classe, istancia-se um objeto ja dentro da classe
#Herança: Uma classe herda atributos de outra classe

class Motor:
    def ligar(self):
        print("Motor ligado")



class Carro:
    def __init__(self, modelo):
        self.modelo=modelo
        self.motor=Motor()
    def ligar(self):
        print(f"Ligando {self.modelo}")
        self.motor.ligar()


carro=Carro("Fusca")

carro.ligar()