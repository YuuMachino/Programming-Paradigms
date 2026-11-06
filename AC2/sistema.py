class Servico:
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__carga_valor = valor
    
    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def executar(self):
        pass

class Profissional:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class ServicoLimpeza(Servico):
    def __init__(self, descricao, valor, nomeProfissional):
        super().__init__(descricao, valor)
        self.profissional = Profissional(nomeProfissional)

    def executar(self):
        super().executar()
        print(f"Executando serviço de limpeza pelo profissional: {self.profissional.get_nome()}")

class ServicoManutencao(Servico):
    def __init__(self, descricao, valor, nomeProfissional):
        super().__init__(descricao, valor)
        self.profissional = Profissional(nomeProfissional)

    def executar(self):
        super().executar()
        print(f"Executando serviço de limpeza pelo profissional: {self.profissional.get_nome()}")

servicos = [
    ServicoLimpeza("Limpeza a vacoo", "50,00", "Roberto"),
    ServicoManutencao("Encanamento", "27,00", "Pauline")
]
for servico in servicos:
    servico.executar()