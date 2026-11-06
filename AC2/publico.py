class Transporte:
    def __init__(self, linha, capacidade):
        self.__linha = linha
        self.__capacidade = capacidade
    
    def get_linha(self):
        return self.__linha

    def get_capacidade(self):
        return self.__capacidade

    def transportar(self):
        pass

class Motorista:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome

class Condutor:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class Onibus(Transporte):
    def __init__(self, linha, capacidade, nomeMotorista):
        super().__init__(linha, capacidade)
        self.motorista = Motorista(nomeMotorista)

    def transportar(self):
        super().transportar()
        print(f"O ônibus está transportando passageiros com o motorista: {self.motorista.get_nome()}")

class Metro(Transporte):
    def __init__(self, linha, capacidade, nomeCondutor):
        super().__init__(linha, capacidade)
        self.condutor = Condutor(nomeCondutor)

    def transportar(self):
        super().transportar()
        print(f"O metrô está transportando passageiros com o condutor: {self.condutor.get_nome()}")

transportes = [
    Onibus("033", "30", "Sergio"),
    Metro("Amarela", "150", "Bruno")
]
for transporte in transportes:
    transporte.transportar()