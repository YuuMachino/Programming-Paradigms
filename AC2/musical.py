class Instrumento:
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca
    
    def get_nome(self):
        return self.__nome

    def get_marca(self):
        return self.__marca

    def apresentar(self):
        print(f"Nome: {self.__nome}")
        print(f"Marca:{self.__marca}")
    
    def tocar(self):
        pass

class Musico:
    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome=nome

class Violao(Instrumento):
    def __init__(self, nome, marca, nomeMusico):
        super().__init__(nome, marca)
        self.musico = Musico(nomeMusico)

    def tocar(self):
        super().tocar()
        print(f"O violao esta sendo tocado pelo musico: {self.musico.get_nome()}")

class Piano(Instrumento):
    def __init__(self, nome, marca, nomeMusico):
        super().__init__(nome, marca)
        self.musico = Musico(nomeMusico)

    def tocar(self):
        super().tocar()
        print(f"O piano esta sendo tocado pelo musico: {self.musico.get_nome()}")

instrumentos = [
    Violao("Violao roxo", "MCV", "Carlos"),
    Piano("Piano classico", "toyota", "Beth")
]

for instrumento in instrumentos:
    instrumento.tocar()