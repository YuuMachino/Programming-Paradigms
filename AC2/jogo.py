class Personagem:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
    
    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def atacar(self):
        pass

class Arma:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class Guerreiro(Personagem):
    def __init__(self, nome, vida, nomeArma):
        super().__init__(nome, vida)
        self.arma = Arma(nomeArma)

    def atacar(self):
        super().atacar()
        print(f"O guerreiro atacou com a arma: {self.arma.get_nome()}")

class Mago(Personagem):
    def __init__(self, nome, vida, nomeArma):
        super().__init__(nome, vida)
        self.arma = Arma(nomeArma)

    def atacar(self):
        super().atacar()
        print(f"O mago lançou uma : {self.arma.get_nome()}")

personagens = [
    Guerreiro("Fouth", "500", "Espada"),
    Mago("Vleunfr", "150", "Bola de fogo")
]
for personagem in personagens:
    personagem.atacar()