class Prato:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def preparar(self):
        pass

class Cozinheiro:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class PratoPrincipal(Prato):
    def __init__(self, nome, preco, nomeCozinheiro):
        super().__init__(nome, preco)
        self.cozinheiro = Cozinheiro(nomeCozinheiro)

    def preparar(self):
        super().preparar()
        print(f"Preparando o prato principal pelo Chef: {self.cozinheiro.get_nome()}")

class Sobremesa(Prato):
    def __init__(self, nome, preco, nomeCozinheiro):
        super().__init__(nome, preco)
        self.cozinheiro = Cozinheiro(nomeCozinheiro)

    def preparar(self):
        super().preparar()
        print(f"Preparando a sobremesa pelo chef: {self.cozinheiro.get_nome()}")

pratos = [
    PratoPrincipal("Frango ao molho", "45,99", "Moratti"),
    Sobremesa("Sorvete", "15,00", "Morgana")
]
for prato in pratos:
    prato.preparar()