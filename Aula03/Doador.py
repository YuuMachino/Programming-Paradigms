##Criar uma classe Doador com os atributos: nome, total doado (inicia em 0). Precisam estar encapsulados
##Metodos: Realizar doação(valor), mostrar total


class Doador:
    def __init__(self, nome, valor):
        self.nome=nome
        self.__valor=valor
    @property
    def realizar_doacao(self):
        return self.__valor
    

    @realizar_doacao.setter
    def realizar_doacao(self, dinheiro):
        if dinheiro >0:
            self.__valor+=dinheiro
        else:
            self.__valor
    

d1=Doador("joao", 0)
print(d1.nome)
d1.realizar_doacao=10000
print(d1.realizar_doacao)