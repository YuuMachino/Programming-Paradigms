#Atividade:
#Criar uma classe chamada carro com: Atributos, cor modelo, ano
#Criar metodos (funcoes): mostrar_dados e ligar_carro

class Carro:
    def __init__(self, atributos, cor, modelo, ano):
        self.atributos=atributos
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        

    def ligar_carro (self):
        print("Carro Ligado")



    def mostrar_dados(self):
        print("Atributos: ", self.atributos)
        print("Cor: ", self.cor)
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)

c1=Carro("Farol amarelo", "Vermelho", "Chevet", 1964)

c1.ligar_carro()
c1.mostrar_dados()
