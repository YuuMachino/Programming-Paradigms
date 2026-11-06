class Hospedagem:
    def __init__(self, nome, valor_diaria):
        self.__nome = nome
        self.__valor_diaria = valor_diaria
    
    def get_nome(self):
        return self.__nome

    def get_valor_diaria(self):
        return self.__valor_diaria

    def reservar(self):
        pass

class Endereco:
        def __init__(self, estado, cidade):
            self.__estado = estado
            self.__cidade = cidade
        def get_estado(self):
            return self.__estado
        def get_cidade(self):
            return self.__cidade


class Hotel(Hospedagem):
    def __init__(self, nome, valor_diaria, nomeEstado, nomeCidade):
        super().__init__(nome, valor_diaria)
        self.endereco = Endereco(nomeEstado, nomeCidade)


    def reservar(self):
        super().reservar()
        print(f"Reserva realizada no hotel do estado de {self.endereco.get_estado()} na cidade de {self.endereco.get_cidade()}")

class Pousada(Hospedagem):
    def __init__(self, nome, valor_diaria, nomeCidade, nomeEstado):
        super().__init__(nome, valor_diaria)
        self.endereco = Endereco(nomeEstado, nomeCidade)


    def reservar(self):
        super().reservar()
        print(f"Reserva realizada na pousada do estado de {self.endereco.get_estado()} na cidade de {self.endereco.get_cidade()}")

hospedagens = [
    Hotel("Deluxe", "150,99", "SP", "Guarulos"),
    Pousada("ResortPraia", "249,99", "RJ", "Panama")
]
for hospedagem in hospedagens:
    hospedagem.reservar()