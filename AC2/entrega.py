class Entrega:
    def __init__(self, destino, preco):
        self.__destino = destino
        self.__preco = preco
    
    def get_destino(self):
        return self.__destino

    def get_preco(self):
        return self.__preco

    def realizar_entrega(self):
        pass

class Entregador:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class EntregaMoto(Entrega):
    def __init__(self, destino, preco, nomeEntregador):
        super().__init__(destino, preco)
        self.entregador = Entregador(nomeEntregador)

    def realizar_entrega(self):
        super().realizar_entrega()
        print(f"Entrega sendo realizada de moto pelo entregador: {self.entregador.get_nome()}")

class EntregaCaminhao(Entrega):
    def __init__(self, destino, preco, nomeEntregador):
        super().__init__(destino, preco)
        self.entregador = Entregador(nomeEntregador)

    def realizar_entrega(self):
        super().realizar_entrega()
        print(f"Entrega sendo realizada de caminhão pelo entregador: {self.entregador.get_nome()}")

entregas = [
    EntregaMoto("SP", "4,00", "Bruno"),
    EntregaCaminhao("RJ", "150,00", "Carlos")
]
for entrega in entregas:
    entrega.realizar_entrega()