class Publicacao:
    def __init__(self, titulo, ano):
        self.__titulo = titulo
        self.__ano = ano
    
    def get_titulo(self):
        return self.__titulo

    def get_ano(self):
        return self.__ano

    def exibir_informacoes(self):
        pass

class Editora:
        def __init__(self, nome):
            self.__nome = nome
        def get_nome(self):
            return self.__nome


class Livro(Publicacao):
    def __init__(self, titulo, ano, nomeEditora):
        super().__init__(titulo, ano)
        self.editora = Editora(nomeEditora)

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"O guerreiro atacou com a arma: {self.editora.get_nome()}")

class Revista(Publicacao):
    def __init__(self, titulo, ano, nomeEditora):
        super().__init__(titulo, ano)
        self.editora = Editora(nomeEditora)

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"O guerreiro atacou com a arma: {self.editora.get_nome()}")

publicacoes = [
    Livro("Pedra, papel e tesoura", "2020", "Darkside"),
    Revista("Vogue", "2015", "Vogue")
]
for publicacao in publicacoes:
    publicacao.exibir_informacoes()